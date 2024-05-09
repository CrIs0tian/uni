#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:31:14 2022

@author: gianluca
"""

# In[] esercizio: contare il numero di vocali nella stringa x

x = input('Digita una stringa: ')

numero_vocali = 0
p = 0

while p < len(x):
    # verifico se x[p] è una vocale minuscola
    if x[p] in 'aeiouAEIOU':
        numero_vocali += 1
        # oppure numero_vocali += 1
    p += 1 # equivalente a p = p+1
    
print('Il numero di vocali in '+x+' è '+str(numero_vocali)) # il + per mantenere gli apici '

# In[] esercizio: contare il numero di vocali nella stringa x nelle posizioni pari

x = input('Digita una stringa: ')

numero_vocali = 0
p = 0

while p < len(x):
    
    if p % 2 == 0: # oppure p % 2 != 1    
        if x[p] in 'aeiouAEIOU':
            numero_vocali = numero_vocali+1
            # oppure numero_vocali += 1
    p += 1 # equivalente a p = p+1
    
print('Il numero di vocali nelle posizioni pari di '+x+' è '+str(numero_vocali))

# In[] Operatori booleani

c0, c1 = True, False
print(c0 or c1)
print(not c1)
print(c0 and not c1)


# In[] Operatori relazionali

print(4 <= 5) # minore uguale >=
print(4 != 90)


# In[] sottolineare vocali

x = input('Digita una stringa: ')
sottolineatura = ''

p = 0
while p < len(x):
    # verifico se x[p] è una vocale
    if x[p] in 'aeiouAEIOU':
        sottolineatura += '*'
    else:
        sottolineatura += ' '
    p += 1 # equivalente a p = p+1
    
print(x)
print(sottolineatura)

# In[] istruzione for

x = input('Digita una stringa: ')
sottolineatura = ''

for c in x:
    # verifico se c è una vocale
    if c in 'aeiouAEIOU':
        sottolineatura += '*'
    else:
        sottolineatura += ' '
    
print(x)
print(sottolineatura)
    
# In[]

a = 'programmazione'
a[2] = '*' # NO, le stringhe sono immutabili

    