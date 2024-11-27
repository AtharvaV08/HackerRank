def split_and_join(line):
    # write your code here
    sep_words = line.split(" ")
    # print(sep_words)
    joined_words = "-".join(sep_words)
    print(joined_words)


if __name__ == '__main__':
    line = input()
    split_and_join(line)
    # print(result)
    # print(split_and_join(line))
