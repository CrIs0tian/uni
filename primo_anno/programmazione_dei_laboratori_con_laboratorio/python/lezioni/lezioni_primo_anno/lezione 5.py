#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 26 13:53:40 2022

@author: gianluca
"""

# In[]

import time as t
from math import cos, sin
import random  # moduli

x = "programmgrazione"
# y = 'gramma'
y = "gram"

p, trovato = 0, False
# modificato tenendo conto che possa aver successo...
while p <= len(x) - len(y) and not trovato:
    # verifico se y è in x a partire da p
    if y == x[p : p + len(y)]:
        trovato = True
        break  # esce dal ciclo più interno
    p += 1

if not trovato:
    print("non esiste corrispondenza")
else:
    print(y + " compare in posizione " + str(p) + " di " + x)

# In[] funzioni e moduli
# import modulo rnadom

# verifica con help se intervallo aperto o chiuso ( con numeri compresi tra 0 e 1 e non specificato)
print(random.random())
print(random.randint(2, 10))


print(cos(3.14), sin(3.14))


print(t.time())

# In[]  funzioni


def ricerca_sottostringa(x, y):  # parametri formali
    p, trovato = 0, False
    # modificato tenendo conto che possa aver successo...
    while p <= len(x) - len(y) and not trovato:
        # verifico se y è in x a partire da p
        if y == x[p : p + len(y)]:
            trovato = True
            break  # esce dal ciclo più interno
        p += 1

    if not trovato:
        print("non esiste corrispondenza")
    else:
        print(y + " compare in posizione " + str(p) + " di " + x)


a = "gra"
ricerca_sottostringa("programmazione", a)  # parametri attuali


ricerca_sottostringa("python", a)

# In[]


def ricerca_sottostringa(x, y):  # parametri formali
    p, trovato = 0, False
    # modificato tenendo conto che possa aver successo...
    while p <= len(x) - len(y) and not trovato:
        # verifico se y è in x a partire da p
        if y == x[p : p + len(y)]:
            trovato = True
            break  # esce dal ciclo più interno
        p += 1

    if not trovato:
        return -1
    else:
        return p


a = "gra"
t = ricerca_sottostringa("programmazione", a)

if t < 0:
    print("KO")
else:
    print("OK")

# In[]

"""
progettare una funzione che prende in input due interi a e b con b > a e restituisce

a*(a+1)*(a+2)*...*(b-1)*b
"""


def fattoriale_generalizzato(a, b):
    m, p = 1, a

    while p <= b:
        m *= p  # m = m*p
        p += 1

    return m


print(fattoriale_generalizzato(2, 6))

# In[] funzione range


def fattoriale_generalizzato(a, b):
    m = 1

    for p in range(a, b + 1):
        m *= p

    return m


print(fattoriale_generalizzato(2, 6))

# In[] varianti

for n in range(10):
    print(n)

for n in range(10, 20, 2):
    print(n)

for n in range(20, 10, -1):
    print(n)
