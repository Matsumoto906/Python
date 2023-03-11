mo={'-----':0,'.----':1,'..---':2,'...--':3,'....-':4,'.....':5,'-....':6,'--...':7,'---..':8,'----.':9}
ans=''
for t in range(int(input())):
    s=input().split()
    for i in s:
        ans+=str(mo[i])
    ans+=' '
ans=ans.split()
for i in ans:
    print(i)