def sort_by_freq(a):
    d = {}
    sorted_keys = []
    for v in a:
        i = 0
        if v not in d.keys():
            d[v] = []
        d[v].append(i)
    
    a.sort(key = lambda x: d[x])
    print(a)
    
L= ['a', 4, 2, 2, 2, 'b', 'b', 1]

sort_by_freq(L)
