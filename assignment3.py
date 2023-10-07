# 1. Write a program to define a function that can accept an integer number as    input and print the "It is an even number" if the number is even, otherwise print "It is odd".

# num=int(input("Enter a number"))
# mod=num%2
# if mod >0:
#     print("This is an odd number.")
# else:
#     print("This is an even number.")



# 2. Write a program to define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# d=dict()
# for x in range(1,21):
#     d[x]=x**2
# print(d)  


# 3. Write a program to take a string as input and return a string with vowels removed.

# string = "vivanya"
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# result = ""
# for i in range(len(string)):
#     if string[i] not in vowels:
#         result = result + string[i]
# print("\nAfter removing Vowels: ", result)



# 4. Write a program to display Powers of 2  using Anonymous functions?(lambda,map).

# terms = 10
# result = list(map(lambda x: 2 ** x, range(terms)))
# print("The total terms are:",terms)
# for i in range(terms):
#    print("2 raised to power",i,"is",result[i])



# 5. Write a program to implement bubble-sort algorithm

# def bubbleSort(arr):
#     n = len(arr)
#     swapped = False
#     for i in range(n-1):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j + 1]:
#                 swapped = True
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         if not swapped:
#             return
# arr = [64, 34, 25, 12, 22, 11, 90]
# bubbleSort(arr)
# print("Sorted array is:")
# for i in range(len(arr)):
#     print("% d" % arr[i], end=" ")



# 6. Write a program to implement binary-search algorithm

# def binarySearch(array, x, low, high):
#     while low <= high:
#         mid = low + (high - low)//2
#         if array[mid] == x:
#             return mid
#         elif array[mid] < x:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return -1
# array = [3, 4, 5, 6, 7, 8, 9]
# x = 4
# result = binarySearch(array, x, 0, len(array)-1)
# if result != -1:
#     print("Element is present at index " + str(result))
# else:
#     print("Not found")



# 7. Write a program to take two list of same length as input and return a dictionary with one as keys and other as values.

# test_keys = ["vivanya", "swapna", "vrinda"]
# test_values = [1, 4, 5]
# print("Original key list is : " + str(test_keys))
# print("Original value list is : " + str(test_values))
# res = {}
# for key in test_keys:
#     for value in test_values:
#         res[key] = value
#         test_values.remove(value)
#         break
# print("Resultant dictionary is : " + str(res))



# 8. Write a program to print fibonocci series using recursion.

# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
# nterms = 10
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))



# 9. Write a program to find the factorial of a number using recursion.

# def recur_factorial(n):
#    if n == 1:
#        return n
#    else:
#        return n*recur_factorial(n-1)
# num = 7
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    print("The factorial of", num, "is", recur_factorial(num))



# 10. Program to implement concept of decorator to calculate the time needed to execute one or more function in a program.

# def my_decorator(func):
#     def wrapper_function(*args, **kwargs):
#         print("*"*10)
#         func(*args,  **kwargs)
#         print("*"*10)
#     return wrapper_function
# def say_hello():
#     print("Hello Geeks!")
# @my_decorator
# def say_bye():
#     print("Bye Geeks!")
# say_hello = my_decorator(say_hello)
# say_hello()
# say_bye()



# 11. Write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.(implement generator).

# def numgenerator(n):
#     for i in range(n+1):
#         if 1%5==0 and i%7==0:
#             yield i
# n=int(input("enter number"))
# values=[]
# for i in numgenerator(n):
#     values.append(str(i))
# print(",".join(values))



# 12. Write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.(implement generator).

# def my_generator(n):
#     value = 0
#     while value < n:
#         yield value
#         value += 1
# for value in my_generator(3):
#     print(value)



# 13. Write a program to implement Insertion-Sort algorithm in python.

# def insertionSort(array):
#     for step in range(1, len(array)):
#         key = array[step]
#         j = step - 1
#     while j >= 0 and key < array[j]:
#         array[j + 1] = array[j]
#         j = j - 1
#     array[j + 1] = key
# data = [9, 5, 1, 4, 3]
# insertionSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)



# 14. Program to implement Linear-Search Algorithm.

# def linearSearch(array, n, x):
#     for i in range(0, n):
#         if (array[i] == x):
#             return i
#     return -1
# array = [2, 4, 0, 1, 9]
# x = 1
# n = len(array)
# result = linearSearch(array, n, x)
# if(result == -1):
#     print("Element not found")
# else:
#     print("Element found at index: ", result)



# 15. Program to implement Selection-Sort Algorithm.

# def selectionSort(array, size):
#     for step in range(size):
#         min_idx = step
#         for i in range(step + 1, size):
#             if array[i] < array[min_idx]:
#                 min_idx = i
#     (array[step], array[min_idx]) = (array[min_idx], array[step])
# data = [-2, 45, 0, 11, -9]
# size = len(data)
# selectionSort(data, size)
# print('Sorted Array in Ascending Order:')
# print(data)



# 16. Write a Python program to find the second smallest number in a list using function.

# list = [] 
# n = int(input("Enter the number of elements: "))
# for i in range(1, n+1): 
#     elem = int(input("Enter the elements: ")) 
#     list.append(elem) 
# list.sort() 
# print("The sorted list: ", list) 
# print("The second smallest number of this list: ",list[1])