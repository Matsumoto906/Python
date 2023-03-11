a=set(input('請輸入A的興趣 :').split())
b=set(input('請輸入B的興趣 :').split())

print('A與B所有的興趣 :',sorted(a.union(b)))
print('A與B共同的興趣 :',sorted(a.intersection(b)))
print('A與彼此沒有的興趣 :',sorted(a.symmetric_difference(b)))
print('A有但B沒有的興趣 :',sorted(a.difference(b)))