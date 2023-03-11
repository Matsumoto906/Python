import numpy as np
g=[]
for t in range(int(input())):
    a,b,c,d=map(int,input().split(','))
    s1=np.array([[b,c],[1,1]])#等號左邊
    s2=np.array([d,a])#等號右邊
    ans=np.linalg.solve(s1,s2)#使用linalg、solve
    #print(int(ans[0]),int(ans[1]),sep=',')
    g.append(str(int(ans[0]))+','+str(int(ans[1])))
for i in g:
    print(i)