# EASY LEVEL 
# Variables and Data Types

#1. Swap two numbers - Using Tuple

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

print('First number: ', num1)
print('Second number: ', num2)

num1, num2 = num2, num1

print('After swapping')
print('First number: ', num1)
print('Second number: ', num2)


#1a. Swap two numbers - Using a third variable

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

print('First number: ', num1)
print('Second number: ', num2)

num3 = num1
num1 = num2
num2 = num3

print('After swapping')
print('First number: ', num1)
print('Second number: ', num2)

#1b. Swap two numbers - Without using a third variable

num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print('First number: ', num1)
print('Second number: ', num2)

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print('After swapping')
print('First number: ', num1)
print('Second number: ', num2)