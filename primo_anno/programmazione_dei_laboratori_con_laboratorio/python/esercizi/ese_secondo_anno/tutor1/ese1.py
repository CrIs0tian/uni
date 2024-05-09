s= str(input('inserire stringa '))
i = 0
while (i<len(s)):
    if (s[i] in 'aeiouAEIOU'):
        print(s[i])
    i+=1
    
#oppure possiamo fare cosi, più pulito 

s = input('inserire stringa')
for c in s: 
    if c in 'aeiouAEIOU' : print(c) 
