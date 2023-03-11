for j in range(0,int(input())):
    s=list(map(int,input().split()))
    s.sort()
    ans=[]
    s=s[::-1]
    for i in s:
        if i not in ans:
            ans.append(i)
    if len(ans)<2:
        print(ans[0],ans[0])
    else:
        print(ans[0],ans[1])