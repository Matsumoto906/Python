def nroot(x,y):
    return pow(x,1/y)

a=int(input('請輸入被開方數字 :'))
b=int(input('請輸入開方數字 :'))

print(a,'開',b,'次方為',int(nroot(a,b)))