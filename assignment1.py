# 1. Write a program to check whether the entered number is postive or negative

# num=int(input("enter the number"))
# if num==0:
#     print("zero")
# elif num>0:
#     print("number is positive")
# else:
#     print("number is negative")



# 2. Write a program to  swap two variables.                   

                    
# x =int(input("Enter the first number"))

# y =int(input("Enter the second number"))

# z = x

# x = y

# y = z

# print ("The value of the first variable after swapping is:", x)

# print ("The value of the second variable after swapping is:", y)



# 3. Write a program to  Determine If Year Is Leap Year

# year=int(input("enter any year that is to be checked for leap year"))
# if(year % 4)==0:
#     if(year % 100)==0:
#         if(year % 400)==0:
#             print("the given year is a leap year")
#         else:
#             print("it is not a leap year")
#     else:
#         print("it is not a leap year")
# else:
#     print("is is not a leap year")



# 4. Write a program check whether the given number is odd or even.

# num = int (input ("Enter any number to test whether it is odd or even: "))

# if (num % 2) == 0:

#               print ("The number is even")

# else:

#               print ("The provided number is odd")


# 5.Write a program to print the fibonocci series.

# n=10
# num1=0
# num2=1
# next_number=num2
# count=1
# while count <=n:
#     print(next_number,end=" ")
#     count +=1
#     num1, num2=num2,next_number
#     next_number=num1+num2
# print()


# 6.Write a program to  generate following pyramid or triangle like  given below using for loop.

# a
# rows = int(input("Enter number of rows: "))

# for i in range(rows, 0, -1):
#     for j in range(0, i):
#         print("* ", end=" ")
    
#     print("\n")


# 7. Write a program to print the prime numbers between given interval.

# lwr=900
# upr=1000
# print("prime number between",lwr,"and",upr,"are:")
# for num in range(lwr,upr+1):
#     if num>1:
#         for a in range(2,num):
#             if(num%a)==0:
#                 break
#             else:
#                 print(num)


# 8. Write a program for Printing Odd numbers between 1 and 50 and calculate the sum of that numbers.

 
# start, end = 1, 50

# for num in range(start, end + 1):
#      if num % 2 != 0:
#         print(num, end = " ")


# 9. Write a program to find the factorial of the given number.

# n = int (input ("Enter a number: "))

# factorial = 1

# if n >= 1:

#               for i in range (1, n+1):

#                              factorial = factorial *i

# print ("Factorial of the given number is: ", factorial)


# 10.Write a program to Check if the given string  is Palindrome or not.

# my_str="python"
# my_str=my_str.casefold()
# rev_str=reversed(my_str)
# if list(my_str)==list(rev_str):
#     print("the string is a palindrom.")
# else:
#     print("the string is not a palindrom.")


# 12.Write a program to Display Multiplication Table

# num=int(input("enter a number:"))
# print("table of:")
# for a in range(1,11):
#     print(num,'x',a,'=',num*a)


# 13. Write a program to calculate the area and perimeter of a rectangle.

# l=int(input("Length : "))
# w=int(input("Width : "))
# area=l*w
# perimeter=2*(l+w)
# print("Area of Rectangle : ",area)
# print("Perimeter of Rectangle : ",perimeter)


# 14. Write a program to find the sum of n' Natural Numbers.
# num = 16

# if num < 0:
#    print("Enter a positive number")
# else:
#    sum = 0
#    # use while loop to iterate until zero
#    while(num > 0):
#        sum += num
#        num -= 1
#    print("The sum is", sum)


# 15.Write a program to find whether given no. is Armstrong or not.
# num = int(input("Enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** 3
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")
                


# 16. Write a program to find the largest among 3 numbers.
# num1 = 10
# num2 = 14
# num3 = 12
# if (num1 >= num2) and (num1 >= num3):
#    largest = num1
# elif (num2 >= num1) and (num2 >= num3):
#    largest = num2
# else:
#    largest = num3
# print("The largest number is", largest)


# 17. Write a program to remove all punctuations from given string.














# 18. Write a program to  Display Triangle as follow : 
# 1

# 2 2

# 3 3 3

# 4 4 4 4...

rows = 5
for i in range(rows):
    for j in range(i):
        print(i, end=' ')
    print('')


# 19. Write a program to count the no:of each vowel in a given string.