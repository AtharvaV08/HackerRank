#!/bin/python3

import math
import os
import random
import re
import sys


def solve(statement: str):
    # string = len(s)
    # result = ""
    # words = statement.split(" ")
    # # print(words)
    # for word in words:
    #     # print(word)
    #     first_char = word[:1]
    #     # print(f"First character is: {first_char}")
    #     rest_char = word[1:]
    #     # print(f"Rest character is: {rest_char}")
    #     first_capi = first_char.capitalize()
    #     joined_word = first_capi + rest_char
    #     # print(joined_word)
    #     result = result + " " + joined_word
    # return result.strip()
                                #OR
    return re.sub(r'\b[a-zA-Z]', lambda match: match.group(0).upper(), statement)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = solve(s)
    print(result)
    # fptr.write(result + '\n')
    # fptr.close()
