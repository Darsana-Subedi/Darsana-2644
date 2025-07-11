# Given the string s = "PythonPractice", what are the outputs of:
  # - s[1]
   #- s[-3:]
   #- s[2:7] 
s="pythonpractice"
print(s[1])
print(s[-3:])
print(s[2:7])

# Write a one-liner to reverse the string "developer" using slicing.
s="pythonpractice"
reversed_s=s[::-1]
print(reversed_s)

#Write a function that counts the number of vowels in a given string.
def count_vowels(s):
    vowels="AEIOUaeiou"
    count=0
    for char in s:
      if char in vowels:
       count += 1
    return count
s = "pythonpractice"
print("number of vowels:", count_vowels(s))

# Write a function to check if a given string is a palindrome. Ignore spaces and capitalization.

def is_palindrome(s):
    s = s.replace(" ", "").lower()  
    return s == s[::-1]  
print(is_palindrome("Eve"))         # True
print(is_palindrome("malyalam"))            # False
print(is_palindrome("madam"))           

#Clean and Format String
   #Given text = "   hello world! welcome to Python.   ", write code to:
   #- Remove leading/trailing spaces
   #- Capitalize each word
   #- Replace the word "Python" with "Programming"
s = "   hello world! welcome to Python.   "
s = s.strip()
t = "   hello world! welcome to Python.   "
t = t.title()
te = "   hello world! welcome to Python.   "
te = te.replace("Python", "Programming")

print(s)
print(t)
print(te)

# Write a function that takes a sentence and returns the longest word in it.
def longest_word(sentence):
    words = sentence.split()               
    longest = max(words, key=len)         
    return longest

sentence = "Write a function that takes a sentence and returns the longest word in it"
print("Longest word:", longest_word(sentence))


 #Given s1 = "Py" and s2 = "thon", what are the results of:
  # - s1 + s2
   #- s1 * 3
   #- "y" in s1
   
s1="py" 
s2="thon"
print("s1 + s2 =", s1 + s2)      
print("s1 * 3 =", s1 * 3)       
print('"y" in s1 =', "y" in s1)


#Remove Duplicate Characters
#Write a function that removes all duplicate characters from a string but keeps the first occurrence.
def remove_duplicates(s):
    result = ""
    dupli = set()
    for char in s:
        if char not in dupli:
            result += char
            dupli.add(char)
    return result

# Example usage
text = "welcome"
print(remove_duplicates(text))  


#Check for Anagram
  # Write a function that returns True if two strings are anagrams of each other.
def are_anagrams(str1, str2):
    
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    
    return sorted(str1) == sorted(str2)


print(are_anagrams("listen", "silent"))    
print(are_anagrams("hello", "world"))      


#Word Frequency Counter
   # Write a function that takes a sentence and returns a dictionary of word frequencies.
def word_frequency(sentence):
    words = sentence.lower().split() 
    freq = {}

    for word in words:
        freq[word] = freq.get(word, 0) + 1 

    return freq

sentence = "Hello world hello"
print(word_frequency(sentence))
