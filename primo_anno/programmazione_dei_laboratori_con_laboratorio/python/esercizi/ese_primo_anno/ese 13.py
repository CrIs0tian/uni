import os

"""
1. Modificare browse_dir nel seguente modo: aggiungere un 
   secondo parametro ext opzionale 
   di tipo str che, se specificato, stampi solo i 
   file che hanno per estensione ext.
   Se non indicato, la funzione si comporti nel modo originale.


2. Modificare la precedente funzione in modo tale che, invece di stampare
 i nomi dei file,
 li ritorni in una lista.

"""


#esercizio 1 

def browse_dir(d, ext = None):
    cartella = os.listdir(d)

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path):
            if ext == None or full_path.split('.')[-1] == ext
            print(f"FILE: {full_path}")
        elif os.path.isdir(full_path):
            browse_dir(full_path)


#esercizio 2

def browse_dir(d, ext = None):
    cartella = os.listdir(d)

    l = []

    for x in cartella:
        full_path = os.path.join(d, x)
        if os.path.isfile(full_path):
            if ext == None or full_path.split('.')[-1] == ext:
                l.append(full_path)
        elif os.path.isdir(full_path):
            c = browse_dir(full_path)
            l.extend(c)  
        return l








