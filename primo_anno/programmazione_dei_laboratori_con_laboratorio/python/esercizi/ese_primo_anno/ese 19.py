'''
1.  Trasformare il codice dell'algoritmo Bubble Sort in una funzione denominata bubble_sort
    che prenda in input una lista di numeri e la muti ordinandoli in modo crescente.

2.  Sia n la lunghezza della lista in input, calcolare la complessità computazione 
    della funzione bubble_sort distinguendo il caso peggiore ed il caso migliore.

3.  Modificare la funzione bubble_sort in modo da soddisfare la seguente specifica
    def bubble_sort(a, inplace=True):
        
        Input:  a, una lista di str; inplace un bool
        Output: ordina le stringhe in a dalla più corta alla più lunga, ritorna la lista ordinata.
	    Se inplace è True la funzione muta a, altrimenti viene restituita una nuova lista
	    con le stringhe di a ordinate come richiesto
'''
#In[]
def bubble_sort(num):
    a=len(num)
    for i in range(a-1):
        y=0
        while y<a-1-i:
            if num[y]>num[y+1]:
                num[y], num[y+1]=num[y+1],num [y]
            y+=1
    return num
list=[8,6,7,14,5,9,0,4]
print(bubble_sort(list))
#caso migliore O(n) --->poiche comunque entra nel ciclo for facendo n operzioni costanti 
#caso peggiore O(n**2)

#In[]
def bubble_sort(a, inplace=True):
    l=len(a)
    for i in range(l-1):
        y=0
        while y<l-1-i:  
            if len(a[y])>len(a[y+1]):
                a[y],a[y+1]=a[y+1],a[y]
            y+=1
    if inplace==True:
        return a
    else:
        b=a[:]
        return b
    
lis=['ciao','a','to']
print(bubble_sort(lis,False))

