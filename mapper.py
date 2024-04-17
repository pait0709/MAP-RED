
import sys
import map_red_pb2
import map_red_pb2_grpc
import grpc
import numpy as np
from concurrent import futures
import random
class Mapper(map_red_pb2_grpc.KmeansServicer):
    def __init__(self,port,num_reducers):
        self.port=port
        self.num_reducers=num_reducers
        self.dict=dict()


    def startserver(self,port):
        server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        map_red_pb2_grpc.add_KmeansServicer_to_server(self,server)
        server.add_insecure_port(f'localhost:{port}')

        server.start()
        server.wait_for_termination()
    def map(self,indexes,centroids):
        self.dict.clear()
        for c in centroids:
            self.dict[(c[0],c[1])]=[]
        with open('points.txt','r') as f:
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
            for c in centroids:
                x2,y2=c[0],c[1]
                temp_dis=((x1-x2)**2)+((y1-y2)**2)
                if(temp_dis<dis):
                    dis=temp_dis
                    par=[x2,y2]
            self.dict[(par[0],par[1])].append([x1,y1])
        
        

                

    def partition(self,indexes):
        if self.dict():
    def MastertoMapper(self, request, context):
        print("recieved")
        indexes=request.indexes
        centroids=request.centroids
        # self.map(indexes,centroids)
        # self.partition()
        response=map_red_pb2.MastertoMapperResponse()
        float_centroid=[[float(i.split()[0]),float(i.split()[1])] for i in centroids]
        
            
            

        # random_number = random.randint(1, 2)
        # if random_number==1:
        #     response.status=1
        # else:
        #     response.status=0
        response.status=1
        return response

    def get_partition(self,reducer_number):
        pass
    def ReducertoMapper(self, request, context):
        """reducer requests and also sends its reducer number the partitioned files recieves files and status, Reducer is client, mapper is server
        """
        reducer_number=request.reducer_number
        response=map_red_pb2.ReducertoMapperResponse()
        response.output=self.get_partition(reducer_number)
        # random_number = random.randint(1, 2)
        # if random_number==1:
        #     response.status=1
        # else:
        #     response.status=0
        response.status=1
        return response


if __name__=="__main__":
    received_args=sys.argv
    port_num=received_args[1]
    print("port num of server: "+port_num)
    num_reducers=int(received_args[2])
    mapper=Mapper(port=port_num,num_reducers=num_reducers)
    mapper.startserver(port_num)
