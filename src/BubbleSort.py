list = [10, 9, 11, 6, 15, 2]
TotalPass = len(list) -1
currentPass = 0
while currentPass < TotalPass:
    currentPass += 1
    print(f"----------------  Running pass {currentPass} ----------------")
    size = len(list) - currentPass
    currentIndex = 0
    nextIndex = currentIndex + 1
    while currentIndex < size:
        if list[currentIndex] > list[nextIndex]:
            list[currentIndex], list[nextIndex] = list[nextIndex], list[currentIndex]
        currentIndex += 1
        nextIndex +=1
        print(list)

print(list)
