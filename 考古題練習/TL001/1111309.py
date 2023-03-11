z={
    '10#':'j','11#':'k','12#':'l','13#':'m',
    '14#':'n','15#':'o','16#':'p','17#':'q',
    '18#':'r','19#':'s','20#':'t','21#':'u',
    '22#':'v','23#':'w','24#':'x','25#':'y','26#':'z'}
a={
    '1':'a','2':'b','3':'c','4':'d',
    '5':'e','6':'f','7':'g','8':'h','9':'i'}
ans=''
s=input()
for i in range(0,len(s)):
    if s[i]=='#':
        if s[i-2:i+1] in z:
            ans=ans.replace(ans[-1],'',1)
            ans=ans.replace(ans[-1],'',1)
            ans+=z[s[i-2:i+1]]
    else:
        if s[i]=='0':
            ans+='a'
        else:
            ans+=a[s[i]]
print(ans)