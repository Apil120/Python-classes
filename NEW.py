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
print('*** Hi i\'m  Apil***\n I am the one who knocks \t We need to cook\\ We need to make Methanphetamine')
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
