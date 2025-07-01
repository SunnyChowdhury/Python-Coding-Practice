# EASY 
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

#2. Check if a number is prime number

num = int(input("Enter a number: "))

count = 0

if num > 1:
    for i in range(1, num+1):
        if (num%i == 0):
            count = count + 1
else:
    print(f'{num} is not a prime number')

if (count == 2):
    print(f'{num} is a prime number')
else:
    print(f'{num} is not a prime number')