if __name__ == '__main__':
    n = int(input())
    # print(n)
    # integer_list = map(int, input().split())
    # print(type(integer_list))
    map_obj = map(int, input().split())
    t1 = tuple(map_obj)
    print(hash(t1))