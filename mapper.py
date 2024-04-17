
import sys
import time
import map_red_pb2
import map_red_pb2_grpc
import grpc
import os
import numpy as np
from concurrent import futures
from pathlib import Path
import random
class Mapper(map_red_pb2_grpc.KmeansServicer):
    def __init__(self,port,num_reducers):
        self.port=port
        self.num_reducers=num_reducers
        self.dict=dict()
        self.centroids=None


    def startserver(self,port):
        server=grpc.server(futures.ThreadPoolExecutor(max_workers=10000))
        map_red_pb2_grpc.add_KmeansServicer_to_server(self,server)
        server.add_insecure_port(f'localhost:{port}')

        server.start()
        server.wait_for_termination()
    def map(self,indexes):
        self.dict.clear()
        for c in self.centroids:
            self.dict[(c[0],c[1])]=[]
        with open('Input/points.txt','r') as f:
            buffer=f.readlines()
        if(indexes[0]==-1):
            return
        for i in range(len(buffer)):
            buffer[i]=buffer[i].strip('\n')
            buffer[i]=[float(i) for i in buffer[i].split(',')]
        points=np.array(buffer)[indexes]
        points=points.tolist()
        
        for p in points:
            x1,y1=p[0],p[1]
            dis=1e18
            par=[-1,-1]
            for c in self.centroids:
                x2,y2=c[0],c[1]
                temp_dis=((x1-x2)**2)+((y1-y2)**2)
                if(temp_dis<dis):
                    dis=temp_dis
                    par=[x2,y2]
            self.dict[(par[0],par[1])].append([x1,y1])
    
        


    def partition(self):
        
        directory=f"Mappers/M{(int(port_num)%50051)+1}/"
        file_prefix="partition"
        os.makedirs(directory,exist_ok=True)
        for i in range(1,self.num_reducers+1):
            with open(f"{directory+file_prefix}{i}.txt",'w') as f:
                for k in self.dict.keys():
                    ind=self.centroids.index([k[0],k[1]])
                    if((ind%num_reducers)+1==i):
                        for v in self.dict[k]:
                            f.write(f"{ind} {v[0]} {v[1]}\n")
        
        
                    
                        


 
    def MastertoMapper(self, request, context):
        indexes=request.indexes
        centroids=request.centroids

        # self.partition()
        response=map_red_pb2.MastertoMapperResponse()
        float_centroid=[[float(i.split()[0]),float(i.split()[1])] for i in centroids]
        self.centroids=float_centroid
        self.map(indexes)
        self.partition()    
            
        random.seed(time.time())
        random_number = random.randint(1, 2)
        if random_number==1:
            response.status=0
        else:
            response.status=1
        return response

    def get_partition(self,reducer_number):
        directory=f"Mappers/M{(int(port_num)%50051)+1}/"
        file_prefix=f"partition{reducer_number}.txt"
        with open(directory+file_prefix,'r') as f:
            temp_list=f.readlines()
        for i in range(len(temp_list)):
            temp_list[i]=temp_list[i].strip('\n')
        return temp_list
            

    def ReducertoMapper(self, request, context):
        """reducer requests and also sends its reducer number the partitioned files recieves files and status, Reducer is client, mapper is server
        """
        reducer_number=request.reducer_number
        response=map_red_pb2.ReducertoMapperResponse()
        response.output[:]=self.get_partition(reducer_number)
        random.seed(time.time())

        random_number = random.randint(1, 2)
        if random_number==1:
            response.status=0
        else:
            response.status=1
        response.status=1
        return response


if __name__=="__main__":
    received_args=sys.argv
    port_num=received_args[1]
    os.makedirs(f"Mappers/M{(int(port_num)%50051)+1}/",exist_ok=True)
    num_reducers=int(received_args[2])
    mapper=Mapper(port=port_num,num_reducers=num_reducers)
    mapper.startserver(port_num)
