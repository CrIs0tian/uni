"""
Si progetti una funzione, denominata count_int che prenda in input
una lista che può contenere liste annidate e restituisca
il numero di interi nella lista e in tutte le sottoliste
annidate che questa contiene.
Ad esempio count_int( [3, [9, [2,5], 2], 10, [8, [4,3], [1,2], 3]] )
dovrebbe restituire 12.
"""


def count_int(l):
    res = 0
    for i in l:
        if type(i) == list:
            res += count_int(i)
        else:
            res += 1
    return res


print(count_int([]))
