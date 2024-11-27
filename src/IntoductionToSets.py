def average(array):
    # your code goes here
    sets = set(array)
    add = sum(sets)
    total_elements = len(sets)
    average_value = add / total_elements
    return average_value
    # print(average_value)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    # print(arr)
    result = average(arr)
    print(result)
