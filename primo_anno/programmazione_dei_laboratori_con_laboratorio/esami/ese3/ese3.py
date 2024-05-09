a=[1,2,3,4,5,1.0,2.0,3.0,4.0,5.0,'ads', 'bds', 'cdsd', 'dsd', 'esd']

k = len(a)//3   
res = list(zip(a[0:k], a[k:2*k], a[2*k:3*k]))
for i in range(k): 
    print(res[i],'\n')

