t = int(input())
for inputs in range(t):
    a_fl_test_case = int(input())            # FIRST LINE OF EACH TEST CASE A
    a_secl_test_case = set(map(int, input().split()))  # SECOND LINE OF EACH TEST CASE A
    b_fl_test_case = int(input())
    b_secl_test_case = set(map(int, input().split()))

    a_set = a_secl_test_case.issubset(b_secl_test_case)
    print(a_set)