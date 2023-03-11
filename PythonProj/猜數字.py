import random

x=random.randint(0,1000)
num=int(input('請輸入數字:'))
while num!=x:
    if num>x:
        num=int(input('太大了 請重新輸入:'))
        
    if num<x:
        num=int(input('太小了 請重新輸入:'))
        
if num==x:
    print('猜對了 答案是',x)