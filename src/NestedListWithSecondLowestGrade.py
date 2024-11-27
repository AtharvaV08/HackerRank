# Given the names and grades for each student in a class of N students,
# store them in a nested list and print the name(s)
# of any student(s) having the second lowest grade.
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each
# name on a new line.
# S1 10
# S2 10
# S3 7
# S4 9
# S5 8

if __name__ == '__main__':
    print("Number of Students")
    students = [
        ['Harry', 37.21],
        ['Berry', 37.21],
        ['Tina', 37.2],
        ['Akriti', 41],
        ['Harsh', 39]
    ]
    # for _ in range(int(input())):
    #     currentStudent = []
    #     print("Enter Student Name")
    #     name = input()
    #     currentStudent.append(name)
    #     print("Enter score")
    #     score = float(input())
    #     currentStudent.append(score)
    #     students.append(currentStudent)
    students.sort(key=lambda student: student[1])
    print(students)
    lowestStudent = students[len(students) - 1]
    secondLowest = lowestStudent
    for student in students:
        # print(lowestStudent, secondLowest, student)
        if student[1] < lowestStudent[1]:
            secondLowest = lowestStudent
            lowestStudent = student
        elif student[1] < secondLowest[1] and student[1] != lowestStudent[1]:
            secondLowest = student
    print("second lowest score", secondLowest[1])

    secondLowestStudents = []
    for student in students:
        if student[1] == secondLowest[1]:
            secondLowestStudents.append(student[0])
    secondLowestStudents.sort()
    print("second lowest students", secondLowestStudents)
    for student in secondLowestStudents:
        print(student)









