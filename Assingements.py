#Loop and string assingement
sample_str="String sample"
print(len(sample_str)) ##Length with LEN

for i in range(len(sample_str)):
    i=i+1
    
     

print(i) ##Length with loop and string
mystring = sample_str.lower()#Vowels and consonants in a given string

vowels = ""
consonants = ""

for d in mystring:
    if d in "aeiou":
        vowels += d
    else:
        consonants += d

print("Vowels:", vowels)
print("Consonants:", consonants)

input_string = "My name is xyz"# TWO  CHARACTER FROM THE LAST AND THE FIRST OF A STRING     

new_string = input_string[:2] + input_string[-2:]
print(new_string)

first_str="First"#python program to get a single string from two given strings , seperated by a space and swap the first two characters of each string 
second_str="Second"
x=second_str[:2]+first_str[2:]
y=first_str[:2]+second_str[2:]
z=x+ " " +y
print(z)

string = input("Enter a string: ")#python program to remove nth index character from a non empty string, ask user for string and index
index = int(input("Enter the index of the character to remove: "))
new_stringg = string[:index] + string[index + 1:]
print(new_stringg)

#List Assingements:
#Sort a list without list.sort()
assingements = [1,2,43,64234,3642,143531]
print("List before sorting",assingements)
n=len(assingements)
for i in range(n):
    for j in range(n-i-1):
            if assingements[j]>assingements[j+1]:
                assingements[j],assingements[j+1]=assingements[j+1],assingements[j]



print("List after sorting",assingements)

#python proggram that initializes non empty list of words with length=5.Display longest word with it's length
words=['Apples', 'Bananas', 'Cherries', 'Mango','Watermelon']
longest=" "
length=0
for word in words:
     if len(word)>length:
          length=len(word)
          longest=word


print ('longest word is',longest,'and the  length is',length)   

numbers = [1, 2, 3, 4, 5] # python program to sum all the items in a list

print(numbers)
sum_1 = 0
for i in numbers:
    sum_1 = i+sum_1
print("Sum of elements in a list", sum_1)
smallest = numbers[0]
for x in numbers:
    if x < smallest:
        smallest = x
print("Smallest item in a list :", smallest)

sample=['abc','aba','1221','xyz']
print(sample)
o=0
for k in sample:
     if len(k) >=2  and k [0] == k[-1]:
          o+=1

     
print('the number of strings where string lenth is 2 or more and the first and last characters are the same from a given list of strings is',o)
#to check if a list is empty or not
if len(sample)==0:
     print("List is empty")
if len(sample)!=0:
     print('List is not empty')

#python program to insert a given string infront of the list element
my_list =[1,2,3,4]
strr="std"
output =[strr+item for item in my_list]
print(output)
#Tuple:
#LOOP
#Write a program to generate all possible combinations of 3 numbers from 1 to 5
for x in range(1,6):
    for y in range(1,6):
        for z in range(1,6):
            print(x, y, z)
#Use recursion to print the fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
for i in range(20):
    print(fibonacci(i))

#Experiment with private and protected attributes

class New:
  def __init__(self,name):
    self.a=10
    self._b=20
    self.__c=30
New=New("name")
print(New.a)
print(New._b)
#The line below will return an error as it is directing the print function to a private attribute which can be identified by the two underscores infront of the var name.
print(New.__c)

#Explore hierarchial inherticance:
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

#Q. Write a python program to create abstract class with method start(). Create another 2 class Car and Truck inherited from Abstract Class with the implementation of abstract method.
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

#Experiment with  def __len__ and special methods
#INSTALL AND SETUP DBEAVER
