#loop and string
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