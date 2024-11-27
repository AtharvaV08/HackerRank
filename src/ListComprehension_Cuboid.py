# You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
# Print a list of all possible coordinates given by (i, j, k) on a 3D grid
# where the sum of i + j + k is not equal to n.
# Here, 0<=i<=x;0<=j<=y;0<=k<=z.
# Please use list comprehensions rather than multiple loops, as a learning exercise
from itertools import permutations

if __name__ == '__main__':
    x = int(input())
    # print("Value of x is: ", x)
    y = int(input())
    # print("Value of y is: ", y)
    z = int(input())
    # print("Value of z is: ", z)
    n = int(input())
    # print("Value of n is: ", n)
    valid_combinations = []
    result = [(i, j, k) for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    for combination in result:
        sum = combination[0] + combination[1] + combination[2]
        if sum != n:
            valid_combinations.append(list(combination))
    print(valid_combinations)
    # for i in range(0, x+1):
    #     for j in range(0, y+1):
    #         for k in range(0, z+1):
    #             val = [i, j, k]
    #             val_ijk = permutations(val)
    #             for combination in val_ijk:
    #                 sum = combination[0]+combination[1]+combination[2]
    #                 if sum != n:
    #                     if not valid_combinations.__contains__(list(combination)):
    #                         valid_combinations.append(list(combination))
    # valid_combinations.sort()
    #

# [(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 0), (0, 0, 2), (0, 2, 0), (2, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0), (0, 2, 2), (2, 0, 2), (2, 2, 0), (1, 1, 2), (1, 2, 1), (2, 1, 1), (1, 2, 2), (2, 1, 2), (2, 2, 1), (2, 2, 2)]
# [[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]