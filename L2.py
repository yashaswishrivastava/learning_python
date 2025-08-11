str1 = "this is a string."
str2 = "this is another string."
len1 = len(str1)
print(len1)
print(str1+" "+str2)

#indexing

str = "yashaswi shrivastava"
print(str[9])
#using indexing we can only access the character but we cant modify the characters


#we can only modify the string using slicing method
str = "yashaswi shrivastava"
#str[9] = 'a'
#this will throw an error because strings are immutable in

#slicing 
str = "yashaswi shrivastava"
str1 = str[0:5]
print(str1)
print(str[5:len(str)])

#negative slicing
str = "apple"
print(str[-5:-1])

str = "im studying by myself"
print(str.endswith("elf"))
print(str.capitalize())
str = str.capitalize()

print(str)

print(str.replace("y","u"))
#splitting the string
print(str.find("o"))
#find method returns the index of the first occurrence of the 
print(str.count("by"))
#count method returns the number of occurrences of the substring

#wap to input users first name and print its length
name = input("enter your name:")
print(len(name))

#wap to find the occurence of $ in a string
str = input("enter the string name: ")
print(str.count("$"))

#conditional statement
# if else statement
# if condition is true then the code inside the if block will be executed
# if condition is false then the code inside the else block will be executed
#age = int(input("enter your age: "))
#if age >= 18:
 #   print("you are eligible to vote")
    #else:
        #print("you are not eligible to vote")
        #this will throw an error because the indentation is not correct
        #corrected code
age= int(input("enter your age"))

if(age>=18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

#elif 

caste = input("enter your caste: ")
if (caste == "st"):
    print("you are eligible for reservation")
elif(caste == "obc"):
    print("you are semi eligible for reservation")
elif(caste=="genral"):
    print("you are not eligible for reservation tenenenana lol")
else:
    print("invalid caste bhaaad me jao videsh jao")

#nesting
age = int(input("enter your age: "))
if(age>=18):
    print("you are eligible to vote")
    if(age>=60):
        print("you are eligible for pension")
    else:
        print("you are not eligible for pension")
else:
    print("you are not eligible to vote")

#wap to check if the number is entered by the user is odd or even
num = int(input("enter the number: "))
if(num%2==0):
    print("the number is even")
else:
    print("the number is odd")

#wap to find the greatest of 3 numberes entered by the user

num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
num3 = int(input("enter the third number: "))

if(num1>num2 and num1>num3):
   print("the greatest number is",num1)
elif(num2>num1 and num2>num3):
   print("the greatest number is",num2)
elif(num3>num1 and num3>num2):
   print("the greatest number is",num3)
else:
    print("all numbers are equal")

#wap to check if a number is multiple of 7 or not

num = int(input("enter a number to check if it is divisible by 7: "))
if(num%7==0):
    print("the number is divisible by 7")
else:
    print("the number is not divible by 7")

