'''
Basic programming
-----------------
#1. Swap two numbers - Using Tuple ✅
#1a. Swap two numbers - Using a third variable ✅
#1b. Swap two numbers - Without using a third variable ✅
#2. Check if a number is prime number ✅
#2a. Check if a number is prime number - using math.sqrt() function, start range from 2 ✅
#3. Find factorial (non-recursion) ✅
#4. Fibonacci series (basic recursion) - Print Fibonacci Sequence: 0 1 1 2 3 5 ✅
#5. Print sum of elements in a list - Using for loop ✅
#5a. Print sum of elements in a list - Using for loop and range function ✅
#5b. Print sum of elements in a list - Using built in sum() method ✅
#6. Find Maximum & Minimum Element in an Array - Using for loop ✅
#6a. Find Maximum & Minimum Element in an Array - Using for loop and range function , range function print indices, compare with index ✅
#7. Find The index of Maximum & Minimum Element in an Array - list[i] = element, i = array index ✅
#8. Find the length of a list/Array - Using built in len() method ✅
#8a. Find the length of a list/Array - Using for loop ✅
#8b. Find the length of a list/Array - when list is created by user ✅
#9. Count specific word occurrences - Iterate through every element & indices ✅
#10. Swap first/last or any two elements in a list ✅
#11. Swap any two elements of a list ✅
#12. Remove the duplicate occurrence of words in a string and return a list ✅
#13. Remove the duplicate words from a string and return a string ✅
#14. Search an Element from a list - Using for loop ✅
#14a. Search an Element from a list - Using 'in' operator ✅
#15. Clear a list ✅
#16. Reverse a list - Using slicing ✅
#16a. Reverse a list - Using reverse() method ✅
#17. Clone/copy a list (5 approaches) - Using slicing [:] or [start:end:step] ✅
#17a. Clone/copy a list (5 approaches) - Using copy() ✅
#17b. Clone/copy a list (5 approaches) - Using list() ✅
#17c. Clone/copy a list (5 approaches) - Using extend(), newList.extend(oldList) ✅
#17d. Clone/copy a list (5 approaches) - Using list comprehension ✅
#18. Count occurrences of an element(number) in a list ✅
#19. Multiply elements of a list - Using numpy library and prod method ✅
#19a. Multiply elements of a list - Using for loop and without range function ✅
#19b. Multiply elements of a list - Using for loop and with range function ✅
#20. 2nd largest/smallest element - sort() is first ✅
#21. Check palindrome (word/string) ✅
#22. Reverse words in a string ✅
#23. Substring search (and frequency) ✅
#24. Find the length of String - Use len() method ✅
#24a. Find the length of String - Use for loop ✅
#25. Sum of all Odd numbers ✅
#26. First repeating character in a string - break as soon as the first character is found ✅
#26a. All repeating character in a string - print out a list/tuple etc ✅
#27. FizzBuzz - Print Fizz if it's divisible by 3, print Buzz if it's divisible by 5, print FizzBuzz if it's divisible by both 3 and 5 ✅
#28. Reverse a number - Using while loop ✅
#29. Add the first element with last element of two distinct list - list1[i] + list2[len(list2)-i-1] ✅
#30. Factorial using recursion ✅
#31. Remove duplicate words and return a string ✅
#31a. Remove duplicate words and return a list ✅
#32. Check for special characters using regex - Using re.search() ✅
#32a. Check for special characters using regex - Using re.compile() ✅
#33. Check for URLs in strings using regex - Using http://urlregex.com ✅
#33a. Check for URLs in strings using regex - Using custom regex r'https?://\S+' ✅
#34. Find the second largest/smallest element in a descending order list - sort(reverse=True) ✅
#35. Find the number of repeating substring ✅
#36. Sum of all Even numbers ✅
=================================================================
#38. LRU Cache Implementation
     collections.OrderedDict or Custom LinkedList + HashMap approach.
#39. Multithreading in Python (threading module)
     Write a program that starts multiple threads to compute parts of a task.
#40. Producer-Consumer Problem using Queues
#41. Decorator Functions
     Implement a timing/decorator to log function performance.
#42. Using functools.reduce() and map() on a real problem
#43. Recursive Backtracking
     E.g. generating permutations, solving N-Queens.
#44. Custom Exception Handling
     Define custom errors for test validations.
#45. Use unittest or pytest
     Write end-to-end test for a Python module with mocking.
#46. Parsing JSON / XML / API response
     Useful for SDET testing pipelines.
#47. Writing Parameterized Tests with Pytest
#48. Database interaction using sqlite3

Leetcode: Arrays & Hashing : Easy
--------------------------------
1929. Concatenation of Array ✅
217. Contains Duplicate ✅
242. Valid Anagram ✅
1. Two Sum ✅
14. Longest Common Prefix - Compare the first string elements with the rest in the strs ✅
27. Remove Element - k is the number of element that is not equal to val, nums[k] = nums[i] ✅

Leetcode: Arrays & Hashing : Medium
----------------------------------
49. Group Anagrams - Use dict, ord(), array of 26 characters ✅
128. Longest Consecutive Sequence ✅
122. Best Time to Buy and Sell Stock II ✅

Leetcode: Two Pointers : Easy
-----------------------------
344. Reverse String ✅
125. Valid Palindrome ✅
680. Valid Palindrome II ✅
1768. Merge Strings Alternately ✅
88. Merge Sorted Array ✅

Leetcode: Sliding Window : Easy
-------------------------------
219. Contains Duplicate II ✅
121. Best Time to Buy and Sell Stock ✅

Leetcode: Sliding Window : Medium
----------------------------------
3. Longest Substring Without Repeating Characters ✅

Leetcode: Stack : Easy
----------------------
20. Valid Parentheses ✅

Leetcode Roadmap
----------------
📁 Arrays & Hashing: Easy
-------------------------
217. Contains Duplicate ✅
242. Valid Anagram ✅
1. Two Sum (Very Common) ✅
88. Merge Sorted Array ✅
26. Remove Duplicates from Sorted Array
283. Move Zeroes
169. Majority Element
448. Find All Numbers Disappeared in an Array
349. Intersection of Two Arrays
350. Intersection of Two Arrays II
706. Design HashMap (Practical for Frameworks)

📁 Arrays & Hashing: Medium
---------------------------
36. Valid Sudoku (Excellent for Complex Validation)
347. Top K Frequent Elements
238. Product of Array Except Self
56. Merge Intervals (Great for Test Coverage Analysis)
15. 3Sum

🔁 Two Pointers, Sorting & Intervals: Easy
------------------------------------------
121. Best Time to Buy and Sell Stock ✅
202. Happy Number
141. Linked List Cycle (Memory Leak Concepts)

🔁 Two Pointers, Sorting & Intervals: Medium
--------------------------------------------
11. Container With Most Water
253. Meeting Rooms II (Good for Scheduling Tests)
215. Kth Largest Element in an Array

🔤 Strings & Sliding Window: Easy
--------------------------------
344. Reverse String ✅
387. First Unique Character in a String
125. Valid Palindrome (Very Common) ✅
20. Valid Parentheses (Very Common) ✅
58. Length of Last Word
409. Longest Palindrome
929. Unique Email Addresses (Great for Testing Scenarios)
290. Word Pattern (Good for API Testing)
205. Isomorphic Strings
383. Ransom Note

🔤 Strings & Sliding Window: Medium
-----------------------------------
3. Longest Substring Without Repeating Characters ✅
49. Group Anagrams ✅
151. Reverse Words in a String
394. Decode String (Good for Parsing Tests)
8. String to Integer (atoi) (Excellent for Edge Case Testing!)

🗂 Stacks & Queues: Easy
------------------------
232. Implement Queue using Stacks
225. Implement Stack using Queues
155. Min Stack

🗂 Stacks & Queues: Medium
--------------------------
739. Daily Temperatures

🔁 Recursion & Backtracking (Basic): Easy
-----------------------------------------
104. Maximum Depth of Binary Tree
110. Balanced Binary Tree
206. Reverse Linked List
21. Merge Two Sorted Lists

🔁 Recursion & Backtracking (Basic): Medium
-------------------------------------------
78. Subsets (Combinatorial Testing Concepts)
46. Permutations

🔍 Binary Search & Matrix: Easy
-------------------------------
278. First Bad Version (Classic QA Problem!)
704. Binary Search
74. Search a 2D Matrix

🔍 Binary Search & Matrix: Medium
---------------------------------
33. Search in Rotated Sorted Array
54. Spiral Matrix (2D Test Data)
973. K Closest Points to Origin

🌳 Binary Tree & Graph (Optional Basics): Medium
------------------------------------------------
102. Binary Tree Level Order Traversal (Hierarchical Data Testing)
572. Subtree of Another Tree
617. Merge Two Binary Trees

➕ Bit Manipulation & Math: Easy
--------------------------------
190. Reverse Bits
191. Number of 1 Bits
9. Palindrome Number
13. Roman to Integer

Longterm Roadmap for Leetcode
-----------------------------
📁 Arrays & Hashing: Easy
-------------------------
1. Find Missing Number / Missing Ranges (#268 / #163)
2. Longest Consecutive Sequence (#128) ✅

📁 Arrays & Hashing: Medium
---------------------------
3. Subarray Sum Equals K (#560)
4. Top K Frequent Words (#692)
5. Longest Subarray with Equal 0s and 1s (#525)
6. Maximum Size Subarray Sum Equals K (variation of #560)

🔤 Strings & Sliding Window: Easy
---------------------------------
7. Valid Anagram (#242) ✅
8. Implement strStr() (#28)
9. Count and Say (#38)

🔤 Strings & Sliding Window: Medium
-----------------------------------
10. Minimum Window Substring (#76)
11. Longest Repeating Character Replacement (#424)
12. Longest Palindromic Substring (#5)
13. Find All Anagrams in a String (#438)

🔁 Two Pointers, Sorting & Intervals: Easy
------------------------------------------
14. 2Sum II - Input array sorted (#167)
15. Valid Palindrome II (#680) ✅

🔁 Two Pointers, Sorting & Intervals: Medium
--------------------------------------------
16. Sort Colors (Dutch Flag) (#75)
17. 3Sum Closest (#16)

🗂 Stacks & Queues: Medium
--------------------------
18. Next Greater Element (#496)
19. Sliding Window Maximum (#239)
20. Evaluate Reverse Polish Notation (#150)

🔁 Recursion & Backtracking (Basic): Easy
-----------------------------------------
21. Fibonacci Number (#509)
22. Factorial recursion or Sum of Digits (not official LeetCode)
23. Sum of digits (custom but base recursion problem)

🔁 Recursion & Backtracking (Basic): Medium
-------------------------------------------
24. Generate Parentheses (#22)
25. Combinations (#77)
26. Word Search (#79)

🔍 Binary Search & Matrix: Easy
-------------------------------
27. Search Insert Position (#35)
28. Guess Number Higher or Lower (#374)
29. Find First and Last Position of Element (#34)

🔍 Binary Search & Matrix: Medium
---------------------------------
30. Kth Smallest Element in a Sorted Matrix (#378)
31. Divide Two Integers (#29)

🌳 Binary Tree & Graph (Optional mostly): Medium
------------------------------------------------
32. Same Tree / Symmetric Tree (#100 / #101)
33. Validate Binary Search Tree (#98)

🌳 Binary Tree & Graph (Optional extra senior topics): Medium
-------------------------------------------------------------
34. Lowest Common Ancestor (#236)
35. Course Schedule (Graph) (#207)

➕ Bit Manipulation & Math: Easy
--------------------------------
36. Single Number (#136)
37. Hamming Distance (#461)
38. Power of Two (#231)

➕ Bit Manipulation & Math: Medium
----------------------------------
39. Count Bits (#338)
40. Bits manipulation variants (e.g. #190 or #137)
'''

# Basic programming
# -----------------
#1. Swap two numbers - Using Tuple
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

print('First number: ', num1)
print('Second number: ', num2)

num1, num2 = num2, num1

print('After swapping')
print('First number: ', num1)
print('Second number: ', num2)

#1a. Swap two numbers - Using a third variable
num1 = int(input('Enter the first number: '))
num2 = int(input('Enter the second number: '))

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

#2a. Check if a number is prime number - using math.sqrt() function, start range from 2
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

#9. Count specific word occurrences - Iterate through every element & indices
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

#11. Swap any two elements of a list
arr = [12, 35, 9, 56, 24]
print(arr[1])
print(arr[3])

# swap position 2 with 4
arr[1], arr[3] = arr[3], arr[1]
print(arr[1])
print(arr[3])

#12. Remove the duplicate occurrence of words in a string and return a list
input_str = input("Enter words separated by spaces: ")
uniqueWords = set(input_str.split())
print(list(uniqueWords))

#13. Remove the duplicate words from a string and return a string
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

#17. Clone/copy a list (5 approaches) - Using slicing [:] or [start:end:step]
myList = [4, 8, 2, 10, 15, 18]
print(myList)

#newList = myList[0:len(myList)] 
newList = myList[:]
print(newList)

#17a. Clone/copy a list (5 approaches) - Using copy()
myList = [4, 8, 2, 10, 15, 18]
print(myList)

newList = myList.copy()
print(newList)

#17b. Clone/copy a list (5 approaches) - Using list()
myList = [4, 8, 2, 10, 15, 18]
print(myList)

newList = list(myList)
print(newList)

#17c. Clone/copy a list (5 approaches) - Using extend(), newList.extend(oldList)
myList = [4, 8, 2, 10, 15, 18]
print(myList)

newList = []
newList.extend(myList)
print(newList)

#17d. Clone/copy a list (5 approaches) - Using list comprehension
myList = [4, 8, 2, 10, 15, 18]
print(myList)

newList = [x for x in myList]
print(newList)

#18. Count occurrences of an element(number) in a list
myList = [15, 6, 7, 10, 12, 20, 10, 28, 10]
count = 0
element = int(input("Which number are you looking to find? "))

for i in myList:
    if i == element:
        count += 1

print(f'The number {element} occurs {count} number of times')

#19. Multiply elements of a list - Using numpy library and prod method
import numpy
myList = [3, 2, 4, 8]
result = numpy.prod(myList)
print(result)

#19a. Multiply elements of a list - Using for loop and without range function
myList = [3, 2, 4, 8]
count = 1

for i in myList:
    count = count * i

print(count)

#19b. Multiply elements of a list - Using for loop and with range function
myList = [3, 2, 4, 8]
count = 1

for i in range(len(myList)):
    count = count * myList[i]

print(count)

#20. 2nd largest/smallest element - sort() is first
myList = [70, 11, 20, 4, 100]
myList.sort()
print(myList[-2])

#21. Check palindrome (word/string)
s = "madam madam"

def isPalindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(isPalindrome(s))

#22. Reverse words in a string
string = input("Enter the words of string seperated by comma: ")
print(string)
newString = string.split(" ")
reverse_word = " ".join(newString[::-1])
print("The reverses string is: ", reverse_word)

#23. Substring search (and frequency)
string = 'welcome to python programming'
subString = 'python'
if subString in string:
    print('Substring is present')
else:
    print('Substring is not present')

#24. Find the length of String - Use len() method
string = "Welcome"
print(len(string))

#24a. Find the length of String - Use for loop
string = "Welcome"
count = 0

for i in string:
    count += 1

print(count)

#25. Sum of all Odd numbers
num = int(input("Enter the last number: "))
total = 0

for i in range(1, num+1):
    if i % 2 != 0:
        total = total + i

print(total)

#26. First repeating character in a string - break as soon as the first character is found
s = "aabcde"
repeatedCharacter = set()

for c in s:
    if s.count(c) > 1:
        repeatedCharacter.add(c)
        break

if len(repeatedCharacter) > 0:
    print('The first repeated character is', list(repeatedCharacter)[0])
else:
    print('There is no repeacting character')

#26a. All repeating character in a string - print out a list/tuple etc
str = input("Enter your string: ")
repeatedCharacter = set()

for ch in str:
    if (str.count(ch) > 1):
        repeatedCharacter.add(ch)

if len(repeatedCharacter) > 0:
    print("The repeated characters are: ", repeatedCharacter)
    print("The first repeated character is: ", list(repeatedCharacter))
else:
    print("There is no repeated character")

#27. FizzBuzz - Print Fizz if it's divisible by 3, print Buzz if it's divisible by 5, print FizzBuzz if it's divisible by both 3 and 5
num = int(input("Enter a number: "))

for i in range(1, num+1):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0: 
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

#28. Reverse a number - Using while loop
num = int(input("Enter a number: "))
reverse_number = 0

while num > 0:
    remainder = num % 10
    reverse_number = (reverse_number * 10) + remainder
    num = num // 10

print(reverse_number)

#29. Add the first element with last element of two distinct list - list1[i] + list2[len(list2)-i-1]
listOne = [1, 2, 3, 4, 5]
listTwo = [6, 7, 8, 9, 10]
newList = []

for i in range(len(listOne)):
    newList.append(listOne[i] + listTwo[len(listTwo) - i - 1])

print(newList)

#30. Factorial using recursion
num = int(input("Enter a number: "))

def factorial(num):
    if num < 0:
        return f"no factorial for {num}"
    elif num == 0 or num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(num))

#31. Remove duplicate words and return a string
string = input("Enter the words of string seperated by comma: ")
print(string)
newString = set(string.split())
print(newString)

#31a. Remove duplicate words and return a list
string = input("Enter the words of string seperated by comma: ")
print(string)
newString = set(string.split())
print(list(newString))

#32. Check for special characters using regex - Using re.search()
import re

string = "welcome@@2To%%Python**Programming@!!^%%@$"

if re.search(r'[^a-zA-Z0-9]', string):
    print('Sring contains special character')
else:
    print('String does not contain any special character')

#32a. Check for special characters using regex - Using re.compile()
import re

string = "welcome@@2To%%Python**Programming@!!^%%@$"
regex = re.compile('[~!@#$%^&*]') 

if regex.search(string):
    print('Sring contains special character')
else:
    print('String does not contain any special character')

#33. Check for URLs in strings using regex - Using http://urlregex.com
import re
stringOne = "Im a blogger at http://www.sunnytestingtools.com/"
stringTwo = "My profile: https://sunnyonlinetrainings.com/about.html and MyBlog: http://www.sunnytestingtools.com"

urlOne = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', stringOne)
print(urlOne)

urlTwo = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', stringTwo)
print(urlTwo)

#33a. Check for URLs in strings using regex - Using custome regex r'https?://\S+'
import re
stringOne = "Im a blogger at http://www.sunnytestingtools.com/"
stringTwo = "My profile: https://sunnyonlinetrainings.com/about.html and MyBlog: http://www.sunnytestingtools.com"

urlOne = re.findall(r'https?://\S+', stringOne)
print(urlOne)

urlTwo = re.findall(r'https?://\S+', stringTwo)
print(urlTwo)

#34. Find the second largest/smallest element in a descending order list - sort(reverse=True)
list = [70, 11, 20, 4, 100]
print(list)
list.sort(reverse=True)
print(list)
print('The second largest element is ', list[1])
print('The second smalled element is ', list[-2])

#35. Find the number of repeating substring
string = 'welcome to python programming python'
newString = string.split()
subString = 'python'
count = 0

for i in newString:
    if i == subString:
        count += 1

print(f'The substring {subString} is present {count} times')

#36. Sum of all Even numbers
num = int(input("Enter the last number: "))
total = 0

for i in range(1, num+1):
    if i % 2 == 0:
        total = total + i

print(total)

# Leetcode: Arrays & Hashing : Easy
# ---------------------------------
#1929. Concatenation of Array - Nested for loop with append()
nums = [1,3,2,1]
ans = []
iteration = int(input('Enter the number of times you want to concatenate the array: '))

def concatenationOfArray(nums, x):
    for i in range(x):
        for i in nums:
            ans.append(i)

    return ans

print(concatenationOfArray(nums,iteration))

#217. Contains Duplicate - Use set()
nums = [1,2,3,1]

def containDuplicate(nums):
    hashset = set()
    for i in nums:
        if i in hashset:
            return True
        hashset.add(i)
    return False

print(containDuplicate(nums))

#242. Valid Anagram - Counter method
from collections import Counter
s = "anagram"
t = "nagaram"

def validAnagram(s, t):
    return Counter(s) == Counter(t)

print(validAnagram(s, t))

#242a. Valid Anagram - Sorted method
s = "anagram"
t = "nagaram"

def validAnagram(s, t):
    return sorted(s) == sorted(t)

print(validAnagram(s, t))

#242b. Valid Anagram - Using hasmap algorithm, use .get(key, default)
s = "anagram"
t = "nagaram"

def validAnagram(s, t):
    if len(s) != len(t):
        return False
    
    # create a hashmap/dictionary
    count = {} 

    # add all they keys and values into the hashmap
    for char in s:
        count[char] = count.get(char, 0) + 1

    # check the keys from string t with the hashmap and delete one key at a time
    for char in t:
        if char not in count:
            return False
        count[char] -= 1
        if count[char] < 0:
            return False
    
    return True

print(validAnagram(s, t))

#1. Two Sum - {value: index}, storing the value as the key and the index as the value
nums = [2,7,11,15]
target = 9

def twoSum(nums, target):
    prevMap = {}
    for index, number in enumerate(nums):
        diff = target - number
        if diff in prevMap:
            return prevMap[diff], index
        prevMap[number] = index

print(twoSum(nums, target))

#14. Longest Common Prefix - Compare the first string elements with the rest in the strs
strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
    res = ""
    for i in range(len(strs[0])):                   # i goes from 0 -> len(strs[0]) - 1
        for s in strs:                              # s is each string in strs
            if i == len(s) or s[i] != strs[0][i]:   # this particular string s is too short for index i, string is out of bound
                return res
        res += strs[0][i]
    
    return res

print(longestCommonPrefix(strs))

#27. Remove Element - k is the number of element that is not equal to val, nums[k] = nums[i]
nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

print(removeElement(nums, val))

# Leetcode: Arrays & Hashing : Medium
# ---------------------------------
#49. Group Anagrams - Use dict, ord(), array of 26 characters
from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]
res = defaultdict(list)   # creates an empty list as a default value, no need to create a key

def groupAnagram(strs):
    for s in strs:
        count = [0] * 26                    #create a list of 26 zeros
        for c in s:
            count[ord(c) - ord("a")] +=1    #map a to z to index 0 - 25, ord("c") - ord("a") = 99 - 97 = 2, 'c' maps to slot 2 in the count list
        res[tuple(count)].append(s)         #change the dictionary key to a tuple

    return list(res.values())

print(groupAnagram(strs))

#128. Longest Consecutive Sequence - Use set(), check left number
nums = [1,0,1,2]
hashSet = set(nums)

def longestConsecutiveSequence(nums):
    longest = 0
    length = 0
    for n in nums:
        #check if its the start of a sequence
        if (n - 1) not in hashSet:
            length = 1
        while (n + length) in hashSet:
            length += 1
        longest = max(longest, length)
    return longest

print(longestConsecutiveSequence(nums))

#122. Best Time to Buy and Sell Stock II
prices = [7,1,5,3,6,4]

def bestTimeBuySellTwo(prices):
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            profit += prices[i] - prices[i - 1]
    
    return profit

print(bestTimeBuySellTwo(prices))

# Leetcode: Two Pointers : Easy
# -----------------------------
#344. Reverse String - using Time: O(n) Space: O(1)
s = ["h","e","l","l","o"]

def reverseString(s):
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return s

print(reverseString(s))

#344a. Reverse String - Using Stack Time:O(n) Space: O(n)
s = ["h","e","l","l","o"]

def reverseString(s):
    stack = []
    
    for c in s:
        stack.append(c)
    i = 0
    while stack:
        s[i] = stack.pop()
        i += 1
    
    return s

print(reverseString(s))

#125. Valid Palindrome - Two pointers with alphanum validation
s = "A man, a plan, a canal: Panama"

def alphaNum(s):
    return (ord('A') <= ord(s) <= ord('Z') or ord('a') <= ord(s) <= ord('z') or (ord('0') <= ord(s) <= ord('9')))

def isPalindrome(s):
    left, right = 0, len(s) - 1 
    while left < right:
        # Move left pointer until an alphanumeric character is found
        # not alphaNumber function skip over any non alphanumeric character
        while left < right and not alphaNum(s[left]):
            left += 1
        # Move right pointer until an alphanumeric character is found
        while right > left and not alphaNum(s[right]):
            right -= 1
        # Check if characters are not equal (ignoring case)
        if s[left].lower() != s[right].lower():
            return False
        # Move both pointers towards the center
        left += 1
        right -= 1

    return True

print(isPalindrome(s))

#125a. Valid Palindrome - Two pointers with alphanum validation
s = "A man, a plan, a canal: Panama"
def validPalindrome(s):
    newStr = ""
    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

print(validPalindrome(s))

#680. Valid Palindrome II
s = "racecarx"

def validPalindromeHelper(s, left, right):
    while left < right: 
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def validPalindromeTwo(s):
    left = 0
    right = len(s) - 1
    while left < right:
        return validPalindromeHelper(s, left + 1, right) or validPalindromeHelper(s, left, right - 1)
        left += 1
        right -= 1
    return True

print(validPalindromeTwo(s))

#1768. Merge Strings Alternately
word1 = "abc"
word2 = "pqr"

def mergeStringsAlternately(word1, word2):
    res = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        res.append(word2[j:])
        i += 1
        j += 1
    res.append(word1[i:])
    res.append(word2[j:])

    return "".join(res)

print(mergeStringsAlternately(word1, word2))

#88. Merge Sorted Array
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

def mergeSortedArray(nums1, m, nums2, n):
    # last index of nums1
    last = m + n -1
    # merge in revese order
    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1
        last -= 1
    # fill nums1 with leftover num2 element
    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1
    
    return nums1

print(mergeSortedArray(nums1, m, nums2, n))

# Leetcode: Sliding Window : Easy
# -------------------------------
#219. Contains Duplicate II
nums = [1,2,3,1]
k = 3

def containsDuplicateTwo(nums, k):
    window = set()
    l = 0

    for r in range(len(nums)):
        if r - l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])

    return False

print(containsDuplicateTwo(nums, k))

#121. Best Time to Buy and Sell Stock
prices = [7,1,5,3,6,4]

def bestTimeBuySell(prices):
    l, r = 0, 1
    maxP = 0
    while r < len(prices):
        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)
        else:
            l = r
        r += 1

    return maxP

print(bestTimeBuySell(prices))

# Leetcode: Sliding Window : Medium
# ----------------------------------
#3. Longest Substring Without Repeating Characters
s = "abcabcbb"

def longestSubstingWithoutReapeatingCharacters(s):
    window = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in window:
            window.remove(s[l])
            l += 1
        window.add(s[r])
        res = max(res, r - l + 1)

    return res

print(longestSubstingWithoutReapeatingCharacters(s))

# Leetcode: Stack : Easy
# ----------------------
#20. Valid Parentheses - stack (has elements), not stack (no elements)
s = "()"

def validParenthese(s):
    stack = []
    stackDict = { ")" : "(", "]" : "[", "}" : "{" }

    for c in s:
        if c in stackDict:
            if stack and stack[-1] == stackDict[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return not stack

print(validParenthese(s))