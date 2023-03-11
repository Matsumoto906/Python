dic={'z':'b','x':'n','c':'m','v':'z',
     'b':'x','n':'c','m':'v','a':'j',
     's':'k','d':'l','f':'a','g':'s',
     'h':'d','j':'f','k':'g','l':'h',
     'q':'i','w':'o','e':'p','r':'q',
     't':'w','y':'e','u':'r','i':'t',
     'o':'y','p':'u','Z':'B','X':'N',
     'C':'M','V':'Z','B':'X','N':'C',
     'M':'V','A':'J','S':'K','D':'L',
     'F':'A','G':'S','H':'D','J':'F',
     'K':'G','L':'H','Q':'I','W':'O',
     'E':'P','R':'Q','T':'W','Y':'E',
     'U':'R','I':'T','O':'Y','P':'U'}
s=input()
for i in s:
    if i in dic:
        print(dic[i],end='')
    else:
        print(i,end='')