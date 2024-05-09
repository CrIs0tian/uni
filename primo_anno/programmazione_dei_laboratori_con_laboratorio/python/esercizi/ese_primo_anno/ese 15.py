import os
'''
	Input: filename e k sono str, filename è il nome di un file
	Output: una tupla (r0, r1, ...) di interi che indicano le 
    righe del file in cui compare k  
'''

def find_in_file(filename, k):
    res = ()
    f = open(filename)
    r = 1
    for i in f:
        if k in i:
            res+=(r,)
        r+=1
    f.close()
    return res
    

t= find_in_file('esempio.txt', 'dio')
print(t)
            
    
    
