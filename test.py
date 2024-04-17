import subprocess
import numpy as np
import grpc
import map_red_pb2
import map_red_pb2_grpc
import threading
host='localhost:'
port_address=50051
mapper_output=[]
shard_data=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
centroids=[[9.5, 1.5], [10.2, 0.5], [0.7, 9.9]]
with grpc.insecure_channel(host+str(port_address)) as channel:
        stub=map_red_pb2_grpc.KmeansStub(channel)
        str_centroids=[]
        for i in range(len(centroids)):
            str_centroids.append(str(centroids[i][0])+" "+str(centroids[i][1]))
        request=map_red_pb2.MastertoMapperRequest(indexes=shard_data,centroids=str_centroids)
        response=stub.MastertoMapper(request)
        print(response.status)
        mapper_output.append(response.status)