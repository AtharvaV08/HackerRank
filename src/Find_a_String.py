
def count_substring(string, sub_string):
    count = 0
    for i_start in range(count, len(string)-len(sub_string)+1):
        i_end = i_start + len(sub_string)
        split_string = string[i_start:i_end]
        if sub_string == split_string:
            count = count + 1
    return count


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)