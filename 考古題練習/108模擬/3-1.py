f=[0,1]
for i in range(2,10001):
    f.append(f[i-2]+f[i-1])
for i in range(int(input())):
    s=int(input())
    print(f[s])