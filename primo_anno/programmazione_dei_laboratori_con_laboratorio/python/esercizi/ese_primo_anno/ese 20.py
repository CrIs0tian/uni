'''
Esercizio per casa

Si progetti ed implementi una funzione che prenda in input due liste 
di numeri ordinati in modo crescente e restituisca una nuova lista 
contenente tutti gli elementi delle liste in input ordinati dal più 
piccolo al più grande.
'''
#In[]
def sorted_list(l1,l2):
    l3=sorted(l1+l2)
    print(l3)
l1=[1,4,3,8,6]
l2=[9,3,5,6,2,4,5]
print(sorted_list(l1,l2))
# %%
