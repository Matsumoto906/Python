dic={'0':'零','1':'壹','2':'貳','3':'參','4':'肆',
'5':'伍','6':'陸','7':'柒','8':'捌','9':'玖',}
s=input()
l=len(s)
num=[]
k=9
for i in s:
    num.append((i)+'0'*k)
    k-=1
print(num)