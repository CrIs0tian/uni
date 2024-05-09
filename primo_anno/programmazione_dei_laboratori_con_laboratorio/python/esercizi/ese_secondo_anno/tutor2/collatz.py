#definisci una funzione che dato un numero, 
#ne calcola la congettura di collatz, e ritorna il numero di passi che ha impiegato.
valido = False
n = int(input('inserisci un numero\n'))
while not valido: 
    if n <= 1: 
        print('numero non valido, riprova coglione\n')
        n=int(input('reinscerisci un numero\n'))
    else:
        valido = True
collatz_list= []
count = 0
while(n>1): 
    collatz_list.append(n)
    if (n%2==0):
        n = n//2
    else: 
        n = (n*3)+1
    count+=1
print('numero di passi = ', count)

