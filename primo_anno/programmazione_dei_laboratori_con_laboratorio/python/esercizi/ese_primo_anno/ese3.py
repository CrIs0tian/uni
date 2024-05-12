"""
Esercizio per casa: scrivere un programma che chieda all'utente di inserire due
stringhe xed y e stampi la posizione di x a partire dalla quale compare y;
nel caso in cui y non sia contenuto in x, stampi -1. Ad esempio, se

x = 'programmazione'
y = 'gramma'

il programma deve stampare 3.
"""


def subset(x, y):
    if len(y) > len(x):
        return -1
    else:
        i, j, sol = 0, 0, 0
        while i < len(x):
            sol = i
            while j < len(y) and (x[i] == y[j]):
                i += 1
                j += 1
            if j >= len(y):
                return sol
            else:
                i += 1
                j = 0
        return -1


x = "vivamammamamma"
y = "mamma"

sol = subset(x, y)
print(sol)

"""
esercizio della lezione 4: 
Esercizio per casa. Risolvere l'esercizio proposto nella lezione precedente utilizzando lo slicing.
"""


def subset_slicing(x, y):
    if len(x) < len(y):
        return -1
    else:
        i = 0
        while i < len(x) - len(y):
            if x[i : len(y) + i] == y:
                return i
            i += 1
        return -1


x = "programmazione"
y = "gramma"
res = subset_slicing(x, y)
print(y, " compare nella poszione ", res)
