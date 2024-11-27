# Find a number from an array. If present return index or return -1
arr = [1, 2, 3, 4, 6, 7, 45, 65, 80, 88, 89]
arr = sorted(arr)
number = 80

"""
def linear_search(arr, number):
    for i in range(len(arr)):
        if arr[i] == number:
            # print("Number Found: ", number)
            return i
    return -1
def binary_search(arr, number):
    # Binary search logic here
    left, right = 0,len(arr)
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == number:
            return mid
        if arr[mid] < number:
            left = mid + 1
        else:
            right = mid -1

    return -1
"""
def binary_search(arr, number):
    left, right = (0, len(arr))
    return search_using_loop(arr, number, left, right)
    #return search_using_recursion(arr, number, left, right)

#arr = [1, 2, 3, 4, 6, 7, 45, 65, 80, 88, 89]
def search_using_loop(arr, number, left, right):
    print("Number to be find ")
    while left != right:
        mid = (left + right) // 2
        if number == arr[mid]:
            return mid
        elif number < arr[mid]:
            return mid




def search_using_recursion(arr, number, left, right):
    mid = (left + right) // 2
    print("Left number: ", left)
    print("Right number: ", right)
    print("Mid Value: ", mid)
    if left == right:
        return -1

    if number == arr[mid]:
        return mid
    elif number < arr[mid]:
        right = mid - 1
        return search_using_recursion(arr, number, left, right)
    elif number > arr[mid]:
        left = mid + 1
        return search_using_recursion(arr, number, left, right)



# index = linear_search(arr, number)
index = binary_search(arr, number)
print(f"Index of Number {number} is {index}")

# arr = [1, 2, 3, 4, 6, 7, 45, 65, 80, 88, 89]
# arr = sorted(arr)
# number = 88
