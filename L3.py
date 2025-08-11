#lists and tuples
#a built-in datatype that stores set of values it can store elements of diffrent 
#data types like int, float, string, list, tuple, dict etc.
#it is mutable i.e. it can be changed after creation

marks = [87.4, 98.2, 45.9, 23.7, 88.9]
print(marks)
print(type(marks))
print(marks[4])
print(len(marks))

#accessing elements in list of any datatype
student = ["yashaswi", 54, 94.9, "pune"]
print(student[0])
print(student[3])
print(student[2])

#list slicing
marks = [85, 94, 76, 63, 48]
print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[:])

#list methods
marks = [85, 94, 76, 63, 48]
marks.append(90)#addsone element at the end
print(marks)
marks.insert(2, 88)#inserts element at specified index
print(marks)

marks.sort()#sort in accending order
print(marks)
marks.sort(reverse=True)#sort in descending order
print(marks)

marks.reverse()#reverse the list
print(marks)
marks.insert(0,3)#enteres the value at certain index(indx, value)
print(marks)

list = [2,1,3,1]
list.remove(1)#removes first occurrence of the element
print(list)
list.pop(2)#removes element at index
print(list)

#tuples in python
#it is a collection of elements which are ordered and immutable

tup = (87,64,33,95,76)
print(type(tup))
print(tup[1])

tup =()#valid
tup = (1,)#single valued tuple or else will be considered as normal integer without comma
#tuple method

tup = (1,2,3,4,5,56)
#returns index of first occurence
print(tup.index(5))
print(tup.count(2))#counts total occurence

#wap to ask the user to enter the names of their three movies and store them in a list

movies = []
mov1 = input("enter the name of 1st movie: ")
mov1 = input("enter the name of 2nd movie: ")
mov1 = input("enter the name of 3rd movie: ")
movies.append(mov1)
movies.append(mov1)
movies.append(mov1)
print(movies)

#wap to check if a list contains a palindrome of elements. use copy() method

list1 = [1, 2, 1]
list2 = [1, 2, 3]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")

#wap to count the number of students with the "A" grade in the following tuple

grade = ["C","D","A","A","B","B","A"]
print(grade.count("A"))
grade.sort()
print(grade)

   

