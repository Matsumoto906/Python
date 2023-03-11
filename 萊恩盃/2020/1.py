a=int(input())
b=int(input())
for i in range(b):
    for j in range(1,a+1):
        print(str(j)*j)
    for j in range(a-1,0,-1):
        print(str(j)*j)
    if i != b-1:
        print()