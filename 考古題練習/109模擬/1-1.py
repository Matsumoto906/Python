num=[2,3]
def f(x):
    key=True
    for i in num:
        if x%i==0:
            key=False
            break
    return key
for i in range(4,10001):
    if f(i)==True:
        num.append(i)

for t in range(int(input())):
    s=int(input())
    for i in range(0,len(num)):
        if num[i]>=s:
            print(num[i-1])
            break