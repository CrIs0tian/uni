from utils import * 



def interval_partitioning(a:list) -> list: 
    a.sort(key=lambda x:x[0])
    d = 0 
    schedule = heap() 
    schedule.H[0] = ('c'+d, 0) 
    for i in a: 
        if i[0] >= schedule.H[0].priority: 
            schedule.incr_key_min(0, i[1])
        else: 
            d+=1
            new_c = nodo('c'+d, i[1]) 
            schedule.insert(new_c)

    
    
