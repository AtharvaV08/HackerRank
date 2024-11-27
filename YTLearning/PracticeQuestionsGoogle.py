#--------------------------------------------FOR LOOP-------------------------------
## Print the first 20 even numbers
# i = 1
# x = 21
# for num in range(i, x):
#     print(num * 2)

## Calculate the factorial of a given number
# import math
# n = int(input("Enter Number: "))
# print(math.factorial(n))

## Program to calculate the sum of all numbers from 1 to a given number
# gn = int(input("Enter Ending number: "))
# a = 1
# for sum in range(a, gn + 1):
#     a = a + sum
# print(a)

## Program to build a multiplication table of a given number
# n = int(input("Enter the number: "))
# s = 1
# for i in range(s, 11):
#     print(n, "*", i, "=", s * n)
#     s = i + 1

## Python program to display the numbers from a list
# list = [1, 2, 3, 4, 5, 5, 7, 8, 9, 20]
# for display in list:
#     print(display)

## Program to count the total number of digits in a number
# num = 224455789654
# num = str(224455789654)
# count = 0
# for total_number in num:
#     count += 1
# print(count)

## Program to display numbers from a list
# list = [1, 2, 3, 3, 5, 6, 7, 8, 9]
# for display in list:
#     print(display)

## Program to check if the given string is palindrome
# given_string = "racecar"
# reverse_string = ""
# for palindrome in given_string:
#     reverse_string = palindrome + reverse_string
# if given_string == reverse_string:
#     print("It is a Palindrome!")
#     # break
# else:
#     print("It is not a Palindrome!!")

## Program that accepts a word from the user and reverses it
# word = input("Enter word: ")
# reverse_word = ''
# for i in word:
#     reverse_word = i + reverse_word
# print(reverse_word)

## Program to count the number of even and odd numbers from a series of numbers
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_number = ''
# odd_number = ''
# # count = 0
# for i in numbers:
#     if i%2 == 0:
#         even_number += str(i) + ', '
#         print(i, "Even number")
#     else:
#         odd_number += str(i) + ', '
#         print(i, "Odd number")
# print("Even Numbers are: ", even_number)
# print("Odd Numbers are: ", odd_number)

# for i in range(1, 11):
#     print("Current Value: ", i)

# i = 1
# while i <= 10:
#     print("Current Value: ", i)
#     i += 1

#-----------------------------------------****************--------------------------------------------------------------
# num = ""
# for i in range(1,10):
#     for j in range(0, 9):
#         num += num + str(i)
#     print(num)
#     num = ""

# new_hires = [('Mark Adams', 'SQL Analyst', 4000),
#              ('Leslie Burton', 'HR Specialist', 2300),
#              ('Dorothy Castillo', 'UX Designer', 3100)]
# def remove_sql_specialists(new_hires):
#     for person in new_hires[:]:
#         if 'SQL' in person[1]:
#             new_hires.remove(person)
#     print(new_hires)
#------------------------------------------***************--------------------------------------------------------------

# countries = ['Thailand', 'Vietnam', 'Malaysia', 'UAE']
# for country in countries:
#     print(f"{country} contains {len(country)} letters!")

## Program to display all the numbers within a range except the prime numbers
# for i in range(1, 20):
#     if i/i == 0 or i/1 == 0:
#         print("Prime Number!")
#     else:
#         print(i, "Not a prime number!!")
# i += 1


def average(a, b, c):
    total_average = float(a + b + c) / 3
    print(total_average)
    return total_average
average(1, 2, 3)