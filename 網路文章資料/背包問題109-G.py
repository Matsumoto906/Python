num=[]
while True:
    try:
        x=input()
        if len(x.strip())==0:
            break
        num.append(list(map(int,x.split())))
    except:
        pass
for i in range(0,len(num)):
    dp=[0]*(num[i][0]+1)
    for j in range(num[i][1]):
        for k in range(num[i][0],num[i][j+2]-1,-1):
            if dp[k] < (dp[k-num[i][j+2]]+num[i][j+2]):
                dp[k] = (dp[k-num[i][j+2]]+num[i][j+2])
    print(dp[num[i][0]])