
'''
Esercizio per casa: si scriva una funzione chiamata conta_int()
che prenda in input una lista a e ritorni il numero totale di numeri in a ed in tutte le sue sottoliste e la loro somma.
'''

def conta_int(a):
    s=0
    for i in range(len(a)-1): 
        if type(a[i]) in [int, float]:
            s+=a[i]
        elif type(a[i]) in [tuple, list]:
            s+=conta_int(a[i])
    return s


a = [1,[2,3,4,5,6,7,8,9,0],[1],[1,2,3,4]]

s = conta_int(a)
print(s)
