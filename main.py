'''
EASY Topics:
------------
1. Swap two numbers (with/without temp) ✅
2. Check if a number is prime ✅
3. Find factorial (non-recursive) ✅
4. Fibonacci series (basic recursion) ✅
5. Print sum of elements in a list
6. Find max/min elements in a list
7. Find index of max/min elements
8. Find length of a list
9. Count specific word occurrences
10. Swap first/last or any two elements in a list
11. Remove duplicates from string (set-based)
12. Search an element in a list
13. Clear a list
14. Reverse a list
15. Clone/copy a list (5 approaches)
16. Count occurrences of an element
17. Multiply elements of a list
18. 2nd largest/smallest element
19. Check palindrome (word/string)
20. Reverse words in a string
21. Substring search (and frequency)
22. String length
23. Sum of all odd/even numbers
24. First/all repeating character in a string
25. FizzBuzz
26. Reverse a number
27. Add first and last elements of two lists

Medium Topics:
--------------
28. Factorial using recursion ✅
29. Fibonacci sequence with recursion and validation
30. Remove duplicate words and return a string
31. Check for special characters using regex
32. Check for URLs in strings using regex
33. Leetcode: Contains Duplicate (Set)
34. Leetcode: Valid Anagram (Counter, sort, hashmap approaches)
35. Leetcode: Two Sum (HashMap)
36. Leetcode: Valid Parentheses (Stack)
37. Leetcode: Valid Palindrome (Two pointers with alphanum validation)

Advanced Topics:
----------------
38. LRU Cache Implementation
    collections.OrderedDict or Custom LinkedList + HashMap approach.
39. Multithreading in Python (threading module)
    Write a program that starts multiple threads to compute parts of a task.
40. Producer-Consumer Problem using Queues
41. Decorator Functions
    Implement a timing/decorator to log function performance.
42. Using functools.reduce() and map() on a real problem
43. Recursive Backtracking
    E.g. generating permutations, solving N-Queens.
44. Custom Exception Handling
    Define custom errors for test validations.
45. Use unittest or pytest
    Write end-to-end test for a Python module with mocking.
46. Parsing JSON / XML / API response
    Useful for SDET testing pipelines.
47. Writing Parameterized Tests with Pytest
48. Database interaction using sqlite3
'''

# Easy
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

if num <= 1:
    print(f'{num} is not a prime number')
else:
    for i in range(1, num+1):
        if num%i == 0:
            count = count + 1

    if count == 2:
        print(f'{num} is a prime number')
    else:
        print(f'{num} is not a prime number')

#2a. Check if a number is prime number - using math.sqrt() function
import math
num = int(input("Enter a number: "))

count = 0

if num <= 1:
    print(f'{num} is not a prime number')
else:
    for i in range(2, int(math.sqrt(num)) + 1):
        if num%i == 0:
            print(f'{num} is not a prime number')
            break
    # else after for runs only if the loop completes without break
    else:
        print(f'{num} is a prime number')

#3. Find factorial (non-recursion)
num = int(input("Enter a number: "))

def factorial(num):
    factorial = 1
    if num < 0:
        return (f'There is not factorial for {num}')
    elif num == 0 or num == 1:
        return 1
    else:
        for i in range(1, num+1):
            factorial = factorial * i
        return factorial

print(factorial(num))

#4. Fibonacci series (basic recursion) - Print Fibonacci Sequence: 0 1 1 2 3 5

def fibonacci(num):
    if num < 0 or num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fibonacci(num-1) + fibonacci(num-2)
    

while True:
    numberOfTerms = int(input("Enter the number of terms: "))
    if numberOfTerms > 0:
        for i in range(numberOfTerms):
            print(fibonacci(i))
        break
    else:
        print("Enter a positive number")


# Medium
# Loop & Recursion
#1. Factorial using recursion
num = int(input("Enter a number: "))

def factorial(num):
    if num < 0:
        return f"no factorial for {num}"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)
    

print(factorial(num))

