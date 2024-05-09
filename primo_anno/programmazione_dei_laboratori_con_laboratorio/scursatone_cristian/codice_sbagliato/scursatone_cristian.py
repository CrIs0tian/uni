def second_max(l): 
    n = len(l)
    if n==1 or (l[0]==l[n-1]): 
        return None
    else:
        l.sort() #O(n*logn)
        i=n-1
        max = l[i]
        
        while (l[i]==max): #nel caso peggiore O(n-1)= O(n)
            res=l[i-1]
            i-=1    
        return l[i]


l = [3,7,2,8,8,8,8,5,7,5]
res = second_max(l)
print(res)
#costo temporale = O(nlogn) nel caso peggiore
#costo spaziale = O(1)

