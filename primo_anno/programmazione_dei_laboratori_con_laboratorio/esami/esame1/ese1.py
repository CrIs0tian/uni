def sort_by_freq(l): 
    d = {}
    for x in l: 
        d[x]= d.get(x, 0)+1
    l.sort(key = lambda x:d[x])
    return l

L = ['a', 4,4,4,4, 2, 2, 'b', 'b', 'b']

sort_by_freq(L)
print(L)

#costo spaziale = O(n) nel caso peggiore
#costo temporale = O(n) realizzazzione dizionario + O(nlogn) costo sort = O(nlogn) 



