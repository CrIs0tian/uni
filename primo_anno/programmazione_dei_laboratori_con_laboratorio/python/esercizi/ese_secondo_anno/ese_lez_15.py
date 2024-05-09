 # In[ESERCIZIO]

a = [1,[2,3,4,5,6,7,8,9,0],[1],[1,2,3,4]]
    



# Data una lista a,
# scrivere una funzione che ritorni il numero di
# interi contenuti in a ed in tutte le sue liste
# annidate


def deep_count(lis):
     c = 0
     i=0 
     while i<len(lis): 
         if type(lis[i])==list: 
             c = c + deep_count(lis[i])
         else: 
             c+=1
         i+=1
     return c

count = deep_count(a)
print(count)
