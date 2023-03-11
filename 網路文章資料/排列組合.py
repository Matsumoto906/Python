import itertools
a = [1, 2, 3]
b = list(itertools.permutations(a, r=2))
print(b)