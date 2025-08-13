#print sum
a=4
b=9
sum=a+b
print(sum)

#types of operators
#1. Arithmetic operators + - * / % **
#2. Assignment operators = += -= *= /= %= **=
#3. Relational operators == != > < >= <=
#4. Logical operators not and or

#1.
a=16 
b=2

print(a+b) 
print(a-b)
print(a*b)
print(a/b)
print(a%b) 
print(a**b) #a^b 

#assignment operators
num = 10
num %= 5
print(num)

#logical operator

a=50
b=30
print(not False)
print(not(a>b))

val1 = False
val2 = True
print("AND operator: ", val1 and val2)
print("OR operator: ", (a==b) or (a>b))

#type conversion
a = float("3")
b = 4.25

print(type(a))
print(a+b)

a=3.14
a=str(a)

print(type(a))
print(a)

#input from user

name = input("enter your fucking name: ")
print("welcome", name)

#write a program to input 2 numbers and print their sum

num1 = int(input("Enter your number: "))
num2 = int(input("Enter your number: "))

sum = num1+num2
print("The sum of two numbers: ", sum)

#wap to input side of a square and print its area

side = int(input("enter the side of the square: "))
area = side*side
print("area of the square: ", area)


#wap to input 2 floatong point numbers and print their average.

f1 = float(input("enter the num: "))
f2 = float(input("enter the num: "))
average = (f1+f2)/2
print("the average of two numbers: ",average)

#wap to input 2 int num, a and b. print True if a is greater or equal to b. if not print False.
#wap to input 2 int num, a and b. print True if a is greater or equal to b. if not print False.
#wap to input 2 int num, a and b. print True if a is greater or equal to b. if not print False.

a = int(input("enter the number: "))
b = int(input("enter the number: "))
print(a>=b)
print(not (a>=b))

