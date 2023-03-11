for t in range(int(input())):
    s=input().strip().split("/")
    ip=list(map(int,s[0].split(".")))
    mlen=int(s[1])
    netmask=[0,0,0,0]
    for a in range(3,-1,-1):
        c=mlen-(a)*8
        if c<0:
            continue
        netmask[a]=256-2**(8-c) #256-2^(8-c)
        mlen-=c
        
    mask_len=0
    for a in range(0,3):
        print(ip[a] & netmask[a],end=".")
    print(ip[3] & netmask[3],end="")
    print("/",end="")
    for a in range(0,3):
        print(256+(ip[a] |( ~netmask[a])),end=".")
    print(256+(ip[3] |( ~netmask[3])))
