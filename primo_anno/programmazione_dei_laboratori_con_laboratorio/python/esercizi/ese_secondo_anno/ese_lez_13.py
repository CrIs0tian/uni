'''
Si descriva come invocare la funzione bubble_sort in modo 
che questa ordini una lista contenente numeri e stringhe.
Nella lista risultante i numeri dovranno precedere le stringhe;
i numeri dovranno essere ordinati dal più piccolo al più grande;
le stringhe dovranno essere ordinate lessicograficamente.
'''

#soluzione presa e rielaborata dal file lezione14.py    

def prece_stringa(a): 
    if type(a) == str: 
        return (1, a)
    else: 
        return (0, a)

def id(e):
    return e

def bubble_sort(lis, key=None):
    if key == None: 
        key = id
    sort = False
    c = 0
    n = len(lis)
    while not sort:
        sort = True
        for i in range(n-1-c): 
            if key(lis[i]) > key(lis[i+1]):
                sort = False
                lis[i], lis[i+1] = lis[i+1], lis[i]
        c+=1
    return lis

a = [ 3.14, 'python', 2, 'programma', 12, 0, 'corso' ]
a = bubble_sort(a, key = prece_stringa)
print (a)
