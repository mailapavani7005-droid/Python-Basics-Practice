# Day 4 - Lists

## Topics Covered

### Lists

Lists are used to store multiple values in a single variable.

### List Operations

* append()
* insert()
* remove()
* pop()
* sort()
* reverse()

### List Indexing

Access elements using index numbers.

### List Slicing

Access multiple values from a list.

## Programs Practiced

* Add Elements
* Insert Elements
* Remove Elements
* Pop Elements
* Sort a List
* Reverse a List
* Print List Items Using Loop

## What I Learned

I learned how to store, access, modify, and organize multiple values using lists.



1.fruits=['Apple','Banana','Mango'] 
print(fruits)


2.fruits=['Apple','Banana','Mango'] 
print(fruits[2])


3.fruits=['Apple','Banana'] 
fruits.append('orange')
print(fruits)



4.fruits=['Apple','Banana'] 
fruits.insert(1,'orange')
print(fruits)

5.fruits = ["Apple", "Banana", "Mango"] 
fruits.remove("Banana")
print(fruits)

6.fruits = ["Apple", "Banana", "Mango"] 
fruits.pop(0)
print(fruits)

7.fruits = ["Apple", "Banana", "Mango"] 
for fruit in fruits:
    print(fruit)


8.numbers = [5, 1, 8, 2] 
numbers.sort()
print(numbers)


9.numbers = [1, 2, 3, 4] 
numbers.reverse()
print(numbers)


10.fruit1=input("Enter the fruit1:") 
fruit2=input("Enter the fruit2:")
fruit3=input("Enter the fruit3:")
list=[fruit1,fruit2,fruit3]
print(list) 
