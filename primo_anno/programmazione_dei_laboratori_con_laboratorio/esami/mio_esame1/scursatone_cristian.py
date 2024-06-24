import math


def mode(a):
    d = {}
    l = []
    for i in a:
        d[i] = d.get(i, 0) + 1
    mass = max(d.values())
    for i in d.keys():
        if d[i] == mass:
            l.append(i)
    return l


a = [3, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3]
l = mode(a)
print(l)
# n = len(a)
# costo temporale = O(n+k), con k = d.keys(), ma nel caso peggiore è uguale a n, quindi O(n+O(n))= O(n)
# costo spaziale = O(k) con k = d.keys(), nel caso peggiore è n, quindi O(n) nel caso peggiore
