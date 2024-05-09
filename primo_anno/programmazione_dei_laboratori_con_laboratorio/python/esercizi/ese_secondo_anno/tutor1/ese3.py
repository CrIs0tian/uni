def voc_cons(s:str) ->tuple:
    voc=''
    cons=''
    for c in s: 
        if c in 'aeiouAEIOU':
            voc+=c
        elif c in 'bcdfghjklmnpqrstvwxyz0': 
            cons+=c
            
    return (voc, cons)

print(voc_cons('diomio'))
