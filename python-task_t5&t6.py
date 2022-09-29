'''1. Write a program in Python to allow the error of syntax to be handled using exception handling.
HINT: Use SyntaxError
name=input("Enter the name")

for i in name:
    try:
        print(i
        continue
    except SyntaxError as syt:
        print(syt)

'''
'''2. Write a program in Python to allow the user to open a file by using the argv module. If the
entered name is incorrect throw an exception and ask them to enter the name again. Make sure
to use read only mode. 

import sys
try:
    with open(sys.argv[1],'r') as test.txt:
        print(test.txt.read())
except FileNotFoundError:
    print("File is not Found,Please enter correct file name?")
'''

'''Write a program to handle an error if the user entered a number more than four digits it should
return “The length is too short/long !!! Please provide only four digits”

#solution:
num=input("Enter the 4-digit number:")
print(len(num))
try:
    if len(num)<4:
        print("You have enter correct no of digit")
    elif len(num)>4:
        raise Exception()
except: 
        print("The length is too short/long !!! Please provide only four digits")'''


'''
4. Create a login page backend to ask users to enter the username and password. Make sure to
ask for a Re-Type Password and if the password is incorrect give chance to enter it again but it
should not be more than 3 times.

solution:
user_name="kiran"
pass_word="pythonversion3"

userName=input("Welcome! Enter your username: ")
password=input("Password:")

count=0
count+=1

while userName==userName and password==password:
    if count ==3:
        print("You have try maximum login limit")
        break

    elif userName==user_name and password==pass_word: 
        print("Welcome to my page!")
        break
    
    elif userName!=user_name and password!=pass_word:
        print("You have entered wrong username and password!")
        userName=input("Enter you username again!")
        password=input("Enter password:")
        count+=1
        continue

    elif userName==user_name and password!=pass_word:
        print("You have entered wrong password!")
        userName=input("Enter you username again!")
        password=input("Enter password:")
        count+=1
        continue
    elif userName!=user_name and password!=pass_word:
        print("You have entered wrong username!")
        userName=input("Enter you username again!")
        password=input("Enter password:")
        count+=1
        continue

'''

'''6. Read doc.txt file using Python File handling concept and return only the even length string from
the file. Consider the content of doc.txt as given below:
Hello I am a file
Where you need to return the data string
Which is of even length
Make sure you return the content in The same link as it is present.

#solution

f=open('doc.txt','r')
x=f.read()
for w in doc.txt:
    if(len(w)%2)==0:
        print("True")
'''


#TASK SIX


'''1. Write a program in Python to find out the character in a string which is uppercase using list
comprehension.

solution:
s="abCdeFghIjklmNopqRstuvWxyZ"
text=[i for i in s if i.isupper()]
print("Uppercase element is:",text)

'''


'''
2. Write a program to construct a dictionary from the two lists containing the names of students and
their corresponding subjects. The dictionary should map the students with their respective subjects.
Let’s see how to do this using for loops and dictionary comprehension.
HINT - Use Zip function also
Sample input: students = ['Smit', 'Jaya', 'Rayyan'] subjects = ['CSE', 'Networking', 'Operating System']
Expected output: {‘Smit’ : ’CSE’ , ’Jaya’ : ’Networking’ , ’Rayyan’ : ’Operating System’

solution:
students = ['Smit', 'Jaya', 'Rayyan'] 
subjects = ['CSE', 'Networking', 'Operating System']
dict={i:j for i,j in zip(students,subjects)}
print(dict)
'''


'''3. Learn More about Yield, next and Generators
'''

'''4. Write a program in Python using generators to reverse the string.
Input String = “Consultadd Training

#solution:
def rev_str(text):
    l = len(text)
    for i in range(l-1,-1,-1):
        yield text[i]

for char in rev_str("Consultadd Training"):
    print(char,end=" ")
'''

'''5. Write an example on decorators.
def add_func1(x):
    def func_add2(y):
        return x+y
 
    return func_add2
 
add_value =add_func1(15)
 
print(add_value(10))
'''