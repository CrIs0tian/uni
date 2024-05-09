#1. Modificare browse_dir nel seguente modo: aggiungere un 
#   secondo parametro ext opzionale 
#   di tipo str che, se specificato, stampi solo i 
#   file che hanno per estensione ext.
#   Se non indicato, la funzione si comporti nel modo originale.

#2. Modificare la precedente funzione in modo tale che, invece di stampare
# i nomi dei file,
# li ritorni in una lista.
#In[]
import os

def browse_dir(dir, ext=''):
    folder=os.listdir(dir)
    for x in folder:
        full_dir=os.path.join(dir, x)
        if os.path.isfile(full_dir) and ext in x:
            print(f'FILE:{full_dir}')
        elif os.path.isdir(full_dir):
            browse_dir(full_dir,ext)
            
browse_dir(os.getcwd(),'csv')       
#In[]
import os

def browse_dir(dir, ext='',lista=[]):
    folder=os.listdir(dir)
    for x in folder:
        full_dir=os.path.join(dir, x)
        if os.path.isfile(full_dir) and ext in x:
            lista.append(x)
        elif os.path.isdir(full_dir):
            browse_dir(full_dir,ext,lista)
            
lista=[]
browse_dir(os.getcwd(),'py',lista)
print(lista)


# %%
