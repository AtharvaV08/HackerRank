def mutate_string(string, position, character) -> str:  # 4
    l = list(string)
    l[position] = character
    string = ''.join(l)
    return string  #5


if __name__ == '__main__':
    s = input()  # 1. input jgfsdfsfsfsf
    i, c = input().split()  # 2. input 5 k
    s_new = mutate_string(s, int(i), c)  # 3. calling mutate_string() # 6
    print(s_new)  # 7    H
