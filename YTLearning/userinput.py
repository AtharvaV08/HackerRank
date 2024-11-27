"""
##2 VARIABLES
Atharva = input("Name: ")
Vaidya = input("Age: ")
MIT =  int(input("MIT Fees: "))
DY_Patil = float(input("DY Patil Fees: "))
Total = MIT + DY_Patil
print(Atharva)
print(Vaidya)
print(MIT)
print(DY_Patil)
print(Total)
"""
##USER INPUT
# a = int(input("Enter First Number: "))
# b = float(input("Enter Second Number: "))
# sum = (a + b)
# print("The sum of both the numbers is: ", sum)

## Input side of square from the user and print its area
# side = float(input("Enter the side of the square: "))
# area = side * side
# print("The area of the square: ", area)

## Input 2 floating point numbers from the user & print their average
# num1 = float(input("Enter first number: "))
# num2 = float(input("Enter second number: "))
# average = (num1 + num2) / 2
# print("The average of the two numbers is: ", average)

## Input 2 int numbers, a and b. Print True is a is greater than or equal to b. If not print False
# a = int(input("Enter the number for a: "))
# b = int(input("Enter the number for b: "))
# true_false = a >= b
# print(true_false)
# #OR
# print(a >= b)

## Input user's first name and print it's length
# First_Name = input("Enter First Name:")
# length = len(First_Name)
# print("The length of First Name is: ", length)

## Find the occurrence of $ in a string
# Occurrence = "ASDFGHJ$$"
# Found = Occurrence.count("$")
# print(Found)
# #OR
# print(Occurrence.count("$"))

## Grade Students based on marks
# marks = 69
# if (marks >= 90):
#     print("Grade A")
# elif(marks <90 and marks >= 80):
#     print("Grade B")
# elif(marks <80 and marks >=70):
#     print("Grade C")
# else:
#     print("Grade D")

## Check if a number entered by the user is even or add
# number = float(input("Enter the number: "))
# if (number%2 == 0):
#     print("Even Number")
# else:
#     print("Odd Number")

##Find the greatest of 3 numbers entered by the user
# number1 = float(input("Enter the 1st number: "))
# number2 = float(input("Enter the 2nd number: "))
# number3 = float(input("Enter the 3rd number: "))
# if(number1 > number2 and number1 > number3):
#     print(f"Number 1st {number1} is greatest")
# elif(number2 > number1 and number2 > number3):
#     print(f"Number 2nd {number2} is greatest")
# else:
#     print(f"Number 3rd {number3} is greatest")

##Check if a number is a multiple of 7 or not
# number = float(input("Enter the Number: "))
# if(number%7 == 0):
#     print(f"Number {number} is multiple of 7")
# else:
#     print(f"Number {number} is not multiple of 7")

## Ask the user to enter names of the their 3 favourite movies & store them in a list
# movie1 = input("Enter name of movie1: ")
# movie2 = input("Enter name of movie2: ")
# movie3 = input("Enter name of movie3: ")
# Favourite_movies = [movie1, movie2, movie3]
# print("User's favourite movies are: ", Favourite_movies)
#OR
# movies = []
# movie1 = input("Enter first movie: ")           #OR we can write it as movies.append(input("enter 1st movie: "))
# movie2 = input("Enter second movie: ")
# movie3 = input("Enter third movie: ")
#
# movies.append(movie1)
# movies.append(movie2)
# movies.append(movie3)

## Check if a list contains a palindrome of elements
# list = [1, 2, 3, 2, 1]
# list2 = list.copy()
# list2.reverse()
# print(list2)
# if list == list2:
#     print("Hurray! It is palindrome!!")
# else:
#     print("Sorry! It is not a palindrome!!")

## Count the number of students with the 'A' grade in the following tuple
# tuple = ["C", "D", "A", "A", "B", "B", "A"]
# print("Total no. of Students with 'A' Grade are: ", tuple.count("A"))
# sortedTuple = sorted(tuple)
# print(sortedTuple)
# #OR
# tuple.sort()
# print(tuple)

## Store word meanings in a python dictionary
# store = {
#     "table" : ["a piece of furniture", "list of facts & figures"],
#     "cat" : "a small animal"
#
# }
#
# print(store)

## Given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students
# classroom = {
#     "python", "java", "c++", "python", "javascript", "java", "python", "java", "c++", "c"
# }
# print(classroom)
# print(f"You will require {len(classroom)} classrooms")

## Enter marks from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value
# marks = {}
# sub1 = input("Enter 1st sub: ")
# sub2 = input("Enter 2nd subject: ")
# sub3 = input("Enter 3rd subject: ")
# marks1 = float(input("Enter of marks of sub1: "))
# marks2 = float(input("Enter marks of sub2: "))
# marks3 = float(input("Enter marks of sub3: "))
# marks.update({sub1 : marks1})
# marks.update({sub2 : marks2})
# marks.update({sub3 : marks3})
# print(marks)

## Figure out way to store 9 & 9.0 as separate values in the set. (You can take help of built-in data types)
# values = {9, "9.0"} # "" it is used as python considers it as one int and other str
# print(values)
# #OR
# values = {
#     ("float",9.0),
#     ("int",9)
# }
# print(values)

#-----------------------------------LOOPS--------------------------------------------------#

#---------------------------------WHILE LOOP-----------------------------------------------#
## Print numbers 1 to 100
# num = 1
# while num <= 100:
#     print(num)
#     num = num + 1
#
# ## Print numbers from 100 to 1
# num = 100
# while num >= 1:
#     print(num)
#     num = num - 1

## Print the multiplication table of a number n
# n = int(input("Enter number: "))
# t = 1
# while t <= 10:
#     print(n * t)
#     t = t + 1

## Print the elements of the following list using a loop
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# e = list[0]
# while e != len(list) - 1:
#     print(list)
#     e = e + 1
#OR
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# index = 0
# while index < len(list):
#     print(list[index])
#     index = index + 1

## Search for a number x in this tuple using loop
# tuple = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# f = 0
# x = int(input("Enter no.: "))
# while f < len(tuple):
#     if(tuple[f] == x):
#         print("Number Found at index", f)
#         break
#     else:
#         print("Number Not Found!!!", f)
#     f = f + 1

#-------------------------------------FOR LOOP----------------------------------------------#

## Print the elements of the following list using loop
# list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# for elements in list:
#     print(elements)

## Search for a number x in this tuple using loop
# tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
# x = 36
# i = 0
# for char in tup:
#     if char == x:
#         print("Number Found at index", i)
#     i = i + 1

#-------------------------------------FOR LOOP RANGE FUNCTION----------------------------------------------#

## Print numbers from 1 to 100
# for num in range(1, 101):
#     print(num)

## Print numbers from 100 to 1
# for num in range(100, 0, -1):
#     print(num)

## Print the multiplication table for number n
# n = int(input("Enter number: "))
# for table in range(n, n*11, n*1):
#     print(table)

## Find the sum of first n natural numbers(using while loop)
# n = 7
# sum = 0
# i = 1
# while i <= n:
#     sum += i
#     i += 1
# print("Total sum is", sum)

## Find the factorial of first n numbers(using for loops)
# n = 5
# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(f"Fact of {n} =", fact)

##