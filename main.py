'''
Basic programming: Easy
-----------------------
1. Swap two numbers (with/without temp) ✅
2. Check if a number is prime ✅
3. Find factorial (non-recursive) ✅
4. Fibonacci series (basic recursion) ✅
5. Print sum of elements in a list ✅
6. Find max/min elements in a list ✅
7. Find index of max/min elements ✅
8. Find length of a list ✅
9. Count specific word occurrences ✅
10. Swap first/last or any two elements in a list ✅
11. Remove duplicates from string (set-based) ✅
12. Search an element in a list ✅
13. Clear a list ✅
14. Reverse a list ✅
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

Basic programming: Medium
-------------------------
28. Factorial using recursion ✅
29. Fibonacci sequence with recursion and validation
30. Remove duplicate words and return a string
31. Check for special characters using regex
32. Check for URLs in strings using regex

Basic programming: Advanced
---------------------------
33. LRU Cache Implementation
    collections.OrderedDict or Custom LinkedList + HashMap approach.
34. Multithreading in Python (threading module)
    Write a program that starts multiple threads to compute parts of a task.
35. Producer-Consumer Problem using Queues
36. Decorator Functions
    Implement a timing/decorator to log function performance.
37. Using functools.reduce() and map() on a real problem
38. Recursive Backtracking
    E.g. generating permutations, solving N-Queens.
39. Custom Exception Handling
    Define custom errors for test validations.
40. Use unittest or pytest
    Write end-to-end test for a Python module with mocking.
41. Parsing JSON / XML / API response
    Useful for SDET testing pipelines.
42. Writing Parameterized Tests with Pytest
43. Database interaction using sqlite3

Leetcode: Easy
--------------
44. Leetcode - 217: Contains Duplicate (Set) ✅
45. Leetcode: Valid Anagram (Counter, sort, hashmap approaches)
46. Leetcode: Two Sum (HashMap)
47. Leetcode: Valid Parentheses (Stack)
48. Leetcode: Valid Palindrome (Two pointers with alphanum validation)

Leetcode: Medium
----------------
49. Leetcode - 242: Group Anagram ✅
50. Leetcode - 128: Consecutive Sequence ✅
'''

# Basic programming: Easy
# ------------------------
# Topic: Variables and Data Types
# -------------------------------
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

# Topic: Lists/Arrarys
# ---------------------
#5. Print sum of elements in a list - Using for loop

arr = [10, 20, 30, 40, 50]
total = 0

for i in arr:
    total = total + i

print(sum)

#5a. Print sum of elements in a list - Using for loop and range function

arr = [10, 20, 30, 40, 50]
total = 0

for i in range(len(arr)):
    total = total + arr[i]

print(sum)

#5b. Print sum of elements in a list - Using built in sum() method

arr = [10, 20, 30, 40, 50]
print(sum(arr))

#6. Find Maximum & Minimum Element in an Array - Using for loop

arr = [10, 50, 200, 40, 3]
max = arr[0]
min = arr[0]

for i in arr:
    if i > max:
        max = i
    if i < min:
        min = i

print(f'The max value is {max}')
print(f'The min value is {min}')

#6a. Find Maximum & Minimum Element in an Array - Using for loop and range function , range function print indices, compare with index

arr = [10, 50, 200, 40, 3]
max = arr[0]
min = arr[0]

for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]

print(f'The max value is {max}')
print(f'The min value is {min}')

#7. Find The index of Maximum & Minimum Element in an Array - list[i] = element, i = array index

list = [10, 20, 13, 2, 200, 19]

max_index = 0
min_index = 0

for i in range(len(list)):
    if list[i] > list[max_index]:
        max_index = i
    if list[i] < list[min_index]:
        min_index = i

print(f'The index of the maximum number is: {max_index}')
print('The index of the minimum number is:', min_index)

#8. Find the length of a list/Array - Using built in len() method

arr = [10, 300, 20, 400, 50, 70]
print(len(arr))

#8a. Find the length of a list/Array - Using for loop

arr = [10, 300, 20, 400, 50, 70]
count = 0

for i in arr:
    count += 1

print('The total number of elements in the list is', count)

#8b. Find the length of a list/Array - when list is created by user

userList = input("Enter the numbers separated by space: ")
total = userList.split()
print(len(total))

#9. Count specific word occurrences

str = "my name is sunny giving interview sunny knows python"
count = 0
count1 = 0

list = str.split()

# Iterate through every element
for i in list:
    if i == 'sunny':
        count += 1

#Iterate though indices
for i in range(len(list)):
    if list[i] == 'sunny':
        count1 += 1

print(count)
print(count1)

#10. Swap first/last or any two elements in a list

arr = [12, 35, 9, 56, 24]

print(arr[0])
print(arr[-1])

arr[0], arr[-1] = arr[-1], arr[0]

print(arr[0])
print(arr[-1])

#11.  Swap any two elements of a list:

arr = [12, 35, 9, 56, 24]
print(arr[1])
print(arr[3])

# swap position 2 with 4
arr[1], arr[3] = arr[3], arr[1]
print(arr[1])
print(arr[3])

#12. Remove the duplicate occurrence of words in a string and return a list:

input_str = input("Enter words separated by spaces: ")

uniqueWords = set(input_str.split())

print(list(uniqueWords))

#13. Remove the duplicate words from a string and return a string:

input_str = input("Enter words separated by spaces: ")
print(input_str)
newStr = set(input_str.split())
print(newStr)
print(" ".join(newStr))

#14. Search an Element from a list - Using for loop

myList = [12, 222, 34, 4, 5]

num = int(input("What number do you want to find? "))

for i in myList:
    if num == i:
        print('Element found')
        break
else:
    print(f'Element not found')


#14a. Search an Element from a list - Using 'in' operator
myList = [12, 222, 34, 4, 5]

num = int(input("What number do you want to find? "))

if num in myList:
    print(f'Element found')
else:
    print(f'Element not found')

#15. Clear a list
myList = [1, 6, 3, 5, 3, 4]

print('Before clearing the list', myList)

myList.clear()

print('After clearing the list', myList)

#16. Reverse a list - Using slicing 

myList = [1, 6, 3, 5, 3, 4]
print('Before reversing', myList)
reversedList = myList[::-1]
print('After reversing', reversedList)

#16a. Reverse a list - Using reverse() method

myList = [1, 6, 3, 5, 3, 4]
print('Before reversing', myList)
myList.reverse()
print('After reversing', myList)







# Basic programming: Medium
# -------------------------
# Topic: Loop & Recursion
# -----------------------
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






# Leetcode: Easy
# --------------
# Topic: Arrays & Hashing
# -----------------------
#44. Contains Duplicate (Leetcode: 217) - Use set()

nums = [1,2,3,1]

def containDuplicate(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(containDuplicate(nums))



# Leetcode: Medium
# ----------------
# Topic: Arrays & Hashing
# -----------------------
#49. Group Anagrams (Leetcode: 242) - Use dict, ord(), array of 26 characters

from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list)   # creates an empty list as a default value, no need to create a key

def validAnagram(strs):
    for s in strs:
        count = [0] * 26

        for c in s:
            count[ord(c) - ord("a")] +=1  # Map 'a' - 'z' to idex 0 - 25

        res[tuple(count)].append(s)

    return list(res.values())

print(validAnagram(strs))

#50. Longest Consecutive Sequence (Leetcode: 128) - Use set(), check left number

nums = [100,4,200,1,3,2,5]
hashSet = set(nums)

def longestConsecutiveSequence(nums):
    longest = 0
    for n in nums:
        if (n-1) not in hashSet:  # check if the left value is present in the set 
            length = 1
        while (n+length) in hashSet:
            length += 1
        longest = max(length, longest)
    return longest

print(longestConsecutiveSequence(nums))