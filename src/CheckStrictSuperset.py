
a = set(map(int, input().split()))
n = int(input())
for n_line in range(n):
    next_n_line = set(map(int, input().split()))
    if not a > next_n_line:
        print("False")
        break
else:
    print("True")

# NEED TO UNDERSTAND THIS LOOP ^