#Write a program to detect double spaces in a string
#Replace the double spaces from problem 3 with single spaces.
#write a program to format the following letter using escape sequence characters

text = "Dear students, This python course is going well.Thnaks"
if" " in text:
    print("double space is detected")
    
else:
    print("there is no double space")
    
    
    #2
   
replaced = text.replace(" "," ")
print(replaced)

#3
text = "Dear students\n\tThis python course is going well.\nThnaks"