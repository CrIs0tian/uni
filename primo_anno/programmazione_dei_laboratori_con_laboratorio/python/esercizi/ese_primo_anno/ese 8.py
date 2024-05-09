'''
Esercizi per casa

    1) Si progetti una funzione denominata init_tuple che prenda in input un intero positivo n e, 
    opzionalmente, una funzione v. La funzione restituisca una tupla di lunghezza n che in 
    posizione i contenga v(i). Qualora il parametro v non fosse specificato, 
    la funzione restituirebbe una tupla composta da n zeri.
    
    [Suggerimento. Potrebbe essere utile partire da una tupla vuota 
    - si indica così () - e poi procedere per concatenazioni successive. 
    A tal proposito si provi ad usare l'operatore + come si fa con le stringhe. 
    Una tupla composta da un unico elemento e si definisce in questo modo (e, ).]

    2) Utilizzare la funzione init_tuple per creare una tupla contenente i primi 10 numeri dispari

    3) Utilizzare la funzione init_tuple per creare una tupla contenente 10 stringhe non vuote di 
    lunghezza crescente

    4) Utilizzare la funzione init_tuple per creare una tupla contenente 10 tuple tali che la tupla 
    in posizione i sia lunga 10 e contenga i in ogni posizione. Suggerimento: come per le stringhe,
    * sulle tuple è l'operatore di ripetizione.

'''

def init_tuple(n, v=None):
    t = ()
    if (v == None):
        for i in range(n):
            t+=(0,)
        return t
    for i in range (n): 
        t += (v(i),)
    return t

t = init_tuple(10, )
print (t)


def init_tuple(n):
    t = ()
    for i in range (n): 
        p = (i,)
        p*=10
        t += (p,)
    return t
t = init_tuple(8)
print (t)
