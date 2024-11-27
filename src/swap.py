#arr = [5,10]
a = int(input("Enter Number: "))
b = int(input("Enter Number 2: "))
a, b = b, a
print(f"Value of a: {a}, Value of b: {b}")
sw = a
a = b
b = sw
print(f"Value of using 3rd variable: {a}, Value of b: {b}")
a = a + b
b = a - b
a = a - b
print(f"Value of a: {a}, Value of b: {b}")
# a = 25
# b = 50
# print(arr)
# # arr[0] = 25
# # print(arr)
# # arr[1] = 50
# # print(arr)
# # arr.append(75)
# # print(arr)
# a = arr[0]
# arr[0] = arr[1]
# print(arr)
# arr[1] = a
# print(arr)