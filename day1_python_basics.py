1.name=input("Enter the name:") 
print("Hello",name,"Welcome to python")

2.marks1=int(input("Enter the marks1:")) 
marks2=int(input("Enter the marks2:"))
marks3=int(input("Enter the marks3:"))
avg=(marks1+marks2+marks3)/3
print("avg:",avg)


3.age=int(input("Enter the age:")) 
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")


4.for i in range(1,21): 
    if i%2==0:
        print(i)

5.for i in range(1,11): 
    if i==5:
        break
    print(i)

6.name="pavani" 
print(len(name),name.upper(),name[0])

7.fruits = ["Apple","Banana","Mango"] 
fruits.append("orange")
fruits.remove("Banana")
print(fruits)




8.def add(a,b): 
    return a+b
result=add(10,20)
print(result)

9.for i in range(1,11): 
    if i==5:
        continue
    print(i)

10.marks=int(input("Enter the marks:")) 
if marks>90:
    print("A Grade")
elif marks>75:
    print("B Grade")
elif marks>35:
    print("C Grade")
else:
    print("Fail")



