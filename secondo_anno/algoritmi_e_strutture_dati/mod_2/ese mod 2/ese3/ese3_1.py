#implementazione del primo problema dell'esercitazione 3 

def opt1(s : str)-> int: 
    n = len(s)
    M = [[0] * n for _ in range (n)] #faccio una lista di 0 lunga n e lo faccio per n volte
    for i in range (n): 
        M[i][i] = 1
    for d in range(1,n):  #mi permette di scorrere la diagonale, considera le righe della diagonale d scorrono da 0 fino a n-1-d se indicizziamo a 0, n-d se indicizziamo a 1
        for i in range(n-d):
            j = i+d

            if s[i]==s[j]: 
                M[i][j] = 2 + M[i+1][j-1]
            else: 
                M[i][j] = max(M[i+1][j], M[i][j-1])
    return M[0][n-1]
print(opt1('algoritmo'))
#opt usando la memoization
def memoization(s:str, i:int , j:int, cache : dict = dict()): 
    if (i,j) in cache:
        return cache[i,j]
    if i>j: 
        cache [i,j] = 0
    elif i == j:
        cache[i,j] = 1 
    else: 
        if s[i] == s[j]: 
            cache[i,j] = 2 +memoization(s, i+1 , j-1, cache)
        else: 
            cache[i,j] = max(memoization(s, i, j-1, cache), memoization(s, i+1, j, cache))
    return cache[i,j]

    
