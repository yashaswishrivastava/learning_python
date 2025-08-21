#dictionary and set in python
# dictionaries are used to store data values in key:value pairs
#thwy are unordered, mutable(changeable)& dont allow duplicate keys

info = {
    "name": "john",
    "age": "20",
    "subjects" : ["python", "c","java"],
    #"marks" : {"maths": 90, "science": 85}
    "topics" : ("dictionaries","sets"),
    "marks": 98.75
}
print(info)
print(info["name"])

info["name"] = "yashaswi"
print(info)

#nested dictionaries

student = {
    "name" : "yashaswi",
    "subjects" : {
        "os" : 100,
        "cn" : 100,
        "dbms": 99,
        "se" : 98,
        "python" : 99
    },
    "marks" : 98.75
}
print(student["subjects"]["os"])

#dictionaries method
print(student.keys())#return all the 
print(student.values())#return all the values
print(student.items())#returns all (key, val) pairs as tuples
print(student.get("name"))#returns the value for the given key
print(student.get("name", "default"))
print(student.update({"name": "yashi"}))#update the new key in the dictionary


#sets in python
#set is the collection of the unordered items.
#each element in the set must be unique and immutable
#duplicate values get ignored
#sets are mutable and unorederd

collection = {1,2,2,2,2,3,4,5,6,7,8,"hello","boom"}
print(collection)
print(len(collection))

empty_set = set()#to create empty set

#set methods
collection.add(45)#adds an element
collection.remove(4)#removes an element
#collection.clear()#empties the set
collection.pop()#removes a random value
collection.discard(4)#removes an element if it exists
print(collection)

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.union(set2))
print(set1.intersection(set2))

#store the following word meanings in a python dictionaries

dict = {
    "table":[" a piece of furniture","list of facts and figures"],
    "cat":"a smol animal cutuuuu"
}
print(dict)


#find the total no of classrooms required per subject

class1 = {"python","java","c++","python","javascript","java","python","java","c++","c"}
print(len(class1))

#wap to enter marks of 3 subs from the user and store them in a dictonary. start with an empty dictionary
#and add one by one 

marks = {}

x = int(input("enter phy: "))
marks.update({"phy": x})
#the end 


