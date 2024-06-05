"""
Esercizio: descrivere come utilizzare la funzione str_cmp in modo che vengano
confrontati i caratteri in posizione 0 di due
stringhe in input x e y. In particolare ritorna -1 se x[0] < y[0];
ritorna 0 se x[0] == y[0]; ritorna +1 altrimenti

molto ez, key(x) è una funzione quindi crei una nuova funzione che restitisce il primo carattere
della stringa
"""


def first_el(x):
    return x[0]


def str_cmp(x, y, key=None):
    """
    Input: x, y, due stringhe; key una funzione con input str
    Output: ritorna -1 se key(x) < key(y); 0 se key(x) è uguale a key(y);
        +1 se key(y)< key(x)
    """

    x0, y0 = (x, y) if key == None else (key(x), key(y))  # espressione condizionale

    if x0 < y0:
        return -1
    if x0 == y0:
        return 0
    return 1


print(str_cmp("Addio", "addio", len))
print(str_cmp("Addio", "addio", str))
print(str_cmp("Addio", "addio", first_el))


"""
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

"""


def id(x):
    return x


def dispari(x):
    return 2 * x + 1


def incr_str(x):
    st = "0" * x
    return st


def ten_tuple(x):
    t = (x,) * 10
    return t


def init_tuple(n, v=None):
    if v == None:
        """se non specifico la funzione stampo una tupla lunga n di 0"""
        res = (0,) * n
        return res
    else:
        res = ()
        for i in range(n):
            res += (v(i),)
        return res


print(init_tuple(10, id), "\n")
print(init_tuple(10, dispari), "\n")
print(init_tuple(10, incr_str))
print(init_tuple(10, ten_tuple))

"""
le funzioni invece di essere scritte cosi possiamo usare il comando lambda, che ci permette di 
creare funzioni molto semplici (quelle che sono come se fossere funzioni matematiche ) e inserirle 
direttamente nei parametri della funzione init_tuple, 

formato lambda 

f(nome funzione) = lambda i(nome variabile controimmagine della funzione): f(i) (corpo funzione )
"""
