def print_formatted(number):
    # your code goes here
    zero = 0
    width = len(bin(number)) - 2
    for numbers in range(1, number + 1):
        decimal = str(numbers)
        octal = oct(numbers)[2:]  # Remove '0o' prefix
        hexadecimal = hex(numbers)[2:].upper()  # Remove '0x' prefix
        binary = bin(numbers)[2:]
        print(f"{decimal:>{width}} {octal:>{width}} {hexadecimal:>{width}} {binary:>{width}}") # '>' Symbol represent right alignment


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
