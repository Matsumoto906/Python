while True:
    try:
        n,b=map(int,input().split())
        people = []
        num = 0
        k = 0
        die = 0
        for i in range(n):
            people.append(i + 1)
        
        while die < n-1:
            if people[num] != 0:
                k += 1
                if k == b:
                    people[num] = 0
                    k = 0
                    die += 1
            num += 1
            if num == n:
                num = 0
        
        ans = 0
        while people[ans] == 0:
            ans += 1
        print('%d'%people[ans])
    except:
        break