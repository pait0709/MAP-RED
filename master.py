import time
import subprocess
import numpy as np
import grpc
import map_red_pb2
import map_red_pb2_grpc
import threading
reducer_output=[]
mapper_output=[]
reducer_centroids=[]
host='localhost:'
def mapper_call(port_address,shard_data,centroids):
    with grpc.insecure_channel(host+str(port_address)) as channel:
        stub=map_red_pb2_grpc.KmeansStub(channel)
        str_centroids=[]
        for i in range(len(centroids)):
            str_centroids.append(str(centroids[i][0])+" "+str(centroids[i][1]))
        request=map_red_pb2.MastertoMapperRequest(indexes=shard_data,centroids=str_centroids)
        response=stub.MastertoMapper(request)
        mapper_output.append(response.status)








def reducer_call(port_address,centroids):
    with grpc.insecure_channel(host+str(port_address)) as channel:
        str_centroids=[]
        for i in range(len(centroids)):
            str_centroids.append(str(centroids[i][0])+" "+str(centroids[i][1]))
        stub=map_red_pb2_grpc.KmeansStub(channel)
        request=map_red_pb2.MastertoReducerRequest(go_ahead=1,centroids=str_centroids)
        response=stub.MastertoReducer(request)
        reducer_output.append(response.status)
        reducer_centroids.append(response.output)




if __name__=="__main__":
    #when master takes input
    #initialise the relevant number of child programs and assign address space
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
            
    # for i in range(num_reducers):
    #     port_num=str(reducers[i+1])
    #     command=["python3","reducer.py",port_num,str(num_mappers),str(i+1)]
    #     subprocess.run(command)
    # print("waiting 10 secs run both the scripts")
    # time.sleep(10)
    with open('points.txt','r') as f:
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
    is_start=True
    j=0
    while j<num_iters:

        threads_mapper=[]
        threads_reducer=[]
        if is_start:
                centorids=centorids
        else:
            #need to write
            pass
        for i in range(num_mappers):
            thread=threading.Thread(target=mapper_call,args=(mappers[i+1],mapper_shards[i],centorids))
            thread.start()
            threads_mapper.append(thread)
        for t in threads_mapper:
            t.join()
        if sum(mapper_output)==num_mappers:
            print("NIGGA")
            for i in range(num_reducers):
                thread=threading.Thread(target=reducer_call,args=(reducers[i+1],centorids))
                thread.start()
                threads_reducer.append(thread)
            for t in threads_reducer:
                t.join()
            if(sum(reducer_output)==num_reducers):
                #do something
                #check convergence
                j+=1
            reducer_output=[]
            reducer_centroids=[]
            mapper_output=[]
            j+=1
                
        else:
            print("NO NIGGA")
            j+=1
            reducer_output=[]
            mapper_output=[]
            reducer_centroids=[]
            continue
                    

                



        




#call the mappers in a thread


#when call of mappers is received

#detect failure

#call reducers

#detect failure

#if failure dont decrease iter

#rinse and repeat till conversion or iterations
