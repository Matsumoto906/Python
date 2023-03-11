n=int(input())
key=0
for i in range(2,n):
    if n%i==0:
        key="Y"
        break   
    else:
        print(i)
        key="N"
print(key)