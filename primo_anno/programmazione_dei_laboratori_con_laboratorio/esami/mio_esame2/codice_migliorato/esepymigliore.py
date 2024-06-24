def second_max(l): 
    if len(l)<=1 or l[0] == l[len(l)-1]: 
        return None
    else: 
        max = 0
        sec_max=0 
        for x in l:
            if x > max: 
                sec_max=max 
                max = x
            elif x<max and x > sec_max: 
                sec_max = x
    return sec_max

l =[9,8,7,6,5,4,3,2,1]
max = second_max(l) 
print(max)

#costo temporale = O(n) con n = len(l), 
#costo spaziale = O(1) 
