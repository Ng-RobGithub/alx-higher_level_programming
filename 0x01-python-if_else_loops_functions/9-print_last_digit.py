#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # Calculate the last digit
    print(last_digit, end="")
    return last_digit

# Test the function
num = 12345
result = print_last_digit(num)
print("\nThe last digit is:", result)
