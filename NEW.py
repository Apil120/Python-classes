from typing import Any
sr="String Indexing"
print (sr)
print (sr[0])
print (sr[2])
print (sr[4])
print (sr[5])
print (sr[13])
print("Using negative indexing")
print (sr[-15])
print (sr[-11])
print (sr[-1])
print (sr[-10])
print (" Using Slice indexing")
print (sr[0:6:2])
print (sr[0:3:1])
print (" Using negative slice indexing")
print (sr[-1:-4:-1])    
print(sr[-15:-12:1])
print("Getting characters in even indexes")
print (sr[0:15:2])
print (sr[0:])
print(sr[::3])
print(sr[2::-1])
print(sr[-1:-4:-1])
#String methods
print(sr.upper())
q="I Am pracTinG string METhoD !!! "
print(q.upper())
print(q.lower())
print(q.split(" "))
w="Am pracTinG"
by="have practiced"
print(q.replace(w, by))
print(q.endswith(" "))
s="12"
print(s.isdigit())
print(q.strip("!!! "))
d=input('Enter your username')
e=int(input('Enter your age'))
print("Hello"+d+","+ "your age" +str(e))
print("Hi {} . Your age is   {}".format(d, e))
f"HI {d}, your age is {e}"
print('*** Hi i\'m  Apil*** \n I am the one who knocks \t We need to cook\\ We need to make Methanphetamine')
print(len(w))
for char in w:
    print(char)
    print('----------------')


##9JUNECLASS
mutable_list=['a','b','c','d','e','f','g']#Changing the list of characters 
print(mutable_list)
mutable_list[0]='A'
print(mutable_list)
#List methods
new_list=[1,2,3,4]
new_list.append(5)
print(new_list)
new_list.insert(1,45)
print(new_list)
new=[1,2,3,4]
list=[5,6,7,8,9,10,11,12,13]
new.extend(list)
#concatenate list "+" operator
listt=list+new
print(listt)
list.remove(13)
print(list)
print("This is the 69th line of the file... nice!")
n=int(input("Enter an index"))
list.pop(n)
print(list)
list.reverse()
print(list)
list.sort()
print(list)
list[::-1]
print(list)
list_sort=[1,23,3,2,3,43,4,5446,346]
print(list_sort)
list_sort.sort()
print(list_sort)
list_sort.sort(reverse=True)
print(list_sort)
input_list=['hello', 'world']
result=" ".join(input_list, " ")
join_list=['hello', 'world']
loop_list=['Hello','I','am','world']
for i in loop_list:
    print(i)
    print('----------------')

for idx,i in enumerate(loop_list):
        print(idx)
        print(i)
        print(type(i))
        print('----------------')
       

#Tuple(Immutable)
#Empty tuple
a=()
print(a)
print('----------------')
#simple tuple with mixed data types
tuple_list=(1,2,"3",'4',5,'The','cat',')')
print(tuple_list)
print('----------------')
print(type(tuple_list))
print('----------------')
#length of tuple
z=(len(tuple_list))
print(z)
print('----------------')
#Nested tuple
nested_tuple=((1,2),(3,4),'a',(5,6))
print(nested_tuple)
print('----------------')
print(len(nested_tuple))
print('----------------')
print(type(tuple_list))
print('----------------')
#Tuple from string
sample_str='I am creating a tuple from a string'
sample_str.split(" ")
print(tuple(sample_str.split(" ")))
print('----------------')
#Tuple Indexing
#SAME AS LIST
#Positive index
tuple_len=(1,2,3,4,5)
print(tuple_list[0])
print('----------------')
print(tuple_list[4])
print('----------------')
print(tuple_len[len(tuple_len)-1])
print('----------------')
#Negative index
print(tuple_len[-5])
print('----------------')
print(tuple_len[-1])
#Tuple Slice
#tuple[start:end:step]
#Positive Step
print(tuple_len[0:3:0])
print('----------------')
print(tuple_len[-3::1])
print('----------------')
print(tuple_len[0:5:2])
print('----------------')
#Negative Step
print(tuple_len[-3::-1])
print('----------------')
print(tuple_len[-2::-1])
print('----------------')
print(tuple_len[-1:-4:-1])
print('----------------')
print(tuple_len[::-1])
print('----------------')
#Verification of tuple immutability
tuple_len[0] ='Hello'
#Tuple methods
tuple_lent=(1,2,2,2,2,4,2,34,32,4,8,5,5,5,5,)
print(tuple_lent.count(2))
print('----------------')
print(tuple_lent.index(5))
print('----------------')
#Tuple item addition methods
#Tuple--> list-->list.append()-->tuple
s=list(tuple_lent)
s.append(7)
nig=tuple(s)
print(nig)
#Tuple and tuple can be added together with + operator
tt=(1,2,3)
td=(23,4,2134)
tttd=tt+td
print(tttd)
#Unpack tuple
unpack_tuple=('pyhton','is','awesome','great')
a,b,c,d=unpack_tuple
print(a)
print('-----')
print(b)
print('-----')
print(c)
print('-----')
print(d)
print('-----')
#2 items in a single variable
#'*' tells python to print all remaining items in b 
a,*b,c=unpack_tuple
print(a,b,c)
#Tuple loops
initialize_tuple=('pyhton','is','awesome','great')
for item in initialize_tuple:
     print(item)
     print('-----')
for idx, item in enumerate(initialize_tuple):
     print(idx, '=',item)
     print('-----')
#Tuple Comprehension
compres=('PyThoN','iS','GrEaT')     
lower=tuple(item.lower() for item in compres)
print(lower)
#Dictionary 

thid={
 'Car':'Ford',
 'Languages':'English',
 'years':'2020',
 'name':'Hari',
 'age':'20',
 'address':'kathmandu',
 'cond':False,
'con':True
}
print(thid)
print(thid['Car'])
print(type(thid))
#Nested dictionary
nested_dict={
'fruits':{'Mango':2,'Apple':3,'Banana':4},
'Drinks':{'Coke':5,'Whiskey':6,'Rum':7},
'thid':thid
}
print(type(nested_dict))
print(nested_dict['fruits']['Mango'])
print(len(nested_dict))
#Dictionary indexing
fruit_count={
     'Mango':20,
     'Apple':30,
     'Banana':40
}           
print(fruit_count)
print(fruit_count['Mango'], fruit_count['Apple'],fruit_count['Banana'])   
food={
    'sweet':{'Chocolate':42,'Cakes':444,'her':19,},
    'Drink':{'Coke':40,'sprites':44}
}                           
print(food)
print(food['sweet']['her'])
#Dictionaries are mutable
fruit_count['Mango']=50
print(fruit_count)
fruit_count['Mango']=500
print(fruit_count)
#Dictionary Methods
print(type(thid))
print(thid.keys())#IMPORTANT
print(thid.values())#IMPORTANT
print(thid.items())#IMPORTANT
print(thid.get('name'))
print(thid.get('age'))
print(thid.update({'name':'Apil'}))
thid.pop('name')
for x in thid:
     print(x)
#Dictionary Compreshion
sample_list=[10,20,30,40,50,60]
sample_dict={idx:item for idx, item in enumerate(sample_list)}
print(sample_dict)
#SETS
my_empty_set=set()
print(my_empty_set)
print(type(my_empty_set))
my_set={1,2,3}
print(my_set)
my_new_set=set([1,2,'2','d'])
print(my_new_set)
my_set.add(4)
print(my_set)
my_set.remove(4)
print(my_set)
print(len(my_set))
#SET METHOD
print(my_set.union(my_new_set))
print(my_set.intersection(my_new_set))
print(my_set.difference(my_new_set))
print(my_set.symmetric_difference(my_new_set))
print(my_set.issubset(my_new_set))
print(my_set.issuperset(my_new_set))
print(my_set.isdisjoint(my_new_set))
sample_l=[1,2,3,4,5,6,7,8,9,10,11]
sample_lma={idx:item for idx,item in enumerate(sample_l)}
print(sample_lma)
#Conditions and branching
#if,elif,else are keywords for conditions
z=int(input("Enter a number"))
if z>=0 :
     print('Positive')
else :
 print('negative')
eve=int(input("Enter a number"))
if eve%2==0:
    print("Even")
elif eve%2!=0:
 print("odd")

ol=int(input("Enter a number"))
if ol%2==0:
    for i in range( ol ):
        print('Hello')

elif ol%2==1:
    for i in range( ol ):
        print('World')

wojids=int(input("Enter a number"))
if wojids == 54:
    print("Hello")
elif wojids != 54:
    print("World")

for i in range( wojids ):
    if i%2==0:
     print("Hello world")
    else:
     print("World")
variab=input("Enter a string of text")
print(variab)
if len(variab)%2==0:
    print("Hello world")
else:
    print('Goodbye world')
number=int(input("Enter a number"))
number21=int(input("Enter another number"))
if number>number21:
    print("number>number21")
elif number==number21:
    print("number=number21")
else:
    print("number<number21")
#Nested if else
num1=int(input("Enter a number"))
num2=int(input("Enter a number"))
num3=int(input("Enter a number"))
if num1>num2:
    if num1>num3:
        print("The first number is the largest number")
elif num2>num1:
    if num2>num3:
        print("The second number is the largest number")
else:
    print("The third number is the largest number")
a=20
b=30
print("a is greatest ")if a>b   else  print("a is less than b ")
#GREATEST NUM IN 3 USING TERNARY OPERATORS
a=20
b=30
c=100
print("a is greatest ")if (a>b and a>c)   else  ('Greatest is B ')if (b>c) else ('Greater is C ')
#PASS KEYWORD

#LOOPS 
i=0
while i <10:
    print("Hello world")
#Break Keywords
i=0
while i < 10:
    if i ==3:
        break
    print("Hello world")
    i=i+1
#CONTINUE KEYWORD
i=0
while i < 10:
    if i ==3:
        continue
    print("Hello world")
    i=i+1
#INFINITE LOOP
i=0
while True:
    print("Hello world")
    i=i+1
#For Loop
for i in range(5):
    print("*"*i)
#Functions in python
def sum(a,b):
    return a+b
print(sum(2,3))
def sum(a,b):
    return a+b
    sum(2,3)
#Function to take two numbers and return the larger number without parameters
def print_greater():
    a=int(input("Enter a number"))
    b=int(input("Enter a number"))
    if a>b:
        print(a)
    else:
        print(b)
#Function with parameters and without return 
a=int(input("Enter a number"))
b=int(input("Enter a number"))
def print_greater(a,b):
    if a>b:
        print(a)
    else:
        print(b)
print_greater(a,b)
#Function without parameters and with return 
a=int(input("Enter a number"))
b=int(input("Enter a number"))
def print_greater():
    if a>b:
        return a
    else:
     return b
print_greater()
#Function with parameters and with return
def find_greater_number(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

result = find_greater_number(10, 20)
print("The greater number is:", result)
#Function with parameters and return 
def function_name(a,b):
    if a>b:
            mesg="a is greater than b"
    else:
            mesg="a is less than b"
    return mesg
a=2
b=3
mesg=function_name(a,b)
print(mesg)
#Study Global vs Local Variable
#Args 
def args(*args):
  args=list(args)
  args[0]=0
  sum=0
  for i in args:
    sum+=i

  return sum
print(args(1,2,3,4,5,56,5,4,46))
#KWargs
def print_add(**kwargs):
   for key,value in kwargs.items():
    print(f"{key}:{value}")

print_add(city='KTM',
          STATE='BAGMATI')
#Recursion
def fact():
  print("I am recursion")
fact()

#Factorial of a number
n=int(input("Enter a number"))
def fact(n):
 if (n==0 or n==1):
  return 1
 else:
  return n*fact(n-1)
fact(n)
#Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(20):
    print(fibonacci(i))
#Class and object
class Person:
  name='Apil'
  occupation='Student'
  networth=10000
  def info(self):
    print(f"{self.name} is a {self.occupation}" )
a=Person()
b=Person()
c=Person()
a.name='Messi'
#Access Modifiers
#According to OOP convention, protected variables can be accessed only by derived class
#_varname is a protected variable, the protected variables have '_' infront of the name
#Create private variables:
class Vehicle:
  def __init__(self,color="Red"):
    self.__vehicle_color = color
  def access_priv(self):
    return self.__vehicle_color

  def __reset_color(self,color):
    self.__vehicle_color= color

  def temp(self,color):
    self.__reset_color(color)
    print(f"Color reset to  :{self.__vehicle_color}")
car = Vehicle("Green")
print(car.access_priv())
#car.__vehicle_color

#Resetting color
car.temp("BLUE")
b.name="Ronaldo"
b.occupation="Also a footballer"
a.info()
b.info()
c.info()

#Create private variables

class Vehicle:
  def __init__(self, color):
    # create private attributes
    self.__vehicle_color = color

  def access_private(self):
    return self.__vehicle_color

  # create private methods
  def __reset_color(self, color):
    print('Colour Reseting')
    self.__vehicle_color = color

  # access private methods inside class
  def reset_display_color(self, color = None):
    self.__reset_color(color)
    print(f"Colour after reseting is: {self.__vehicle_color}")


# create object
car = Vehicle('red')
## access private attributes outside of class
# car.__vehicle_color
## access private attributes via public methods
private_attr = car.access_private()
print(private_attr)
## Base class
class Vehicle:
  def __init__(self, name, color):
    self.name = name
    self.color = color
 
  def start(self):
    print(f"The {self.color}  {self.name} is starting.")
 
  def stop(self):
    print(f"The {self.color} {self.name} is stopping.")

#Encaplsulatoin Practice
class Car:
    def __init__(self, speed, color):
        self.__speed = speed
        self.__color = color

    def set_speed(self, value):
        self.__speed = value

    def get_speed(self):
        return self.__speed

    def set_color(self, value):
        self.__color = value

    def get_color(self):
        return self.__color

ford = Car(200, "Red")
honda = Car(250, 'Black')
audi = Car(260, 'Blue')
##Changing the values
ford.set_speed(400)
ford.__speed=400
ford.set_color('Orange')
ford.__color="Cyan"
print(ford.get_speed())
print(ford.get_color())
print("-------")

## Derived class Car
 
class Car(Vehicle):
  def __init__(self, name, color, fuel_type):
    super().__init__(name, color) ## super is used to call base class constructor
    self.fuel_type = fuel_type
 
  def drive(self):
    print(f"The {self.color} {self.name} is driving.")
 
## Derived class Bike
class Bike(Vehicle):
  def __init__(self, name, color, engine_capacity):
    super().__init__(name, color) ## super is used to call base class constructor
    self.engine_capacity = engine_capacity
 
  def ride(self):
    print(f"The {self.color} {self.name} is being ridden.")
 
# Creating instances of derived classes
car = Car("Car", "Red", "Petrol")
bike = Bike("Motorcycle", "Blue", 250)
 
# Accessing attributes and calling methods
print(car.name)  # Output: Car
print(bike.color)  # Output: Blue
 
car.start()  # Output: The Red Car is starting.
bike.stop()  # Output: The Blue Motorcycle has stopped.
 
car.drive()  # Output: The Red Car is driving.
bike.ride()  # Output: The Blue Motorcycle is being ridden.


#Write a python program to create two Base class named wheels and engine. From the 2 base classes, create 
#Base class 1
class Engine:
  def start(self):
    print("The engine is starting")
  def stop (self):
    print("The engine has stopped")

  #Base Class 2
class wheels:
  def drive(self):
    print("The wheels are rotating")
#Derived Class
class Car(Engine,wheels):
  def rotate(self):
    print("The car is being driven")
    #objectname=derivedclass()
    #objectname.method()
    ##MAKE INSTANCE oF DERIVED CLASS, AND ACCESS THE BASE CLASS METHODS USING THE INSTANCE
car=Car()
print(type(car))

# access methods of base class "Engine"
car.start()  # output: The engine is starting.
car.stop()  # output: The engine has stopped.

# access methods of base class "Wheel"
car.rotate() # output: The wheels are rotating.


#Multilevel inheritance
 #Syntax class DerivedClass1(Baseclass)
 #class Derivedclass2(DerivedClass1)
#Example of multilevel inheritance:
#Creation of Base class:
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def start(self):
        print(f"The {self.name} is starting")

class Car(Vehicle):
    def drive(self):
        print(f"The {self.name} is being driven")

class SportsCar(Car):
    def accelerate(self):
        print(f"The {self.name} is accelerating")

sport_car = SportsCar("Sports Car")
sport_car.start()  # Output: The Sports Car is starting
sport_car.drive()  # Output: The Sports Car is being driven
sport_car.accelerate()  # Output: The Sports Car is accelerating


#Hierarchial Inheritance
#Single base class gets inherited by multiple derived classes
#Syntax 
#class A
#class B(A)
#class C(A)
#class D(B)
#class E(B)

#Example of Hierarchical Inheritance
#Base class:
class Vehicle:
    def __init__(self, name):
        self.name = name

    def start(self):
        print(f"The {self.name} is starting.")

    def stop(self):
        print(f"The {self.name} is stopped.")

#Derived classes:
class Car(Vehicle):
    def drive(self):
        print(f"The {self.name} is driving.")


class Bus(Vehicle):
    def drive(self):
        print(f"The {self.name} is driving.")


C = Car("Car")
d = Bus("Bus")

C.start()
d.start()
C.drive()
d.drive()
C.stop()
d.stop()
#Abstract classes
from abc import ABC, abstractmethod


class Vehicle(ABC):
  @abstractmethod
  def start(self):
    pass
class car(Vehicle):
  def start(self):
    print("I am a car")

class Truck(Vehicle):
  def start(self):
    print("I am truck")


Car=car()
Car.start()
TrucK=Truck()
TrucK.start()

#Special methods
#Example:
class Vehicle:
  def __init__(self,name,color,price,num_tiers):
    self.name=name
    self.color=color
    self.num_tiers=num_tiers
    self.price=price
  def __str__(self):
    return f"{self.color} {self.name} has price of {self.price}"
  def __add__(self,other):
    return self.price+other.price
  def __gt__(self,other):
    if(self.price>other.price):
      return True
    else:
      return False
  def __del__(self):
    print("Object is destroyed")

#Object instantiation
car=Vehicle("car","red",100000,4)
bus=Vehicle("bus","blue",100000,8)

#Invoke __str__
print(car)
print(bus)

#str(car)
#str(bus)

#Invoke addition
car+bus
#Invoke __gt__:
car>bus
#Invoke __del__:
del car
#FILE IN PYTHON
#!touch demo.txt
#!cat demo.txt
#Opening files in python
#Syntax:
#file_object=open("filename","mode")
file_obj=open("demo.txt","r")
print(type(file_obj))
file_obj=open("demo.txt","w")
file_obj=open("demo.txt","a")
file_obj=open("new.txt","x")
with open("demo.txt","r") as file_obj:
  file_content=file_obj.read()
print(file_content)
with open("demo.txt","r") as file_obj:
  file_content=file_obj.readline()
print(file_content)
with open("demo.txt","r") as file_obj:
  file_content=file_obj.readlines()
print(file_content)
file_o=open("New.txt","r")
file_contents=file_o.read(5)

print(file_contents)
file_name="Test_file.txt"
with open(file_name,"w") as file_object:
  file_object.write("**Hi I am learning File Handling in python**")

with open(file_name,"a") as file_object:
  file_object.write("\n I am soon going to learn about AI")

import os
os.remove('file_name')

#!ls
#!pwd
dir(os.path)
file_name="Test_file.txt"
with open(file_name,"w") as file_object:
  file_object.write("**Hi I am learning File Handling in python**")
fileo="Test_file.txt"
if os.path.exists("Test_file.txt"):
  os.remove("Test_file.txt")
  print(f"File named {fileo} deleted")
else:
  print("No such file")

#Database connection
import sqlite3
db_name="Users.db"
conn=sqlite3.connect(db_name)
print("Opened Database Sucessfully")

conn.execute(""" CREATE TABLE NEWemploye
(
  ID                  INT                           PRIMARY KEY                 NOT NULL,
  NAME                VARCHAR(50)                                               NOT NULL,
  AGE                 INT                                                       NOT NULL,
  ADDRESS             TEXT,
  SALARY              FLOAT
)
""")
print("Table created sucessfully")


conn.execute(""" INSERT INTO NEWemploye (ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,"RAM",32,"KATHMANDU",20000000)""")
print("Data inserted sucessfully")

conn.execute(""" INSERT INTO NEWemploye (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,"Hari",32,"Bhaktapur",200000)""")
print("Data inserted sucessfully")

conn.execute(""" INSERT INTO NEWemploye (ID,NAME,AGE,ADDRESS) VALUES(3,"Rama",33,"Lalitpur")""")
print("Data inserted sucessfully")

conn.execute(""" INSERT INTO NEWemploye (ID,NAME,AGE,SALARY) VALUES(4,"Sita",34,2000)""")
print("Data inserted sucessfully")

cursor=conn.execute("SELECT id,name,address,salary from NEWemploye")
for row in cursor:
  print("ID=",row[0])
  print("Name=",row[1])
  print("Address=",row[2])
  print("Salary=",row[3])
  print("--------")

items=conn.execute("SELECT *FROM NEWemploye").fetchall()
print(items)

conn.execute("UPDATE NEWemploye SET salary=250000 where id=4")
conn.execute("UPDATE NEWemploye SET Address='Pokhara' where id=2")
conn.commit()

conn.execute("DELETE FROM NEWemploye where name='Sita'")
conn.commit()
conn.close()
print("Connection Ended")

#Exception Handling:

a=int(input("Enter first number"))
b=int(input("Enter second number"))

division=a/b #ZeroDivisionError occurs if b=0
print(f"Division a/b=",division)
print("Division completed")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    division = a / b
    print("Division is", division)
except Exception as e: #This line Can handle any exception and is not exception specific
    print("Exception occurred:", e)

print("Division completed")


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

try:
    division = a / b
    print("Division is", division)
except ZeroDivisionError : #This line can handle only ZeroDivisionError
    print("Division by 0 is not possible")

print("Division completed")

try:
   int("test")
except ValueError: #This line can handle only ValueError
  print("Strings cannot be typecasted into integer")
  print("Code ran sucessfully")

try:
 print(we)
except Exception as e: #NameError
  print("Error :",e)

#Exception handling with multiple excceptions:
try:
  a=int(input("Enter a number"))
  b=int(input("Enter a number"))
  
  division=a/b #if b=0,ZeroDivisionError Exception
except ValueError:
  print("Strings cannot be typecastted into integers please input only intergers")

except ZeroDivisionError:
  print("Division by 0 is not possible")

except Exception as e:
  print("Error ",e)

#try except else block:
a=10
b=10
try:
  division=a/b

except ZeroDivisionError:
  print("From except block")
  print("Cannot divide by zero")

else:
  print("No error from else block")
  print(f"{a}/{b}={division}")
#try exception finally block:
try:
    num=int(input("Enter a number"))
    result=10/num
    print("Result:",result)

except ValueError:
  print("Invalid Input please input only integers")
  
except ZeroDivisionError:
    print("Cannot divide by 0")
finally:
    print("Program executed sucessfully")
#Raising an Exception:
def raise_exception(num):
   if num <0:
      raise ValueError("Square root of negative doesnt exist")
   else:
     return num**0.5
   
raise_exception(num)

num=40
try:
  result=raise_exception(num)
except Exception as e:
  print("Error:",e)
