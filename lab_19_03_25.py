# Exercise programs on basic control structures & loops.

#(a) Write a program for checking the given number is even or odd.

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

number = int(input("Enter a number: "))
print(check_even_odd(number))

#(b) Using a for loop, write a program that prints the decimal equivalents of 1/2, 1/3, 1/4 ,....... 1/10
def print_decimal_equivalents():
    for i in range(2, 11):
        print(f"1/{i} = {1/i:.2f}")

print_decimal_equivalents()

#(c) Write a program for displaying reversal of a number.
def reverse_number(number):
    reversed_number = int(str(number)[::-1])
    return reversed_number

number = int(input("Enter a number: "))
print(f"Reversed number: {reverse_number(number)}")

#(d) Write a program for finding biggest number among 3 numbers.

def find_biggest_number(a, b, c):
    if a > b and a > c:
        return f"The biggest number is {a}"
    elif b > a and b > c:
        return f"The biggest number is {b}"
    else:
        return f"The biggest number is {c}"

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print(find_biggest_number(a, b, c))

#(e) Write a program using a while loop that asks the user for a number, and prints a countdown from that number to zero.

def countdown(number):
    while number >= 0:
        print(number)
        number -= 1

number = int(input("Enter a number: "))
countdown(number)

