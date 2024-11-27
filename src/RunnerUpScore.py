if __name__ == '__main__':
    # n = int(input())
    arr = map(int, input().split())
    scores = list(arr)
    #print(scores)
    # print(max(scores))
    # Solution one
    scores = sorted(scores)
    maxScore = max(scores)
    secondMax = scores[0]
    for i in scores:
        if maxScore > i or i < secondMax:
            secondMax = i
    print(secondMax)

    # solution 2
    scores = sorted(scores, reverse=True)
    maxScore = scores[0]
    secondMax = maxScore
    for i in scores:
        if i != maxScore:
            secondMax = i
            break

    print(secondMax)
