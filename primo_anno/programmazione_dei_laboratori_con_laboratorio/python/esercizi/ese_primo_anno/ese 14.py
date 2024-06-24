"""prima implementazione dell soluzione
(costo inefficiente)"""


def hist(a, bins):
    """
    Input: a una lista di m float e bins una lista di n-1 floats ordinati in modo crescente
    Output: una lista h di n floats tale che:
        - h[0] = numero di elementi in a < bins[0]
        - h[n-1] = numero di elementi in a >= bins[n-2]
        - per i = 1,..., n-2, h[i] = numero di elementi in a >= bins[i-1] e < bin[i]
    """
    h = [0] * len(bins)

    for i in a:
        if i < bins[0]:
            h[0] += 1
        elif i >= bins[len(bins) - 1]:
            h[len(bins) - 1] += 1
    i = 1
    while i < len(bins) - 1:
        for j in a:
            if j >= bins[i - 1] and j < bins[i]:
                h[i] += 1
        i += 1
    return h


a = [1, 2, 3, 90]
bins = [1, 2, 3, 4, 5]
print(hist(a, bins))

"""
-correttezza del codice assicurata, ddato che per ogni valore in a in sostanza viene controllata per ogni singolo valore in bins 
in quale intervallo appartiene. 
-complessità, qua abbiamo un costo altino. considerando n=len(a) e m=len(bins), facciamo n confronti iniziali e poi per m-2 volte vengono fatti
n confronti... in sostanza n + m-2(n)----> O(n*m)
"""


"""seconda implementazione, un po' più efficiente """


def hist2(a, bins):  # assumendo che n = len(a), m = len(bins)
    h = [0] * len(bins)  # O(m)
    a.sort()  # la parte più costosa, O(n*log(n))
    i, j = 0, 0
    while i < len(a):  # caso peggiore---> O(n)
        if j >= len(bins):
            h[len(bins) - 1] += len(a) - i
            return h
        elif a[i] < bins[j]:
            h[j] += 1
            i += 1
        else:
            j += 1
    return h


a = [90, 90, 90, 90]
bins = [1, 2, 3, 4, 5]
print(hist2(a, bins))

"""
complessità -----> O(n*logn + n + n) n per la lista iniziale, n*log(n) per il sort, n per il controllo (dato che nel caso peggiore, vengono 
                    controllati tutti gli elementi in a)
"""
