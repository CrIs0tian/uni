# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:59:35 2023

@author: Gianluca
"""

# input
N = ['B', 'A', 'D', 'F', 'E', 'C']
P = [2, 0, 6, 9, 7, 3]

# output, lista dei centri di N

n = len(N)

# calcoliamo l'eccentricità, lista E con E[i] = eccentricità di P[i] 
# ( distanza, tra uno dei due estremi dell retta, 
# quindi estremo sinistro e destro hanno eccentricità massima)
#

E  = []  # O(1)

for x in P:
    ecc_x = 0
    for y in P:
        if abs(x-y) > ecc_x: # abs, valore assoluto
            ecc_x = abs(x-y)
    E.append(ecc_x) # O(1) nel 'caso medio', quando non raggiunge la capacità, se raggiunta (caso peggiore), riscrive il tutto in una altra parte e fa append---> O(n)+O(1) = O(n)
    
# ^ Theta(n*n) ^
    
print (E)
C = [] # i nomi dei punti centrali di P, costo O(1)

m = None
# in C tengo i punti con eccentricità pari ad m

i = 0
while i < len(E):
    e = E[i] # O(1)
    if e == m: 
        C.append(N[i]) 
    elif m == None or e < m:
        m = e
        C = [ N[i] ] # O(1) nel caso peggiore
    i += 1

print (N)
# ^ Theta(n)
    
 
# Complessità temporale è Theta(n*n)
# Complessità spaziale è Theta(n) ovvero la dimensione di E
