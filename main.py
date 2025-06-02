#1. Swap two numbers

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
