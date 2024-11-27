if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    score = student_marks[query_name]
    # print(score)
    average = (score[0] + score[1] + score[2]) / 3
    average = f"{average:.2f}"
    print(average)

# {
#   'krushna': [67.0, 68.0, 69.0],
#   'Arjun': [70.0, 98.0, 63.0],
#   'Malika': [52.0, 56.0, 60.0]
# }
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika