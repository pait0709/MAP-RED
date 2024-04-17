
import grpc
import map_red_pb2
import map_red_pb2_grpc
from concurrent import futures
import sys

class Reducer(map_red_pb2_grpc.KmeansServicer):
    def __init__(self, mappers,reducer_number):
        self.mappers=mappers
        self.reducer_number=reducer_number

    def startserver(self,port):
        server=grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        map_red_pb2_grpc.add_KmeansServicer_to_server(self,server)
        server.add_insecure_port(f'localhost:{port}')
        print("server started")
        server.start()
        server.wait_for_termination()

    def MastertoReducer(self, request, context):
        """master gives the go-ahead to reduce and master recieves status and centroids, Reducer is server, master is client
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

if __name__=="__main__":
    received_args=sys.argv
    port_num=received_args[1]
    num_mappers=int(received_args[2])
    reducer_number=int(received_args[3])

    address_space_mappers=50051
    mappers={}
    #making an address book of all the mappers
    for i in range(num_mappers):
        mappers[i+1]=address_space_mappers
        address_space_mappers+=1
    reducer=Reducer(mappers,reducer_number)
    reducer.startserver(port_num)

    #thread up to server and client shit