
import subprocess

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
        command=["python3", "mapper.py", port_num]
        subprocess.run(command)
    
    for i in range(num_reducers):
        port_num=str(reducers[i+1])
        command=["python3","reducer.py",port_num,str(num_mappers)]
    with open('points.txt') as f:
        f.readlines
        

#shard the data, indexes and shi.


#call the mappers


#when call of mappers is received

#detect failure

#call reducers 

#detect failure

#if failure dont decrease iter

#rinse and repeat till conversion or iterations