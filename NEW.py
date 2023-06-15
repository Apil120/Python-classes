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
