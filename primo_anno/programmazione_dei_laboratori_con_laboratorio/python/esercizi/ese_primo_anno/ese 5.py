# -*- coding: utf-8 -*-

# Esercizio per casa. Scrivere una funzione che prende in input due stringhe
# e restituisce il carattere della prima stringa che compare
# più volte nella seconda.Ad esempio se la prima stringa è
# ciao e la seconda è ramarro marrone,
# la funzione deve restituire a.


# una possibile implementazione potrebbe essere questa
def massime_intersezioni(a, b):
    n_max, c_max = 0, 0
    for i in a:
        c_max = 0
        for j in b:
            if i == j:
                c_max += 1
        if c_max > n_max:
            n_max, res = c_max, i
    if n_max == 0:
        print("le due stringhe non hanno caratteri in comune")
    else:
        print(f"il carattere nella stringa '{a}' contenuta di più in '{b}' è '{res}'")


a, b = "ciao", "ramarro marrone"
print(massime_intersezioni(a, b))
"""costo non molto buono---> O(n*m) con n=len(a), m=len(b)
un'altra possibile implementazione, usando il dizionario
"""


def Dict_max_intersect(a, b):
    dict_b = {}
    for i in b:
        dict_b[i] = dict_b.get(i, 0) + 1
    max = 0
    for j in a:
        if j in dict_b:
            if dict_b[j] > max:
                max = dict_b[j]
                ris = j
    return ris


a, b = "ciao", "ramarro marrone"
res = Dict_max_intersect(a, b)
print("\n", res)

"""non migliora molto ma almeno sicuro non fa per forza n*m iterazioni, ma comunque il costo rimane O(nm)"""
