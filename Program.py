
# Description: This is a simple Python program that prints "Hello, world!" to the console.

print("Hello, world!")

# Calculate the sum of two numbers

# Input: two numbers
num1 = 5
num2 = 3
sum = num1 + num2
print("The sum of", num1, "and", num2, "is", sum)

# find the square of a number

def square(num):
    return num * num
print(square(5))  # Output: 25

# Accept the user's name and greet them with it.
name = input("Please enter your name: ")
print("Hello,", name)

# Check whether a number is even or odd.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even.")
else:
    print(num, "is odd.")
    
# Write a Python program that takes a list and returns a new list with unique elements of the first list.
# python

def unique_list(lst):
    return list(set(lst))
print(unique_list([1, 2, 2, 3, 4, 4,8,8, 5]))  # Output: [1, 2, 3, 4, 5]

# Convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
print(celsius_to_fahrenheit(36))  #

# Calculate the area of a circle.

def area_of_circle(radius):
    return 3.14159 * radius ** 2
print(area_of_circle(5))  # Output: 78.53975

# Reverse a given string.

def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))  # Output: olleh

# Check if a number is a prime number.

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
        return True
print(is_prime(43))  # Output: True

# Find the factorial of a number. Calculate the factorial of a number.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(5))  # Output: 120

# Find the maximum number in a list. Find the largest item from a given list.

def find_max(lst):
    return max(lst)
print(find_max([1, 2, 3, 4, 5]))  # Output: 5

#Write a Python program to check whether a number is in a given range.

def in_range(num, start, end):
    if num in range(start, end):
        return True
    else:
        return False
print(in_range(10, 1, 20))  # Output: True
    
# Calculate the number of upper case letters and lower case letters in a string.

def count_case(s):
    upper = 0
    lower = 0
    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return upper, lower
print(count_case("Hello, World!"))  # Output: (2, 9)



