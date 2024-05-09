#In[]
def conta_somme_consecutive(a):
    c = 0
    for x, y, z in zip(a[:-2], a[1:-1], a[2:]): #che zippa? in x tutti gli elementi tranne gli ultimi due, 
                                                #y gli elementi tranne il primo e l'ultimo, mentre z tutti tranne i primi due 
        if z == x+y:
            c += 1
            
    return c

a = [5,3,8,6,14]

print( conta_somme_consecutive(a) )