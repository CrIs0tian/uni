'''
a=[1,2,3,4,5]
b=a

a[1]=10
print("questo è l'array b: ",b)

#cosa stampa print("questo è l'array b",b)
#stampa [1,10,3,4,5]
'''


n=0
def funzione (n):
    n+=1
    return n 
print(funzione(n))
print(n)




tupla=(1,2,3,4)
tupla2=tupla

def funzione2(tup):
	tup+=(5,6)
	return tup

print(funzione2(tupla))
print(tupla)
print(tupla2)



lista = [0,1]
lista2= lista

def funzione3(lis):
    lis.append(0)
    return lis 

print(funzione3(lista[:]))
print(lista)
print(lista2)

'''
cosa ho imparato? che le liste ,essedno mutabili (include quindi anche i dizionari),
quando usati ome argomenti per funzion i, i parametri comunque 'punteranno' alla stessa variabile, e le loro modifiche quindi si noteranno chimanado la varibalie con un altro nome, 
questa coa non funziona però con le variabili immutabili (int, float, str, tuple) dato che esse, se modificate attraverso una funzione questa non cambia il risultato della variabile globale ù
a meno che il valore di ritorno non venga assegnato alla variabile
'''


#scrivi una funzione che sostituisce ad ogni elemento di lista la parola "ciao" SENZA MODIFICARE LA LISTA!!!
lista3=[1,3,8,2]

def mod_list(lis):
    list_copy=lis[:]
    for i in range(len(list_copy)):
        list_copy[i]='suca'
    return list_copy

print(mod_list(lista3))
print(lista3)



