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


    