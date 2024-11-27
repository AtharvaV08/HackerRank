import math


def alphabet_rangoli(n: int):
    import string

    # Generate the alphabet
    alphabet = string.ascii_lowercase
    print(alphabet)

    # Create a list to hold each line of the rangoli
    lines = [None] * (n + 1)
    # print(lines)

    index :int = n
    if n == 1:
        print('a')
        return

    # Build the rangoli from top to center
    for i in range(n):
        # Create the left and right sides of the rangoli
        left = '-'.join(alphabet[n - 1:i:-1])  # From n-1 down to i
        right = '-'.join(alphabet[i + 1:n])  # From i+1 up to n-1
        # Combine left, middle (current letter), and right

        line = left + ('-' if left else '') + alphabet[i] + '-' + right

        # Add padding to the line
        lines[index] = (line.center(4 * n - 3, '-'))
        index = index - 1


    # Create the full rangoli by combining the top and the reversed top (except the last row)
    full_rangoli = lines + lines[-2::-1]

    # Print the result
    for line in full_rangoli:
        if line != None:
            print(line)


# def print_rangoli(size):
#     row_size = size * 2 - 1
#     column_size = row_size * 2 - 1
#     center = math.ceil(column_size / 2)
#     for i_row in range(1, math.ceil((row_size + 1) / 2) + 1):
#         row = ""
#         row_counter = 1
#         for i_column in range(1, center):
#             if (i_column == center or center - 2 == i_column) and i_row + 1 == row_counter:
#                 row = row + '*'
#                 row_counter = row_counter + 1
#             else:
#                 row = row + '-'
#
#         row = row + '*'
#
#         for i_column in range(center + 1, 2, -1):
#             row = row + '-'
#
#         print(row)
#
#     for i_row in range(math.ceil((row_size + 1) / 2), 1, -1):
#         row = ""
#         for i_column in range(1, center + 1):
#             row = row + '-'
#
#         row = row + '*'
#
#         for i_column in range(center + 2, 3, -1):
#             row = row + '-'
#
#         # print(row)
#
#
# def generate_pattern(n):
#     middle = n // 2  # Calculate the middle index
#
#     for i in range(n):
#         # Determine leading spaces
#         if i <= middle:
#             spaces = middle - i
#         else:
#             spaces = i - middle
#
#         # Print leading spaces
#         line = '-' * spaces
#
#         # Determine the number of stars
#         stars = n - 2 * spaces
#
#         # Print stars and spaces
#         for j in range(stars):
#             if j < stars - 1:
#                 line += '*-'  # Star followed by a hyphen
#             else:
#                 line += '*'  # Last star without a hyphen
#
#         # Print trailing spaces (same as leading)
#         line += '-' * spaces
#
#         # Output the constructed line
#         print(line)


if __name__ == '__main__':
    n = int(input())
    alphabet_rangoli(n)

    # -----e-----
    # e-d-c-b-a-b-c-d-e
