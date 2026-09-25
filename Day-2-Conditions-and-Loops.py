# Day 2 - Conditions and Loops

## Topics Covered

### If Statement

Used to execute code when a condition is True.

### If Else Statement

Used to execute one block if the condition is True and another block if it is False.

### If Elif Else Statement

Used to check multiple conditions.

### Nested If

An if statement inside another if statement.

### For Loop

Used to repeat a block of code a specific number of times.

### While Loop

Repeats code as long as a condition is True.

### Break Statement

Stops the loop immediately.

### Continue Statement

Skips the current iteration and moves to the next iteration.

## Programs Practiced

* Pass or Fail Program
* Grade Calculator
* Positive, Negative, Zero Program
* Print Numbers 1 to 10
* Print Even Numbers 1 to 20

## What I Learned

I learned how Python makes decisions using conditions and repeats tasks using loops.



1.name="pavani" 
age=20
college="NRI"
print(name)
print(age)
print(college)


2.name=input("Enter the name:") 
  print("Welcome",name)

  
3.marks=int(input("Enter the marks:")) 
if marks>=35:
    print("Pass")
else:
    print("fail")  

    
4. marks=int(input("Enter the marks:"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=35:
    print("Grade C")
else:
    print("fail")



5.for i in range(1,11): 
    print(i)


6.for i in range(1,21): 
    if i%2==0:
        print(i)

7.i=1 
while i<6:
    print(i)
    i=i+1

8.for i in range(1,11): 
    if i==5:
        break
    print(i)


9.for i in range(1,11): 
    if i==5:
        continue
    print(i)


10.num=int(input("enter the number:")) 
if num >0:
    print("Positive number")
elif num<0:
    print("negative number")
else:
    print("Zero")  check remaining questions code 



