# 1. Write a program to find the transpose of a matrix.

# X = [[1, 3], [4,5], [7, 9]]

# result = [0, 0, 0], [0, 0, 0]

# for i in range (len (X)):

#               for j in range (len (X[0])):

#                              result [j][i] = X [i][j]

# for r in result:

#               print (r)



# 2. Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

# my_str= "python is AWESOME."
# capitalized_string = my_str.capitalize()
# print(capitalized_string)



# 3. Write a program to implement all built-in methods of list.

# 	Method	  Description

# 1	append()  Used for appending and adding elements to the end of the List. 
# 2	copy()	  It returns a shallow copy of a list
# 3	clear()	  This method is used for removing all items from the list. 
# 4	count()	  These methods count the element.
# 5	extend()  Adds each element of the iterable to the end of the List.
# 6	index()	  Returns the lowest index where the element appears. 
# 7	insert()  Inserts a given element at a given index in a list. 
# 8	pop()	  Removes and returns the last value from the List or the given index value.
# 9	remove()  Removes a given object from the List. 
# 10reverse() Reverses objects of the List in place.
# 11sort()	  Sort a List in ascending, descending, or user-defined order,
# 12min()	  Calculates the minimum of all the elements of the List,
# 13max()	  Calculates the maximum of all the elements of the List.



# 4. Write a program to read dictionary values through keyboard and merge two dictionaries.

# dict_1 = {1: 'a', 2: 'b'}
# dict_2 = {2: 'c', 3: 'd'}
# print({**dict_1, **dict_2})



# 5.Write a program to demonstrate all built-in methods of dictionary.

# Functions Name     Descriptions

# clear()            Removes all items from the dictionary
# copy()             Returns a shallow copy of the dictionary
# fromkeys()         Creates a dictionary from the given sequence
# get()              Returns the value for the given key
# items()            Return the list with all dictionary keys with values
# keys()             Returns a view object that displays a list of all the keys in the dictionary in order of insertion
# pop()              Returns and removes the element with the given key
# popitem()          Returns and removes the key-value pair from the dictionary
# setdefault()       Returns the value of a key if the key is in the dictionary else inserts the key with a value to the dictionary
# values()           Updates the dictionary with the elements from another dictionary
# update()           Returns a list of all the values available in a given dictionary



# 6. Write a program to find the sum of all the elements in a list.
	
# def sumlist(list):
#     sum=0
#     for i in range(len(list)):
#         sum = sum+list[i]
#     return sum
# list = [10, 9, 7, 5]
# print(list)
# print("sum of list: ",sumlist(list))



# 7. With a given integral number n, write a program to generate a dictionary that contains(i,i*i) such that i is an integral number between 1 and n. And then the program should print the dictionary.

# n=int(input("type the number "))
# d = dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d) 



# 8. Write a program that accepts a sentence and calculate the number of letters & digits

# num = 3452
# count = 0

# while num != 0:
#     num //= 10
#     count += 1

# print("Number of digits: " + str(count))



# 9. Write a program to implement filter(), map() and reduce() .

# def newfunc(a):
    # return a*a
# x=map(newfunc,(1,2,3,4))
# print(x)
# print(set(x))



# 10. Write a program to implement List Comprehension .

# fruits = ["apple", "banana", "cherry", "grapes", "mango"]
# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist) 



# 11. Write a program to implement Dictionary Comprehension .

# my_dict = dict()
# for num in range(1, 11):
#     my_dict[num] = num*num
# print(my_dict)



# 12. Write a program to find the largest and smallest element from a list.

# mylist = []
# number = int(input('How many elements to put in List: '))
# for n in range(number):
#     element = int(input('Enter element '))
#     mylist.append(element)
# print("Maximum element in the list is :", max(mylist))
# print("Minimum element in the list is :", min(mylist))



# 13. Write a Python program to print the numbers of a specified list after removing even numbers from it. 

# list = [11, 22, 33, 44, 55]
# print("Original list:")
# print(list)
# for i in list:
#     if i % 2 == 0:
#         list.remove(i)
# print("List after removing even numbers:")
# print(list)



# 14. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30

# def printValues():
# 	l = list()
# 	for i in range(1,30):
# 		l.append(i**2)
# 	print(l[:5])
# 	print(l[-5:])
# printValues()



# 15. Write a Python program to insert a given string at the beginning of all items in a list. 

# num = [1,2,3,4]
# print(['geeks{0}'.format(i) for i in  num])



# 16.  Write a Python program to iterate over two lists simultaneously.

# list_1 = [1, 2, 3, 4]
# list_2 = ['a', 'b', 'c']

# for i, j in zip(list_1, list_2):
#     print(i, j)



# 17.  Write a Python program to add a key to a dictionary.

# d = {0:10, 1:20}
# print(d)
# d.update({2:30})
# print(d)



# 18. Write a Python script to concatenate following dictionaries to create a new one.

# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3): dic4.update(d)
# print(dic4)



# 19. Write a Python program to iterate over dictionaries using for loops.

# dt = {'a': 'apple', 'b': 'cherry', 'c': 'banana'}
# for key, value in dt.items():
#     print(key, value)



# 20. Write a Python program to sum all the items in a dictionary.

# my_dict = {'data1':100,'data2':200,'data3':300}
# print(sum(my_dict.values()))



# 21.  Create a dictionary to hold information about pets. Each key is an animal's name, and each value is the kind of animal.Eg : {'Dog':'Willie'}

    # Put at least 3 key-value pairs in your dictionary.
    # Use a for loop to print out a series of statements such as "Willie is a dog."

# pet1={"Name":"Willie","Type":"Dog","Colour":"White","Nickname":"Willie","Owner":"Kurt"}
# for key,value in pet1.items():
#     print(f'{key}:{value}')

# pet2={"Name":"Jimbru","Type":"Cat","Colour":"White","Nickname":"Jimbru","Owner":"Vivanya"}
# for key,value in pet2.items():
#     print(f'{key}:{value}')

# pet3={"Name":"Ammu","Type":"Cow","Colour":"White","Nickname":"Ammu","Owner":"Vrinda"}
# for key,value in pet3.items():
#     print(f'{key}:{value}')


# 22. Write a python function to create and return a new dictionary from the given dictionary (subject: mark).

# Create a new dictionary with subject having marks more than 50.

# marks = {English: 40,'Maths': 60, 'Hindi: 30,'Chemistry': 46,'Physics': 70}

# def markdict(orginal_dict):
#     passed_subject={}
#     for subject,mark in orginal_dict.items():
#         if mark>50:
#             passed_subject[subject]=mark
#     return passed_subject
# sample_dict={"English": 40,"Maths": 60, "Hindi": 30,"Chemistry": 46,"Physics": 70}
# passed_subject_dict=markdict(sample_dict)
# print(passed_subject_dict)



# 23. Write a python function which accepts a sentence and finds the number of letters and digits in the sentence.

# It should return a dictionary in which the key should be letter count and value should be digit count. Ignore the spaces or any other special character in the sentence.

# str_1=input("input a string")
# d=a=0
# for i in str_1:
#     if i.isdigit():
#         d=d+1
#     elif i.isalpha():
#         a=a+1
#     else:
#         pass
# print("letters",a)
# print("digital",d)



#  24. Write a Python function which generates and returns a dictionary where the keys are numbers between 1 and n (both inclusive) and the values are square of keys.

# d=dict()
# n=43
# for i in range(1,n+1):
#     d[i]=i**2
# print(d)
