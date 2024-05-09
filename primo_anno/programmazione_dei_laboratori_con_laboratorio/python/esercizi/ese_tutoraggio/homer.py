'''
Homer è al bar e, come di consueto, ha voglia di fiumi di birra!

Dunque, il suo obiettivo, è di bere il più possibile.

Sapendo che ha a disposizione d dollari, sapendo che una birra 
costa p e che per ogni k bottiglie vuote resistuite al barista ne riceverà 
una extra in omaggio, progettare un algoritmo ricorsivo che calcoli quante birre 
potrà bere al massimo Homer.
'''
'''
Dati i seguenti tre valori, il task è trovare il numero massimo di birre che Homer può bere!

d: dollari posseduti da Homer

p: prezzo di una birra

k: numero di bottiglie vuote da resituire al barista per ottenere una birra extra

Più formalmente:

    Sia 𝚷 il problema appena descritto,

    siano 𝒅,𝐩 float,

    sia 𝐤 int ,

    con 𝐩>0 e 𝐤>=2,

    trovare un algoritmo 𝚨 ricorsivo che computi int 𝐱, tale che 𝐱 sia massimo per 𝚷.

Hint1: ovviamente Homer,ricorsivamente,restituisce le bottigle vuote e ottiene nuove birre da scolarsi (ottiene una birra extra per ogni k restituite)

Hint2: impostare la soluzione definendo due funzioni:

def contaBirreMax(d,p,k)

e

def contaBirreRic(p,k)

dove la prima funzione calcola le birre acquistabili e invoca la seconda; quest'ultima calcola le birre extra ottenibili tramite scambio invocando se stessa in maniera ricorsiva.
Esempio

Input: d = 15.0, p = 1.0, k = 3

Output: 22

Homer compra e beve 15 birre.

Rende 15 bottiglie e ottiene e beve 5 birre extra.

Rende 3 bottiglie, ottiene 1 birra extra, la beve(tiene le altre 2 bottiglie).

Ora ha 3 bottiglie. Le rende tutte e 3 e ottiene e beve 1 birra extra.

totale = 15 + 5 + 1 + 1 = 22

'''
def countBeerRic(n,k):
    if (n//k)<1:
        return 0
    else:
        c=n//k
        x=n//k+n%k
        return c+countBeerRic(x,k)
        
def countMaxBeer(d,p,k):
    BeerPurch=d//p
    MaxBeer=BeerPurch+countBeerRic(BeerPurch,k)
    return MaxBeer
print(countMaxBeer(20,1.80,3)) 


#algoritmo più efficiente (in termini di spazio)
def maxBeer(d,p,k):
    maxBeer = d//p
    c=maxBeer
    while c>=k:
        n = c//k
        maxBeer = maxBeer + n
        c = n+c%k
    return maxBeer
print(maxBeer(15,1,3))
    