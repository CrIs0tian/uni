def interval_scheduling(a:list)-> list: 
    a.sort(key = lambda x:x[1])
    sol = [] 
    f_s=0
    for i in a: 
        if f_s<=i[0]: 
            f_s=i[1]
            sol.append(i) 
    return sol


a = [(0,6), (1, 4), (3,4), (3,8), (4,7), (5,9), (6,10), (8,11)]
s = interval_scheduling(a)
print(s)