def init_list(n,v = lambda x:0):
    l=[]
    for i in range(n):
        l.append(v(i))
    return l
l= init_list(10, v=lambda x: x*8)
print (l)

def rem_none(l):
    for i in range(len(l)):
       if l[i] == None:
           del(l[i])
    return l
l=[1, None]
l = rem_none(l)
print(l)
#codice migliorato e più giusto
def rem_none( a ): #perchè ha un costo medio minore di quello precedente 
    i = 0
    while i < len(a):
        if a[i] == None:
            del(a[i])
        else:
            i += 1
    return a
    