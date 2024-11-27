arr = [1, 2, 3, 4, 6, 7, 45, 65, 80, 88, 89]
arr = sorted(arr)
number = 10


def search(arr):
    left = 0
    print("Left is:", left)
    right = len(arr)
    print("Right is: ", right)
    mid = (left + right) // 2
    print("Mid is: ", mid)
    while left != right:
        if arr[mid] == number:
            print(f"Number {number} Found! ")
            break

        elif arr[mid] < number:
            print(f"Number {number} is to the right of mid and is greater than number", arr[mid])
            left = mid
            print("New mid that is changed to the left value: ", left)
            # right = len(arr)
            # print("New right is: ", right)
            mid = (left + right) // 2
            print(f"Number of new mid is {mid}")
            #break

        elif arr[mid] > number:
            print(f"Number {number} is to the left of mid and is less than the number", arr[mid])
            # left = mid
            # print("new left is: ", left)
            right = mid
            print("New right is: ", right)
            mid = (left + right) // 2
            print(f"The value {mid} is new mid value!")
            break
        else:
            print("Number not found!")
            break


search(arr)
