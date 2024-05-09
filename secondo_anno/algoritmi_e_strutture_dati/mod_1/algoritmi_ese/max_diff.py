def max_diff(a):
    i, j, diff = 0, len(a)-1, 0
    while (i<j):
        if ((a[j]-a[i])<0):
            i+=1
        else:
            if ( diff <= (a[j]-a[i])):
                diff = a[j]-a[i]
                res1 = i
                res2 = j
                
            j-=1
    return res1, res2

a = [2,11,20,5,4,2,9,10]
res1, res2 = max_diff(a)
print( res1, res2)
    