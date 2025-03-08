from collections import defaultdict

grp_dict = defaultdict(list)

n_m = list(map(int, input().split()))

grp_index = 0
for grp_size in n_m:
    for element in range(0, grp_size):
        grp_dict[grp_index].append(input())
    grp_index += 1

# print(grp_dict)
n_line_A = grp_dict[0]
m_line_B = grp_dict[1]

for element_b in m_line_B:
    index = 0
    isIndexNotFound = True
    for element_a in n_line_A:
        index += 1
        if element_a == element_b:
            isIndexNotFound = False
            print(index, end=" ")
    if isIndexNotFound:
        print(-1)
    else:
        print()

