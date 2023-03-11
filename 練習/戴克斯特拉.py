name=['別針','海報','門票','變形金剛','滑板車','動物森友會']
n=[]
dis=[]
t=[]

while True:
    try:
        s=list(map(str,input().split()))
        n.append(s)
    except:
        break

print(n)