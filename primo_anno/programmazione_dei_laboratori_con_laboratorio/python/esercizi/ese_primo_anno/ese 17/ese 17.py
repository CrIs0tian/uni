import os

"""
(Riscaldamento) Si scriva una funzione che prenda in input una lista di
stringhe a e restituisca un dizionario
che abbia per chiavi le iniziali delle stringhe
in a e ad ogni chiave k associ come valore la lista di stringhe in a che cominciano con k.
"""


# in questo caso userò un comando non usato in quelle lezioni
# (acnhe perchè fare un ciclo dove controllo se la chiave esiste già o meno non me va)
# quindi usero il comando get che ha la seguente forma -----> var = dict.get(key, value),
# dove viene assegnato a var il valore corrispondente al valore associato alla chiave key,
# se key non ha valori o non è una chiave, viene assegnato a var il valore value (valore di default)
def list_to_dict(a):
    res = {}  # O(1)
    for i in a:  # O(n)
        res[i[0]] = res.get(i[0], [])  # O(1)
    for j in a:
        res[j[0]].append(j)  # O(1)
    return res


a = ["ciao", "ctodos", "civa", "a ", "ciola"]
print(list_to_dict(a))


"""
 Il docente ha raccolto in una cartella del pc dei file di testo con i risultati delle prove intermedie
 dell'esame di programmazione. Ogni file contiene l'esito di una prova e riporta su ogni riga l'email 
 dello studente ed il punteggio ottenuto (un intero tra 0 e 10). Il docente deve scrivere un programma 
 Python per raccolga tutti i risultati, in particolare vuole ottenere un dizionario che associ agli 
 indirizzi email degli studenti (le chiavi) la lista dei punteggi riportati nelle prove a cui ha partecipato. 
 Si progetti una funzione denominata analizza_test che prenda in input il nome della cartella contenente i file 
 di testo e restituisca il dizionario così come descritto sopra. Si assuma che i file contenenti i risultati abbiano 
 estensione csv, contengano una riga per ogni partecipante all'esame e le righe abbiano il formato:

   email_studente;voto

"""


# imponendo n = dimensione file da analizzare (numero di righe)
def analizza_test(dir):
    dict = {}
    for file in os.listdir(dir):
        # controllo che il file abbia come estensione csv, dato che potrebbero esserci file non idonei (tipo il codice stesso)
        if file.split(".")[-1] == "csv":
            print(file)
            dir_file = os.path.join(dir, file)
            f = open(dir_file)
            for row in f:
                k, v = row.split(";")
                v = int(v)
                # cosi posso fare un unpacking (simile a quello con le tuple)
                if k in dict:
                    dict[k].append(v)
                else:
                    dict[k] = [v]
            f.close()
    return dict


print(analizza_test(os.getcwd()))


"""
Modificare la precedente funzione in modo che il dizionario associ 
indirizzi email al voto finale derivante da tutte le prove a cui hanno 
partecipato gli studenti. Per il voto finale ogni prova intermedia 
contribuisce nel seguente modo: da 0 a 5 punti il contributo è 0, 
con 6 il contributo è 0.3, con 7 il contributo è 0.4, con 8
il contributo è 0.6,con 9 punti il contributo è 1 e con 10 punti il contributo è 1.5.
"""


# imponendo n = dimensione file da analizzare (il numero di righe)
def analizza_test2(dir):
    dict = {}  # O(1)
    grade = {6: 0.3, 7: 0.4, 8: 0.6, 9: 1, 10: 1.5}  # O(1)
    for file in os.listdir(dir):  # O(m) m = nume file da analizzare
        # controllo che il file abbia come estensione csv, dato che potrebbero esserci file non idonei (tipo il codice stesso)
        if file.split(".")[-1] == "csv":
            print(file)
            dir_file = os.path.join(dir, file)
            f = open(dir_file)
            for row in f:  # O(n)
                k, v = row.split(";")  # O(1)
                v = int(v)
                if v >= 0 and v <= 5:  # if else compreso = O(1)
                    val = 0
                else:
                    val = grade[v]
                # cosi posso fare un unpacking (simile a quello con le tuple)
                if k in dict:  # tutto O(1)
                    dict[k] += val
                else:
                    dict[k] = val
            f.close()
    return dict


print(analizza_test2(os.getcwd()))


"""analisi costo 
ese1 -----> caso pggiore = O(n)

ese2 -----> caso peggiore = O(n) per ese2 e ese3 costo per il singolo file da analizzare

ese3 -----> caso peggiore = O(n)
"""


"""continuo dell'esercizio 18, dove dobbiamo riprendere questi e usare il metodo get"""


# ese 1
def analizza_test3(dir):
    dict = {}
    for file in os.listdir(dir):
        # controllo che il file abbia come estensione csv, dato che potrebbero esserci file non idonei (tipo il codice stesso)
        if file.split(".")[-1] == "csv":
            print(file)
            dir_file = os.path.join(dir, file)
            f = open(dir_file)
            for row in f:
                k, v = row.split(";")
                v = int(v)
                a = dict.get(k, [])
                a.append(v)
                dict[k] = a
            f.close()
    return dict


print(analizza_test3(os.getcwd()))


# ese 2
def analizza_test4(dir):
    dict = {}  # O(1)
    grade = {6: 0.3, 7: 0.4, 8: 0.6, 9: 1, 10: 1.5}  # O(1)
    for file in os.listdir(dir):  # O(m) m = nume file da analizzare
        # controllo che il file abbia come estensione csv, dato che potrebbero esserci file non idonei (tipo il codice stesso)
        if file.split(".")[-1] == "csv":
            print(file)
            dir_file = os.path.join(dir, file)
            f = open(dir_file)
            for row in f:  # O(n)
                k, v = row.split(";")  # O(1)
                v = int(v)
                dict[k] = dict.get(k, 0) + grade.get(v, 0)
            f.close()
    return dict


print(analizza_test4(os.getcwd()))
