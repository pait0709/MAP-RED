
import grpc
import map_red_pb2
import map_red_pb2_grpc
from concurrent import futures
import sys
import threading

class Reducer(map_red_pb2_grpc.KmeansServicer):
    def __init__(self, mappers,reducer_number):
        self.mappers=mappers
        self.reducer_number=reducer_number
        self.partitioned_files=[]
        self.centroids=None
        self.shuflled_sorted={}

    def mapper_call(self,port):
        host='localhost:'
        with grpc.insecure_channel(host+str(port)) as channel:
            stub=map_red_pb2_grpc.KmeansStub(channel)
            request=map_red_pb2.ReducertoMapperRequest(reducer_number=self.reducer_number)
            response=stub.ReducertoMapper(request)
            if(response.status==1): 
                if(len(response.output)!=0):
                    for x in response.output:
                        self.partitioned_files.append(x)
                print("mapper call cool")
            else:
                print("mapper call failed")
                self.partitioned_files.append("-1")
    
    def shuffle_sort(self):
        for x in self.partitioned_files:
            if (x=="-1"):
                return False
            points=x.split()
            index=points[0]
            X1=points[1]
            Y1=points[2]
            if (index not in self.shuflled_sorted.keys()):
                self.shuflled_sorted[index]=[(X1,Y1)]
            else:
                self.shuflled_sorted[index].append((X1,Y1))
        return True
    
    def reduce(self):
        ans=[]
        for key, value in self.shuflled_sorted.items():
            avg_X1=0
            avg_Y1=0
            for X1,Y1 in value:
                avg_X1+=float(X1)
                avg_Y1+=float(Y1)
            avg_X1/=len(value)
            avg_Y1/=len(value)
            ans.append(f'{key} {avg_X1:.2f} {avg_Y1:.2f}')
        with open(f"R{self.reducer_number}.txt",'w') as f:
            for i in ans:
                f.write(i+"\n")
        return ans

    def startserver(self,port):
        server=grpc.server(futures.ThreadPoolExecutor(max_workers=100))
        map_red_pb2_grpc.add_KmeansServicer_to_server(self,server)
        server.add_insecure_port(f'localhost:{port}')
        print("reducer server started")
        server.start()
        server.wait_for_termination()

    def MastertoReducer(self, request, context):
        response=map_red_pb2.MastertoReducerResponse()
        go_ahead=request.go_ahead
        centroids=request.centroids
        float_centroid=[[float(i.split()[0]),float(i.split()[1])] for i in centroids]
        self.centroids=float_centroid
        threads_mapper=[]
        for i in range(len(self.mappers)):
            thread=threading.Thread(target=self.mapper_call,args=[self.mappers[i+1]])
            thread.start()
            threads_mapper.append(thread)
        for t in threads_mapper:
            t.join()

        flag=self.shuffle_sort()
        if flag:
            ans=self.reduce()
            response.centroids[:]=ans
            response.status=1

        else:
            response.centroids=["-1"]
            response.centroids=0

        self.partitioned_files=[]
        self.centroids=None
        self.shuflled_sorted={}     
        return response
        


        

if __name__=="__main__":
    received_args=sys.argv
    port_num=str(received_args[1])
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