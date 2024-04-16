
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
    channel=grpc.insecure_channel(host+port_address)
    stub=map_red_pb2_grpc.Kmeans(channel)
    request=map_red_pb2.MastertoMapperRequest(indexes=shard_data,centorids=centroids)
    response=stub.MastertoMapper(request)
    mapper_output.append(response.status)








def reducer_call(port_address):
    channel=grpc.insecure_channel(host+port_address)
    stub=map_red_pb2_grpc.Kmeans(channel)
    request=map_red_pb2.MastertoReducerRequest(go_ahead=1)
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

    address_space_mappers=5050

    address_space_reducers=5150


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
        port_num=str(mappers[i+1])
        command=["python3", "mapper.py", port_num,str(num_reducers)]
        subprocess.run(command)

    for i in range(num_reducers):
        port_num=str(reducers[i+1])
        command=["python3","reducer.py",port_num,str(num_mappers),str(i+1)]
        subprocess.run(command)
#shard the data, indexes
    with open('points.txt','r') as f:
        l=f.readlines()

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
        for i in range(num_reducers):
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
            if sum(mapper_output)==len(num_mappers):
                for i in range(num_reducers):
                    thread=threading.Thread(target=reducer_call,args=(reducers[i+1]))
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
                    
            else:
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
