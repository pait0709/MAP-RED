import time
import subprocess
import numpy as np
import grpc
import map_red_pb2
import map_red_pb2_grpc
import threading
import os
reducer_output=[]
mapper_output=[]
reducer_centroids=[]
host='localhost:'
def mapper_call(port_address,shard_data,centroids):
    with grpc.insecure_channel(host+str(port_address)) as channel:
        try:
            stub=map_red_pb2_grpc.KmeansStub(channel)
            str_centroids=[]
            for i in range(len(centroids)):
                str_centroids.append(str(centroids[i][0])+" "+str(centroids[i][1]))
            request=map_red_pb2.MastertoMapperRequest(indexes=shard_data,centroids=str_centroids)
            response=stub.MastertoMapper(request)
            mapper_output.append(response.status)
        except grpc.RpcError as e:
            pass

def reducer_call(port_address,centroids):
    with grpc.insecure_channel(host+str(port_address)) as channel:
        try:
            str_centroids=[]
            for i in range(len(centroids)):
                str_centroids.append(str(centroids[i][0])+" "+str(centroids[i][1]))
            stub=map_red_pb2_grpc.KmeansStub(channel)
            request=map_red_pb2.MastertoReducerRequest(go_ahead=1,centroids=str_centroids)
            response=stub.MastertoReducer(request)
            reducer_output.append(response.status)
            reducer_centroids.append(response.centroids)
        except grpc.RpcError as e:
            pass

if __name__=="__main__":
    os.makedirs('Mappers',exist_ok=True)
    os.makedirs('Reducers',exist_ok=True)
    with open('dump.txt','w') as f:
        f.write("Starting Master\n")
    num_mappers=int(input("Number of mappers: "))
    num_reducers=int(input("Num reducers: "))
    num_centroids=int(input("Num centroids: "))
    num_iters=int(input("Num iters: "))
    address_space_mappers=50051
    address_space_reducers=50151
    #initialising address of mappers
    mappers={}
    for i in range(num_mappers):
        mappers[i+1]=address_space_mappers
        address_space_mappers+=1

    #initialising address of reducers

    reducers={}
    for i in range(num_reducers):
        reducers[i+1]=address_space_reducers
        address_space_reducers+=1

    #creating mappers and reducers

    for i in range(num_mappers):
        script_filename = "run_mappers.sh"
        subprocess.Popen(['./run_mappers.sh','mapper.py',str(mappers[i+1]),str(num_reducers)])
            
    for i in range(num_reducers):
        port_num=str(reducers[i+1])
        command=["./run_reducer.sh","reducer.py",port_num,str(num_mappers),str(i+1)]
        subprocess.Popen(command)

    with open('Input/points.txt','r') as f:
        l=f.readlines()
    for i in range(len(l)):
        l[i]=l[i].strip('\n')
        l[i]=[float(z) for z in l[i].split(',')]
    chunks=(len(l)//num_mappers)
    mapper_shards=[[] for i in range(num_mappers)]
    if(len(l)<num_mappers):
        for i in range(len(l)):
                mapper_shards[i].append(i)
        for i in range(len(l),num_mappers):
            mapper_shards[i].append(-1)
    else:
        for i in range(len(l)):
            mapper_shards[i%num_mappers].append(i)

    indices=np.random.choice(len(l),num_centroids,replace=False)
    l_copy=np.array(l)
    centorids=l_copy[indices].tolist()
    with open('centroids.txt','w')as f:
        for i in range(len(centorids)):
            f.write(f"{i+1} {centorids[i][0]} {centorids[i][1]}\n")

    is_start=True
    j=0
    while j<num_iters:
        print("iteration: ",j+1)
        with open('dump.txt','a') as f:
            f.write(f"iteration {j}\n")


        threads_mapper=[]
        threads_reducer=[]
        
        for i in range(num_mappers):
            thread=threading.Thread(target=mapper_call,args=(mappers[i+1],mapper_shards[i],centorids))
            thread.start()
            threads_mapper.append(thread)
        for t in threads_mapper:
            t.join()
        if sum(mapper_output)==num_mappers:
            with open('dump.txt','a') as f:
                f.write("Mapper Sucess\n") 
            for i in range(num_reducers):
                thread=threading.Thread(target=reducer_call,args=(reducers[i+1],centorids))
                thread.start()
                threads_reducer.append(thread)
            for t in threads_reducer:
                t.join()
            if(sum(reducer_output)==num_reducers):
                with open('dump.txt','a') as f:
                    f.write("Reducer Sucess\n") 
                #implementing master side
                
                for p in reducer_centroids:
                    for jl in p:
                        points=jl.split()
                        index=int(points[0])
                        X1=float(points[1])
                        Y1=float(points[2])
                        try:
                            centorids[index]=[X1,Y1]
                        except:
                            continue
               #print(f"Centroids for iteration {j+1}:")
                with open('centroids.txt','w')as f:
                    for i in range(len(centorids)):
                        f.write(f"{i+1} {centorids[i][0]} {centorids[i][1]}\n")
                        print(f"{i+1} {centorids[i][0]} {centorids[i][1]}\n")
                j+=1
            else:
                #print("Reducer Failure, Retrying")   
                with open('dump.txt','a') as f: 
                    f.write("Reducer Failure Occured ,Retrying\n")



            reducer_output=[]
            reducer_centroids=[]
            mapper_output=[]
        else:
            #print("Mapper Failure Retrying")
            with open("dump.txt",'a') as f:
                f.write("Mapper Failure Occured,Retrying\n")

            reducer_output=[]
            mapper_output=[]
            reducer_centroids=[]
            continue
    print("completed please check")
                    
