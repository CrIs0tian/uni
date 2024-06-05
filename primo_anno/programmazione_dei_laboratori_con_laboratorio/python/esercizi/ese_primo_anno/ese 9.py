"""
1) Si progetti una funzione analoga a init_tuple per le liste.

2) Si progetti una funzione, denominata rem_none che prenda
   in input una lista ed elimini da questa tutti gli elementi
   a valore None.

"""

"""
prova--> operazioni con piu liste per vedere il comportamento dei puntatori 

"""

t1 = [1, 2, 3, 4]
t2 = [1233]
t3 = t1 + t2

print(t3)
t2[0] = 2
print(t3)

"""outuput= rimane uguale, quindi sembra che che con quella operazione vengano copiate le liste 
e vengono concatenati """


"""esercizio 1"""


def init_list(n, v=None):
    if v == None:
        return [0] * n
    else:
        l = []
        for i in range(n):
            l.append(v(i))
        return l


print(init_list(10))
print(init_list(10, v=lambda i: 2 * i + 1))
print(init_list(10, v=lambda i: "0" * i))
print(init_list(10, v=lambda i: [i] * 10))


"""esercizio 2"""


def rem_none(lis):
    i = 0
    while i < len(lis):
        if lis[i] == None:
            del lis[i]
        i += 1

    return lis


res = [1, 2, 3, 4, None, 3, 4, 5, None, 4, 5, 5, 6, 7]
print(rem_none(res))
