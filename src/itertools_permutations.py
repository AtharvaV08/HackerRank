from itertools import permutations
S, n = input().split()
for i in list(permutations(sorted(S), int(n))):
    print(''.join(i))
