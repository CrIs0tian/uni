#In[]
#(Riscaldamento) Si scriva una funzione che prenda in input una lista di stringhe a e restituisca un dizionario 
#che abbia per chiavi le iniziali delle stringhe in a e ad ogni chiave k associ come valore la lista di stringhe in a che cominciano con k.
def diz_stringhe(a):
    diz={}
    for x in a:
        if x=='':
            continue
        p=x[0]
        if p in diz: #controlla se p è una chiave nel dizionario
            diz[p].append(x)
        else:
            diz[p]=[x]
    return diz
a = ['python', 'for', 'codice', 'programma', '', 'input', 'while', 'for', 'in']
d = diz_stringhe(a)
print(d)
#In[]
import os
'''
 Il docente ha raccolto in una cartella del pc dei file di testo con i risultati delle prove intermedie
 dell'esame di programmazione. Ogni file contiene l'esito di una prova e riporta su ogni riga l'email 
 dello studente ed il punteggio ottenuto (un intero tra 0 e 10). Il docente deve scrivere un programma 
 Python per raccolga tutti i risultati, in particolare vuole ottenere un dizionario che associ agli 
 indirizzi email degli studenti (le chiavi) la lista dei punteggi riportati nelle prove a cui ha partecipato. 
 Si progetti una funzione denominata analizza_test che prenda in input il nome della cartella contenente i file 
 di testo e restituisca il dizionario così come descritto sopra. Si assuma che i file contenenti i risultati abbiano 
 estensione csv, contengano una riga per ogni partecipante all'esame e le righe abbiano il formato:

   email_studente;voto

'''
def  analizza_test(path):
    diz={}
    for x in os.listdir(path):
        if x.split('.')[-1]=='csv':
            full_path=os.path.join(path, x)
            f=open(full_path)
            for y in f:
                key,vote=y.split(';')
                vote=int(vote) #cosi togli elemnti indesiderati, in questo caso \n
                if key in diz:
                    diz[key].append(vote)    
                else:
                    diz[key]=[vote]
            f.close()
    return diz
a=analizza_test(os.getcwd()) 
print(a) 
print(os.getcwd())
#In[]
'''
Modificare la precedente funzione in modo che il dizionario associ 
indirizzi email al voto finale derivante da tutte le prove a cui hanno 
partecipato gli studenti. Per il voto finale ogni prova intermedia 
contribuisce nel seguente modo: da 0 a 5 punti il contributo è 0, 
con 6 il contributo è 0.3, con 7 il contributo è 0.4, con 8
il contributo è 0.6,con 9 punti il contributo è 1 e con 10 punti il contributo è 1.5.
'''
def  analizza_test(path):
    value_diz={6:0.3, 7:0.4, 8:0.6, 9:1, 10:1.5}
    diz={}
    for x in os.listdir(path):
        if x.split('.')[-1]=='csv':
            full_path=os.path.join(path, x)
            f=open(full_path)
            for y in f:
                key,vote=y.split(';')
                vote=int(vote) #cosi togli elementi indesiderati, in questo caso \n
                diz[key]=diz.get(key,0)+value_diz.get(vote,0) # cosi se hanno un voto minore di 5 (nel value_diz), crea una nuova chiave con valore zero 
                
            f.close()
    return diz
a=analizza_test(os.getcwd()) 
print(a) 


# %%
