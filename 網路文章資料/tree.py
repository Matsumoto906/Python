btree=[None]*1024
btree[1]='7'
btree[2]='4'
btree[3]='12'
btree[4]='1'
btree[5]='5'
btree[6]='8'
btree[7]='15'
btree[13]='9'

def postorder(p):
  if btree[p] != None:
    postorder(2*p)
    postorder(2*p+1)
    print(btree[p],'',end='',sep=',')

postorder(1)
print()