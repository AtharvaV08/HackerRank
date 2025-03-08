a = int(input())
num_in_a = set(map(int, input().split()))
n = int(input())
for cmds in range(n):
    cmd = input().split()
    if cmd[0] == "intersection_update":
        num_in_a.intersection_update(set(map(int, input().split())))
    elif cmd[0] == "update":
        num_in_a.update(set(map(int, input().split())))
    elif cmd[0] == "symmetric_difference_update":
        num_in_a.symmetric_difference_update(set(map(int, input().split())))
    elif cmd[0] == "difference_update":
        num_in_a.difference_update(set(map(int, input().split())))

total = sum(num_in_a)
print(total)