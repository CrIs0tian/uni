
def insertion_sort(l):
    for k in range(1, len(l)):
        i=k
        while l[i]<l[i-1] and i!=0 :
            l[i] , l[i-1] = l[i-1], l[i]
            i-=1
    print (l)
    
def bubble_sort(l):
    k=0
    while len(l)-1>k:
        i=1 
        for i in range(1, len(l)-k):
            if l[i]<l[i-1]:
                l[i], l[i-1] = l[i-1], l[i]
        k+=1
    print(l)
l=[9,4,5,6,7,8,3,2,1,0]
insertion_sort(l)
bubble_sort(l)
