import os

"""
primo esercizio: 

	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le 
    righe del file in cui compare k  
"""


def find_in_file(filename, k):
    f = open(filename)
    row = 0
    sol = ()
    for r in f:  # O(n)
        if k in r:  # O(1) assunti che la riga abbia lunghezza costante
            sol += (row,)  # O(len(sol)+1)
            row += 1
    f.close()
    return sol


print(find_in_file("esempio.txt", "d"))

"""
costo computazionale in 2 casi (assunto che n=num righe del file)

primo caso: con lunghezza riga e k costanti: caso peggiore --> n volte facciamo 
            sol+=(row,) quindi 1+2+3+4+.....+n = ((n+1)*n) / 2 = O(n^2)

secondo caso (k = cost, len(r) = O(m)): O(n^2*m), ad ogni passo k in r = O(m)---> ricerca lineare
"""


"""
secondo esercizio 
    
    Modificare la funzione in modo che la nuova specifica sia

    Input: filename e k sono str, filename è il nome di un file
	Output: una tupla ( (r0, c0), (r1, c1), ...) di coppie di interi che indicano le
		righe e le colonne del file in cui compare k. Per colonna si intende la posizione
		all'interno della riga
"""


def find_in_file2(filename, k):
    # costo computazionale
    f = open(filename)  # O(1) ovvero costo costante
    lines = []  # O(1)
    r = 1  # riga corrente
    for line in f:  # eseguito O(n)
        for c in range(len(line) - len(k) + 1):  # costa O(len(line)-len(k)) sempre
            if (
                k == line[c : c + len(k)]
            ):  # len(line)-len(k)[uguale a c]+len(k) ultimo punto che ci può controllare
                lines.append((r, c))  # O(1)
        r += 1
    f.close()  # O(1)
    return tuple(lines)  # cosi rispettiamo le regole dell'output, ma a costo O(n)


t = find_in_file2("esempio.txt", "d")
print(t)
