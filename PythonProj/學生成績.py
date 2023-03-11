people=int(input('請輸入學生人數:'))
count=0
min=''
max=''
for i in range(1,people+1):
    score=int(input('請輸入學生的成績(0~100):'))
    print(score,end=' ')
    if score>=60:
        min=score
    if score<60:
        max=score

if max=='':
    print('及格分數最低為:',min)
    print('best case')
if min=='':
    print('不及格分數最高為:',max)
    print('worst case')
if max and min !='':
    print('不及格分數最高為:',max)
    print('及格分數最低為:',min)
