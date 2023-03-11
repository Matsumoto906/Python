import datetime
for i in range(int(input())):
        a,b=map(int,input().split())
        anyday=datetime.datetime(2021,a,b).strftime("%w")
        if anyday=='1':
            print('Monday')
        elif anyday=='2':
            print('Tuesday')
        elif anyday=='3':
            print('Wednesday')
        elif anyday=='4':
            print('Thursday')
        elif anyday=='5':
            print('Friday')
        elif anyday=='6':
            print('Saturday')
        elif anyday=='0':
            print('Sunday')  