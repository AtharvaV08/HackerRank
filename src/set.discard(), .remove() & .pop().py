n = int(input())                                              #CHANGES I WANT TO DO IN THIS CODE
s = set(map(int, input().split()))                    #1. TO TAKE AS MANY INPUTS IN THE SECOND LINE WHICH USER HAS GIVEN IN THE FIRST LINE
num_cmd = int(input())                                            #EG: IF USER HAS GIVEN 5 INPUT IN THE FIRST LINE THEN
                                                                        # THE 2ND LINE SHOULD TAKE ONLY 5 INPUTS NOT MORE THAN THAT
for item in range(num_cmd):
    cmd = input().split()
    if cmd[0] == "pop":
        s.pop()
    if cmd[0] == "remove":
        s.remove(int(cmd[1]))
    if cmd[0] == "discard":
        s.discard(int(cmd[1]))

total = 0
for item in s:
    total = total + item
print(total)
