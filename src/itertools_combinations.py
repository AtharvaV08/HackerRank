from itertools import combinations
S, n = input().split()
n = int(n)
for i in range(1, n+1):
    for j in list(combinations(sorted(S),i)):
        print(''.join(j))