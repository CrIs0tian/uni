# -*- coding: utf-8 -*-

# Esercizio per casa. Scrivere una funzione che prende in input due stringhe 
# e restituisce il carattere della prima stringa che compare 
# più volte nella seconda.Ad esempio se la prima stringa è 
# ciao e la seconda è ramarro marrone, 
# la funzione deve restituire a.

def massime_intersezioni(a,b):
    n_max , c_max = 0 , 0
    for i in a:
        c_max = 0
        for j in b:
            
            if (i == j):
                c_max+=1
        if (c_max > n_max):
            n_max, res = c_max, i
    if (n_max == 0):
        print('le due stringhe non hanno caratteri in comune')
    else:
        print(f'il carattere nella stringa \'{a}\' contenuta di più in \'{b}\' è \'{res}\'')

a , b = 'ciao', 'ramarro marrone'
print(massime_intersezioni(a,b))
        
                
    