
import grpc
import sys
address_space_mappers=5050

if __name__=="__main__":
    received_args=sys.argv
    port_num=received_args[1]
    num_mappers=int(received_args[2])
    reducer_number=int(received_args[3])

    address_space_mappers=5050
    mappers={}
    #making an address book of all the mappers
    for i in range(num_mappers):
        mappers[i+1]=address_space_mappers
        address_space_mappers+=1


    #thread up to server and client shit