#In[]
#primo esercizio

'''n matematica, si definisce fattoriale di un numero naturale n, indicato con n!, il prodotto dei numeri interi positivi minori o uguali a tale numero

n!=∏nk=1k=1⋅2⋅3⋯(n−1)⋅n

Si progetti una algoritmo ricorsivo che calcoli il fattoriale di un numero
'''
def fattoriale(n):
    if n==0:
        return 1
    else:
        return n*fattoriale(n-1)

print(fattoriale(5))
#algoritmo iterativo 
def fattoriale_iter(n):
    k=n
    while k>1:
        k-=1
        n*=k
    return n
print(fattoriale_iter(5))

#In[]
#secondo esercizio: Hailstone sequence
'''E' una sequenza di interi positivi dove l'i+1-esimo numero è calcolato a partire dall'i-esimo, come segue:

    se i è pari -> dividi i per 2
    se i è dispari -> moltiplica i per 3 ed aggiungi 1

Si progetti una algoritmo ricorsivo che generi una sequenza come descritto sopra, restituendo una lista in output
'''

def hailstoneseq(n,l=[]):
    l.append(n)
    if n==1:
        print(l)
    elif n%2==0:
        hailstoneseq(n//2,l)
    else:
        hailstoneseq(3*n+1,l)

n=6
hailstoneseq(7)
        

# %%

#In[]
#probelma 3: frasi palindrome
'''Vogliamo scrivere un algoritmo ricorsivo che stabilisca se una data sequenza sia palindroma, ovvero se resta la stessa indipendentemente dal verso in cui viene letta.

'Anna','oro','asso' sono tutte sequenze palindrome ad esempio.
'''

def preProcessing(frase):
  #lista che contiene i segni che si vogliono eliminare dalla frase
  segni = [" ",",","'","."]
  print(f"frase in input:  {frase}")

  #metodo che permette di convertire una frase in minuscolo
  frase = frase.lower()
  print(f"conversione in minuscolo:  {frase}")

  #per ogni segno da eliminare, lo sostituisco con la stringa vuota "" tramite metodo replace
  for segno in segni:
    frase = frase.replace(segno,"")
  print(f"eliminazione spazi e segni punteggiatura:  {frase}")
  return frasePalindromaRic(frase,0,len(frase)-1)

def frasePalindromaRic(stringa,sx,dx):
    if sx>=dx:
        return True
    if stringa[sx]==stringa[dx]:
        return frasePalindromaRic(stringa,sx+1,dx-1)
    else:
        return False
    
print(preProcessing("O mordo tua nuora, o aro un autodromo."))
print("----------------------------------------------------------")

print(preProcessing("Eri un nano, non annuire."))
print("----------------------------------------------------------")

print(preProcessing("I topi non avevano nipoti."))
print("----------------------------------------------------------")

print(preProcessing("Ai lati d'italia."))
print("----------------------------------------------------------")

print(preProcessing("Anna di sera se c'e, Cesare si danna."))
print("----------------------------------------------------------")

print(preProcessing("Ala"))
print("----------------------------------------------------------")

print(preProcessing("ciao, sono uno studente di informatica"))
