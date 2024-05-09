'''
    1) Modificare le funzioni bubble_sort e merge_sort in modo che ritornino 
    il numero di confronti eseguiti; scrivere una funzione per testare quanti 
    confronti eseguono i due algoritmi su istanze di lunghezza diversa. 
    La funzione deve eseguire i test su liste generate 'casualmente' 
    di lunghezze diverse e, per ogni test eseguito, deve salvare 
    su una riga di un file csv: la lunghezza della lista usata per il test; 
    numero di confronti eseguiti da bubble_sort; numero di confronti eseguiti da merge_sort.

    2) Modificare la funzione merge_sort rendendo i parametri lx e rx opzionali. 
    Se non indicati, la funzione deve ordinare tutta la lista.

    3) Modificare la funzione dell'Esercizio 1 in modo la questa ritorni un dizionario C 
    che mappi interi a coppie di float con la seguente semantica: C[n] = (b, m) 
    se su liste lunghe n il numero di confronti medi di bubble_sort è stato b 
    e quello di merge_sort è stato m.
'''
#In[]
import random as rn
import os
def bubble_sort(a):
    ordinata = False
    j = 0
    n = len(a)
    count = 0

    while not ordinata:
        ordinata = True
        i = 0
        while i < n-1-j:
            count+=1
            if a[i] > a[i+1]:
                # se la lista è ordinata non entro
                a[i], a[i+1] = a[i+1], a[i]
                count+=1
                ordinata = False
            i += 1
        j += 1
    return count

def merge( a, lx, cx, rx ):
    '''
    Parameters
    ----------
    a : lista di valori confrontabili con < 
        con a[lx:cx] e a[cx:rx] ordinati
        lx<cx<rx
    
    Output: muta a in modo tale che a[lx:rx] sia ordinata 
    '''
    count = 0
    
    c = []
    i, j = lx, cx
    
    # sia n = len(a)
    # sia m = rx-lx
    
    while i < cx and j < rx: # eseguito <= m volte
        if a[i] < a[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(a[j])
            j += 1
        count+=1    
        
    if i == cx:
        k, last_index = j, rx
    else:
        k, last_index = i, cx
    
    while k < last_index: # costo O(m)
        c.append(a[k])
        k += 1
        
    #a = a[:lx] + c + a[rx:] # costo O(n), non va bene!!!!
    
    for t in range(rx-lx): # costo O(m)
        a[lx+t] = c[t]
    return count

def merge_sort(a, lx=0, rx=0):
    if (lx==0 and rx ==0):
        rx=len(a)
    
    '''
    Parameters
    ----------
    a : lista di elementi per cui vale la relazione <
    lx < rx : int, indici in a
    Returns
    -------
    Muta a in modo tale che a[lx:rx] sia ordinata con <
    '''
    
    if rx  == lx  or rx == lx+1:
        return 0
    
    cx = (rx+lx)//2
    c0 = merge_sort(a, lx, cx)
    c1 = merge_sort(a, cx, rx)
    c2 = merge(a, lx, cx, rx)
    return c2+c0+c1
    
    
    
    
L = [10,9, 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0]
count =bubble_sort(L)
print(L, count)
L = [10,9, 8 , 7 , 6 , 5 , 4 , 3 , 2 , 1 , 0]
count = merge_sort(L, 0, len(L))
print(L,count)
print(os.getcwd())
      


def cmp_sort():
    count_merge=0
    count_bubble=0
    l_merge=[]
    l_bubble=[]
    lun = rn.randint(0,100)
    i=0
    while len(l_merge)<lun:
        l_merge.append(rn.random())
    l_bubble=l_merge[:]
    count_bubble=bubble_sort(l_bubble)
    count_merge=merge_sort(l_bubble)
    f=open('test.csv', 'a')
    f.write(f'lunghezza lista = {lun}; confronti con bubble = {count_bubble}; confronti con merge = {count_merge}\n')
    f.close()

for i in range(10):
    cmp_sort()
    
    
