s=input()
ans=0
for i in s:
    ans+=int(i)**len(s)
if ans==int(s):
    print(True)
else:
    print(False)