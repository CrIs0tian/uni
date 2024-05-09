# In[]  
def count_int(list,i=0,c=0):
    if len(list)>i:
        if type(list[i])==int:
            return count_int(list,i+1,c+1)                
        else:
            return count_int(list,i+1,c)+count_int(list[i],i=0,c=0)    
    else:
        return c

print(count_int( [3, [9, [2,5], 2], 10, [8, [4,3], [1,2], 3,8]]))                
            
# %%
