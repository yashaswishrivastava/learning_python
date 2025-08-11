#loops
#loops are used to repet instruction

count = 1
while count<=5:
    print("hello!")
    count = count + 1#without this line of code the code will run to infinite no of time
    #break statement
    #iteration
    
i=1
while i <= 100:
    print("yashaswi",i)
    i+=1

#print numbers from 1 to 10
i = 1
while i <= 10:
    print(i)
    i += 1
    #break statement

#print numbers from 100 to 1
i = 10
while i >= 1:
    print(i)
    i -= 1

#print the multiplication table of a number n
n = 5
i = 1
while i <= 10:
    print(n,"*",i,"=",n*1)
    i += 1

#print the elements of the following list using a loop
list1 = [1,4,9,16,25,36,49,64,81,100]
i=0
while i < len(list1):
    print(list1[i])
    i += 1

#search for a number x in this tuple using loop
tup = (1,4,9,16,25,36,49,64,81,100)
i=0
while i < len(tup):
    if tup[i]==25:
       print("number found")
       i += 1

#



