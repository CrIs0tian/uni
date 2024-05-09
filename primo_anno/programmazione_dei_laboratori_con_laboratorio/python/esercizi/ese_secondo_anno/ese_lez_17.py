def bin_search(a, k):
    '''
    Parameters
    ----------
    a : una lista ordinata
    k : una chiave di ricerca

    Returns
    -------
    la posizione del primo elemento più grande di k
    
    ovvero
    
    0 se k < a[0]
    n se k >= a[n-1]
    
    a[p] > k e a[p-1] <= k
    '''
    lx, rx = 0, len(a)

    if (k < a[0]): 
        return 0
    if (k >= a[rx-1]):
        return rx
    while lx<rx: 
        cx = (lx+rx)//2
        if (a[cx] > k and a[cx-1] <= k): 
            return cx
        if (a[cx]<k): 
            lx=cx+1 
        else: 
            rx=cx

a = [2,4, 6, 7, 7, 10, 10, 10, 10, 14, 16, 17, 20, 24 , 25 ]

print(bin_search(a, 23))




