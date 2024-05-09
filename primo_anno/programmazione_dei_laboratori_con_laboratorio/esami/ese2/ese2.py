def intersection(d0, d1): 
    res=[]
    for x in d0: 
        if x in d1: 
            res.append(x)
    return res 

d0 = {2:'ehdhei', 8:'jddjjd'}
d1 = {3: 'ddhdh',2: 'dhhdf', 4:'bdddu'}
l = intersection(d0, d1)
print(l)
