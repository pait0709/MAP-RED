
import sys
import map_red_pb2
import map_red_pb2_grpc
import grpc
from concurrent import futures
import random
class Mapper(map_red_pb2_grpc.KmeansServicer):
    def __init__(self,port,num_reducers):
        self.port=port
        self.num_reducers=num_reducers

    def startserver(self,port):
        server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        map_red_pb2_grpc.add_KmeansServicer_to_server(self,server)
        server.add_insecure_port(f"[::]:{port}")
        server.start()
        server.start()
        server.wait_for_termination()
    def map(self,indexes,centroids):
        pass
    def partition(self):
        pass
    def MastertoMapper(self, request, context):
        indexes=request.indexes
        centroids=request.centroids
        self.map(indexes,centroids)
        self.partition()
        response=map_red_pb2.MastertoMapperResponse()
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
    num_reducers=received_args[2]
    mapper=Mapper(port=port_num,num_reducers=num_reducers)
    mapper.startserver(port_num)
