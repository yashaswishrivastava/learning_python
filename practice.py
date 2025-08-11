#To calculate salary of an employee given his basic pay (take as input from user). Calculate gross salary of employee. 
#Let HRA be 10 % of basic pay and TA be 5% of
#basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary payable after deductions.

basicpay = float(input("\nEnter the total salary"))

hra = 0.10* basicpay
print("The HRA is: ",hra)
ta = 0.05* basicpay
print("\nThe TA is: ",ta)

gross_salary = hra + ta + basicpay
print("\nThe gross salary is: ",gross_salary)

proffesional_tax = 0.02* gross_salary
print("\nThe proffesional tax is: ",proffesional_tax)

net_salary = gross_salary - proffesional_tax
print("\nThe net salary of the employee is: ", net_salary)

#To accept an object mass in kilograms and velocity in meters per second and display its
#momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is its velocity.

mass = float(input("Enter the mass: "))

velocity = float(input("\nEnter the velocity of the object: "))

momentum  = mass * velocity 
print("the value of enery is: ",momentum)

#To accept N numbers from user. Compute and display maximum in list, minimum in list, sum and average of number.

max_list = [2,4,3,5,7,6,9,8,10,23,42,64,53,87,61,32,48]
min_list = [2,4,8,9,6,1,3,5,7]
print(len(max_list))
print(len(min_list))

sum_list = len(max_list) + len(min_list)
average =  (len(max_list) + len(min_list))/2

print("the sum of lists is: ", sum_list)
print("The average sum of lists is: ", average)

#To accept student’s five courses marks and compute his/her result. Student is passing if he/she scores marks equal to and above 40 in
#each course. If student scores aggregate greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the
#grade if first division. If aggregate is 50>= and <60, then the grade is second division. If aggregate is 40>= and <50,
#then the grade is third division.

marks = float(input("Enter the marks of the student: "))
total_marks = int(input("Enter the total marks: "))

aggregate_marks = (marks/total_marks)*100
print("\nThe marks percentage obtained by the student is: ", aggregate_marks,"%")

if (aggregate_marks > 75):
    print("The student is passed with distinction")

    

elif(aggregate_marks >= 60):
    print("The student is passed with first division")

   

elif(aggregate_marks >= 50):
    print("The student is passed with second division")
   

elif(aggregate_marks >= 40):
    print("The student is passed with third division")
   
else:
    print("congratulations you failed")


#To check whether input number is Armstrong number or not. An Armstrong number is an integer with three digits 
#such that the sum of the cubes of its digits is equal to the number itself. Ex. 371.





#To simulate simple calculator that performs basic tasks such as addition, subtraction, multiplication and division with special operations
#like computing xy and x!.

num1 = float(input("Enter the number"))
num2 = float(input("enter the number"))

cal = input("how do you want to calculate?")

if cal == "+":
    print(num1 + num2)
elif cal == "-":
    print(num1-num2)
elif cal == "*":
    print(num1*num2)
elif cal == "/":
    print(num1/num2)
else:
    print("sorry im not that of a good coder and also fuck you")


#To accept the number and Compute 
#a) square root of number, b) Square of number, c) Cube of number d) check for prime, d) factorial of number e) prime factors


import math

num = float(input("enter the number1: "))


squareroot = math.sqrt(num)
print(squareroot)

#another way to write the code for the same

num = float(input("enter the number1: "))


squareroot = num**0.5
print(squareroot)

#square of the num

num = float(input("enter the number1: "))
square = num**2
print(square)

#cube of the number

num = float(input("enter the number1: "))
cube = num**3
print(cube)

#check for prime
num = int(input("Enter the number: "))


if num > 1:
    # Check if number has any factor other than 1 and itself
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


#factorial of the number

num = int(input("Enter the number: "))
fact = 1
for i in range( 1, num + 1):
    fact = fact * i

print("factorial of the num is: ",fact)

#another method for factorial

import math

num = int(input("enter the number: "))
fact = math.factorial(num)
print("The factorial of the number is : ",fact)

#prime factors

num = num = int(input("enter the number: "))

i = 2

while i <= num:
    if num % i == 0:
        print(i, end=" ")
        num = num // i  
    else:
        i += 1
print(" are the prime factors of the number ", i)

#To accept two numbers from user and compute smallest divisor and Greatest Common
#Divisor of these two numbers.

#smallest divisor
num = int(input("Enter the number1: "))
for i in range (2, num +1):
    if num % i == 0:
        print("the smallest divisor is: ",i)
        break
    
#for greatest comman factor

num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

while num2 != 0:
    num1, num2 = num2, num1 % num2
    print("The gcd is: ",num1)
    break

#using math import    

import math
num1 = int(input("Enter the number1: "))
num2 = int(input("Enter the number2: "))

ans = math.gcd(num1,num2)
print(ans)

#reverse the number

num = list(map(int, input("Enter elements separated by space: ").split()))
num.sort(reverse=True)
print(num)

#convert the binary into decimal

binary = input("enter the binary number: ")

decimal = int(binary,2)

print("the decimal of the binary number is: ", decimal)

#generate pseudo random numbers

import random

num = random.randit(1,100)
print(num)

#To accept list of N integers and partition list into two sub lists even and odd numbers.

#mylist = list(map(int, input("enter the seperated by space: ").split()))

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter the number: "))
    numbers.append(num)
    
evenlist = []
oddlist = []

for num in numbers:
    if num % 2 == 0:
        evenlist.append(num)
    else:
        oddlist.append(num)

print("Even numbers: ", evenlist)
print("Odd numbers: ", oddlist)

#To accept the number of terms a finds the sum of sine series.

import math 

x = float(input("enter the angle in radians: "))
n = int(input("enter the number of terms: "))

sine_sum = 0
sign = 1
power = 1

for i in range (n):
    term = sign * (x ** power) / math.factorial(power)
    sine_sum += term
    power += 2
    sign *= -1

print("Sum of the sine series: ", sine_sum)

#Write a python program that accepts a string from user and perform following string 
#operations- i.	Calculate length of string ii.	String reversal iii. Equality check of two
#strings iii. Check palindrome ii.  Check substring


string = input("Enter the string: ")
print("The length of the string is: ",len(string))
print("The reversed string is: ",(string[::-1]))

#equality of 2 strings

string1 = input("enter the string 1: ")
string2 = input("enter the string 2: ")

length1 = (len(string1))
length2 = (len(string2))

if (length1 == length2):
    print("The strings are equal.")
else:
    print("The strings are not equal.") 

#copystring = string.copy()
rev = string[::-1]

if (string == rev):
    print("The string is palindrome.")
else:
    print("The string is not palindrome.")


#Control Structures
#1️⃣ Write a program to input a number and check if it is positive, negative, or zero.
#2️⃣ Write a program to check if a number is prime or not using a 
#loop and decision-making structures.
#3️⃣ Write a program to find the largest and smallest number among three user-input values.

#1
num = int(input("enter the number: "))

if (num == 0):
    print("the number is zero.")
elif(num >= 0):
    print("the number is positive number.")
elif(num <= 0):
    print("the number is negetive number.")
else:
    print("ERROR!!!")

#2

num = int(input("enter the number: "))
if num > 1:

    for i in range(2, num):
        if(num % i == 0):
            print("the number is prime.")
            break

        else:
            print("the number is not prime.")

#3

a = float(input("enter the  number: "))
b = float(input("enter the  number: "))
c = float(input("enter the  number: "))

largest = a
if b > largest:
    largest = b 
if c > largest:
    largest = c

smallest = a 
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c

print("the largest number:",largest)
print("the smallest number:",smallest)

#Data Structures (List, Dictionary, Tuple)
#4️⃣ Write a program to create a list of numbers and display the sum and average of the elements.
#5️⃣ Write a program to create a dictionary of 5 students with roll numbers as keys and marks as values. 
#Display students who scored more than 70 marks.
#6️⃣ Write a program to create a tuple of even numbers between 1 and 50 and display it.
#7️⃣ Write a program to accept names in a list and display them in alphabetical order.


#1

mylist = list(map(int,input("enter the element seperated by space: ").split()))
sum_elements = sum(mylist)
avg = sum(mylist) / len(mylist)
print(avg)

#2

students = {}

for i in range(5):
    roll_no = input("Enter roll number of student : ")
    marks = int(input("Enter marks for roll number: "))
    students[roll_no] = marks


print("\nStudents who scored more than 70 marks:")
for roll_no, marks in students.items():
    if marks > 70:
        print(f"Roll No: {roll_no}, Marks: {marks}")



#Functions, Scoping, Recursion, List Mutability
#8️⃣ Write a program to demonstrate the use of local and global variables in Python functions.
#9️⃣ Write a recursive program to find the nth term of a Fibonacci series.
#🔟 Write a program to pass a list to a function, modify it inside the function, and display the changes outside (demonstrating list mutability).

# Global variable
x = 10

def my_function():
    # Local variable
    y = 5
    global x  # Telling Python we want to use the global x
    x = x + 5
    print("Inside function:")
    print("Local variable y =", y)
    print("Global variable x =", x)

my_function()
print("\nOutside function:")
print("Global variable x =", x)


#2

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Example
n = int(input("Enter the term number for Fibonacci series: "))
print(f"The {n}th term is:", fibonacci(n))

#3

def modify_list(my_list):
    my_list.append(100)  # Modify the list by appending 100
    print("Inside function:", my_list)

# Original list
numbers = [1, 2, 3]
print("Before function call:", numbers)

# Passing list to function
modify_list(numbers)

print("After function call:", numbers)



try:
    age = int(input("Enter your age: "))
    assert age > 0
    print("Your age is:", age)

except AssertionError:
    print("Assertion Error: Age must be greater than 0!")




















