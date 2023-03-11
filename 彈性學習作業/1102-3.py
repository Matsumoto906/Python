import time
import random
time.sleep(3)
num=[]
while len(num)!=6:
    k=(random.randrange(1,49))
    if k not in num:
        num.append(k)
for i in range(0,6):
    print('第 ',i,' 個號碼 : ',num[i],sep='')
print('特別號 : ',random.randrange(1,49))