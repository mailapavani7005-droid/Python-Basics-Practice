# Day 5 - Tuples and Dictionaries

## Tuple Topics

### Tuple

A tuple is used to store multiple values and cannot be changed after creation.

### Tuple Features

* Uses ()
* Immutable
* Supports Indexing

## Dictionary Topics

### Dictionary

Stores data in key-value pairs.

### Dictionary Methods

* keys()
* values()
* items()

### Operations

* Access Values
* Add New Keys
* Update Existing Values

## Programs Practiced

* Student Dictionary
* Book Dictionary
* Tuple Creation
* Access Dictionary Values

## What I Learned

I learned the difference between tuples and dictionaries and how key-value pairs work.


1.fruits=('Apple','Banana','Mango') 
print(fruits)

2.fruits = ("Apple", "Banana", "Mango") 
print(fruits[1])


3.student={ 
    "name":"pavani",
    "age":20,
    "city":"vijayawada"
    }
print(student)

4.student={ 
    "name":"pavani",
    "age":20,
    "city":"vijayawada"
    }
print(student["name"])

5.student={ 
    "name":"pavani",
    "age":20,
    "city":"vijayawada"
    }
student["college"]="NRI"
print(student)

6.student={ 
    "name":"pavani",
    "age":20,
    "city":"vijayawada"
    }
student["college"]="NRI"
print(student.keys())


7.student={ 
    "name":"pavani",
    "age":20,
    "city":"vijayawada"
    }
student["college"]="NRI"
print(student.values())

8.student={ 
    "name":"pavani",
    "age":20,
    "city":"vijayawada"
    }
student["college"]="NRI"
print(student.items())

9.Book={ 
    "title":"python",
    "price":500
    }
print(Book["price"])


10.name=input("Enter the name:") 
age=int(input("Enter the age:"))
student={
    "name":name,
    "age":age
    }
print(student)
