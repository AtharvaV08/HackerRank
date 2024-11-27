# Initialize your list
# and read in the value of followed by lines of commands where each command will be of the  types listed above.
# Iterate through each command in order
# and perform the corresponding operation on your list.
if __name__ == '__main__':
    list = []
    N = int(input())
    for i in range(N):
        cmd = input()
        print("Input command: ", cmd)
        cmdArgsList = cmd.split()
        print("cmdArgsList: ", cmdArgsList)
        if cmdArgsList[0] == 'insert':
            index = int(cmdArgsList[1])
            value = int(cmdArgsList[2])
            list.insert(index, value)
        elif cmdArgsList[0] == 'print':
            print(list)
        if cmdArgsList[0] == 'remove':
            value = int(cmdArgsList[1])
            list.remove(value)
        if cmdArgsList[0] == 'append':
            value = int(cmdArgsList[1])
            list.append(value)
        if cmdArgsList[0] == 'sort':
            list.sort()
        if cmdArgsList[0] == 'pop':
            list.pop()
        elif cmdArgsList[0] == 'reverse':
            list.reverse()
