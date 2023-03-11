for t in range(int(input())):
    a,b=map(str,input().split('/'))
    a=a.split('.')

    num1=[]
    num2=[]
    not_num2=[]
    and_num=[]
    or_num=[]
    ans=''

    for i in a:
        k=str(bin(int(i)))[2:]
        k=k.zfill(8)
        num1.append(k)
    k=''
    for i in range(1,33):
        if i <=int(b):
            k+='1'
        else:
            k+='0'
        if i%8==0:
            k+='.'
    k=k.strip(k[-1])
    num2=k.split('.')


    k=''
    for i in range(0,4):
        for j in range(0,8):
            if num2[i][j]=='1':
                k+='0'
            else:
                k+='1'
        k+='.' 
    k=k.strip(k[-1]) 
    not_num2=k.split('.')
    
    k=''
    for i in range(0,4):
        for j in range(0,8):
            if num1[i][j]=='1' and num2[i][j]=='1':
                k+='1'
            else:
                k+='0'
        k+='.'
    k=k.strip(k[-1])
    and_num=k.split('.')

  

    k=''
    for i in range(0,4):
        for j in range(0,8):
            if not_num2[i][j]=='1' or num1[i][j]=='1':
                k += '1'
            else:
                k+='0'
        k+='.'
    or_num=k.split('.')
    
    for i in and_num:
        i='0b'+i
        if i =='0b':
            break
        ans+=str(int(i,2))+'.'

    ans=ans.strip(ans[-1])
    ans+='/'
    
    for i in or_num:
        i='0b'+i
        if i =='0b':
            break
        ans+=str(int(i,2))+'.'

    ans=ans.strip(ans[-1])

    print(ans)