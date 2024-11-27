if __name__ == '__main__':
    scores = [37.21, 37.21, 37.2, 41, 39]
    scores.sort()
    lowest = scores[len(scores) - 1]
    secondLowest = lowest
    for score in scores:
        # print(lowest, secondLowest, score)
        if score < lowest:
            secondLowest = lowest
            lowest = score
        elif score < secondLowest and score != lowest:
            secondLowest = score
    print(secondLowest)
