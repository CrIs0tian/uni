def stampa_vocali(s):
    for c in s : 
        if c in 'aeiouAEIOU' : print(c) 
    return 0 

s = input()
stampa_vocali(s)
