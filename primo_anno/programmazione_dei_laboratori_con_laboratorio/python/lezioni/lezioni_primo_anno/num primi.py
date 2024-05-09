n=input()
s=8
for i in range(7,1000,2):
    for z in range(3,i+1,2):
        if i%z==0 and z!=i:
            break
        elif i==z:
            s+=i
print(s)
        
