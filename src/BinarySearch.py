arr = [1, 2, 3, 4, 6, 7, 45, 65, 80, 88, 89]
arr = sorted(arr)
number = 10

def search(arr):
    print("Find Index of number", number)
    left = 0
    print("Left Pointer is: ", left)
    right = len(arr)
    print("Right Pointer is: ", right)
    mid = (left + right) // 2
    print("Mid pointer is: ", mid)
    while left != right:
        if arr[mid] == number:
            print("Number Found On Index: ", mid)
            break

        elif arr[mid] > number:
            print(f"Number {number} on left and it is less than number: ", arr[mid])
            right = mid
            mid = (left + right) // 2
            print("New Right Pointer Value: ", right)
            print("New Mid value is: ", mid)


        elif arr[mid] < number:
            print(f"Number {number} on right and it is greater than number: ", arr[mid])
            left = mid
            mid = (left + right) // 2
            print("New Left Pointer Value: ", left)
            print("New Mid value is: ", mid)
        else:
            print(f"Number {number} not found")
            break



search(arr)