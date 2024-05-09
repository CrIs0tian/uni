#soluzione esercizio 13
#In[]
import os 

def Browse_dir(d,ext=None): #va bene anche ext=stringa vuota
    
    #input: d è il nome di una cartella (un str), ext è una str che indica un tipo di estensione
    #di un file
    #output: stampa tutti i file in d e in tutte le sue sottocartelle che terminano in .ext
    #se ext=none, stampa tuti i file
    cartella=os.listdir(d)
    
    for x in cartella:
        full_path=os.path.join(d,x)
        if os.path.isfile(full_path):
            if ext==None or x.split('.')[-1]==ext:
                print(f'FILE:{full_path}')
        elif os.path.isdir(full_path):
            Browse_dir(full_path, ext)
Browse_dir(os.getcwd(),ext=None)     

# per l'esercizio si usa una funzione per le stringhe str.split()
#dove dalla stringa viene creata una lista con elementi la stringa divisa usando un parametro

#In[]
#esercizio con la lista 
def Browse_dir(d,ext=None):#va bene anche ext=stringa vuota
    
    #input: d è il nome di una cartella (un str), ext è una str che indica un tipo di estensione
    #di un file
    #output: stampa tutti i file in d e in tutte le sue sottocartelle che terminano in .ext
    #se ext=none, stampa tuti i file, tutti slavati in una lista
    b=[]
    cartella=os.listdir(d)
    
    for x in cartella:
        full_path=os.path.join(d,x)
        if os.path.isfile(full_path):
            if ext==None or x.split('.')[-1]==ext:
                b.append(full_path)
        elif os.path.isdir(full_path):
            c = Browse_dir(full_path, ext)
            b.extend(c)  #uguale for x in c:
                        #b.append(x) 
    return b
d = Browse_dir(os.getcwd(),ext=None)  
print(d)


#In[]
import os
a=os.getcwd()
f=open('esempio.txt')
for line in f:
    print(line)
    
f.close() 
#In[]
#prendiamo lo stesso esercizio ma utilizziamo la funzione open 
def Browse_dir(d,txt):
    b=[]
    cartella=os.listdir(d)
    
    for x in cartella:
        full_path=os.path.join(d,x)
        if os.path.isfile(full_path) and full_path.split('.')[-1]=='py':
            f=open(full_path)
            for line in f:
                if txt in line:
                    b.append(full_path)
                    break
            f.close()
        elif os.path.isdir(full_path):
            c= Browse_dir(full_path, txt=txt)
            b.extend(c)  #uguale for x in c:
                                            #b.append(x) 
        return b
b=Browse_dir(os.getcwd(),'len')
print(b)  

#In[]
#esempio di uso funzioni open, close etc.
f=open('esempio.txt','w')    # w sta per la modalità, in questo caso di write , cioè di scrittura e sostituisce il file prima
f.write('oh my god wowowow\n')   #nel file txt esempio scrive la frase 'oh my god'. l'a capo funziona anche interagendo con file esterni
f.write('SBORRO')
f.close()# chiude il file e lo salva, sostituendo il contenuto scritto in precedenza
f=open('esempio.txt','a')  # con a impostato si puo scrivere(write) ma la prima riga è 'appesa' al'ultima linea utilizzata senza sostituire il file  
f.write('oh my god\n')   
f.write('SBORRO')
f.close()
# %%
