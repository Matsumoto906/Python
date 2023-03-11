n=int(input())
for i in range(0,n):
    in_str=input().strip().split("/")
    ip=list(map(int,in_str[0].split(".")))
    netmask=list(map(int,in_str[1].split(".")))
    mask_len=0
    for a in range(0,3):
        print(ip[a] & netmask[a],end=".")
    print(ip[3] & netmask[3],end="")#第四個byte(第四組數字)另外處理
    print("/",end="")
    for a in range(0,3):
        print(256+(ip[a] |( ~netmask[a])),end=".")
    print(256+(ip[3] |( ~netmask[3])))#第四個byte(第四組數字)另外處理
    #print(ip[a] & netmask[a])