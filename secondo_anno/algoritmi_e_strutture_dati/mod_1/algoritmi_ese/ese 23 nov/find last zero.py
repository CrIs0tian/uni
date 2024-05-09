def recursive_last_zero(A:list, i:int, j:int) -> int:
    if i > j: 
        return -1
    m = (i+j)//2
    if A[m]== 0 and A[m+1]==1:
        return m 
    if A[m] == 1:
        return recursive_last_zero(A, i, m-1 )
    else: 
        return recursive_last_zero(A, m+1, j)

def las_zero(A):
    n=len(A)
    if A[n-1]==0: 
        return -1
    else:
        return 

