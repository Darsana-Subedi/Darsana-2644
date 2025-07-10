#write a program to print the sum of 2 number entered by the user

sum1 = float(input("enter any numbers : "))
sum2 = float(input("enter any numbers : "))
total = sum1 + sum2
print("total = " , total)#write a python to find reminder when a number is divided by 2

sum= int(input("enter any number"))
reminder = sum % 2
print(reminder)#check the type of the variable assigned input() fumction

value= int(input("enter any number"))
print(type(value))
# use the comparision operators to find out whether a variable is greater than b or not

a=34
b=80
result=a>b
print(f"the variable a is greater than b : {result}")

#write a python program to calculate square a numbers entered by the user

a=int(input("enter the value : "))
total1=a**2
print(f"the square value : {total1}")

#write a python to display a user centered nmae followed by good afternoon using input()function
name=input("enter your Name")
print(f"Good Afternoon {name}")

from os import replace
#WAP to fill in a letter template given below with name and date
letter ='''Dear <|Name|>,
          you are selected !
             <|Date|>'''


username=input("Enter you name to see the result :")
Date=input("enter the full date you participated :")

letter=letter.replace("<|Name|>", username)
letter=letter.replace("<|Date|>",Date)

print(letter)
#wap to detect double space in a string
sentence=input("Enter your sentence")
if " " in sentence :
  print("Please, Aviod double spacing (    )")
else:
  print("No double space found")
# Replace the double space from the sentence with a single space

sentence1 = input("Enter your sentence: ")
sentence2 = sentence1.replace("  ", " ")  # Replace double spaces

print("Original sentence:", sentence1)
print("Fixed sentence   :", sentence2)