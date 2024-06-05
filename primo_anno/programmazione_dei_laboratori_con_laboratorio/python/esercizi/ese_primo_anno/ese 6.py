"""Esercizio per casa. Scrivere una funzione che riceva in input un intero n e
restituisca un float (pseudo)-casuale compreso tra 0 ed 1 composto da n
    cifre decimali significative dopo la virgola."""

import random as rn


def pseudo_float(n):
    res = "0."
    for c in range(n - 1):
        res += str(rn.randint(0, 9))
    res += str(rn.randint(1, 9))
    float(res)
    return res


n = pseudo_float(20)
print(n)
