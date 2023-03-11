z=['a','e','i','o','u']
s=input().lower()
l=len(s)
a=0
b=0
for i in range(0,l//2):
    if s[i] in z:
        a+=1
for i in range(l//2,l):
    if s[i] in z:
        b+=1
if a==b:
    print(True)
else:
    print(False)