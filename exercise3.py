#Problems on strings:

#1. Write a Python program to calculate the length of a string.
'''
print('calculate the length of a string.')
s=input('Enter a string:')
print('length of given string is:',len(s))
'''

#2. Write a Python program to count the number of characters (character frequency) in a string.
# Sample String : 'google.com'
# Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
'''
print('count the number of characters (character frequency) in a string')
s=input('Enter a string:')
d={}
for i in s:
    dict={i:s.count(i)}
    #print(dict)
    d.update(dict)
print(d)
'''

#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.
# Sample String : ‘skillologies' Expected Result : 'skes'
# Sample String : 'mi' Expected Result : 'mimi'
# Sample String : ' m' Expected Result : Empty String
'''
print('to get a string made of the first 2 and the last 2 chars from a given a string')
s=input('Enter a string:')
if len(s)>=2:
    print(s[0],s[1],s[-2],s[-1],sep='',end=' ')
else:print('Empty string')
'''

#4. Write a Python program to get a string from a given string where
# all occurrences of its first char have been changed to '$', except the first char itself.
# Sample String : 'restart' Expected Result : 'resta$t'
'''
s=input('Enter a string:')
t=s.replace(s[0],'$')
for i in range(len(t)):
    if i==0:
        print(s[0],end='')
    else:
        print(t[i],end='')
'''

#5. Write a Python program to get a single string from two given strings,
# separated by a space and swap the first two characters of each string.
# Sample String : 'abc', 'xyz' Expected Result : 'xyc abz'
'''
s=input('Enter a first string:')
t=input('Enter a second string:')
a=s.replace(s[0],t[0])
b=a.replace(a[1],t[1])
c=t.replace(t[0],s[0])
d=c.replace(c[1],s[1])
print(b+' '+d)
'''
'''
s=input('Enter a first string:')
t=input('Enter a second string:')
for i in range(len(s)):
    if i>1:
      p=(s[i])
for i in range(len(t)):
    if i>1:
      q=(t[i])
print(t[0],t[1],p,' ',s[0],s[1],q,sep='',end='')
'''

#6. Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.
# Sample String : 'abc' Expected Result : 'abcing'
# Sample String : 'string' Expected Result : 'stringly'

'''
s=input('Enter a string:')
if len(s)>=3:
    if s.endswith('ing'):
        print(s.__add__('ly'))
    else:
        print(s.__add__('ing'))
else:
    print(s)
'''

#7. Write a Python program to find the first appearance of the substring 'not' and 'poor'
# from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'.
# Return the resulting string.
# Sample String : 'The lyrics is not that poor!' Expected Result : 'The lyrics is good!'

'''
s=input('Enter a string:')
a=int(s.find('not'))
print(a)
b=int(s.find('poor'))
print(b)
c=int(s.find('bad'))
print(c)
if (b>a) and a>0 and b>0:
    t=s.replace(s[a:(b+4)],'good')
    print(t)
if (c>a) and a>0 and c>0:
    t=s.replace(s[a:(c+3)],'good')
    print(t)
else: print(s)
'''

#8. Write a Python function that takes a list of words and returns the length of the longest one.

'''
def maxima():
    s=(input('Enter words:'))
    l=s.split()
    list=[]
    for i in l:
        list.append(len(i))
    m=max(list)
    for i in l:
        if len(i)==m:
            print(i,':',m)
maxima()
'''

#9. Write a Python program to remove the nth index character from a nonempty string.
'''
print('remove the nth index character from a nonempty string')
s=input('Enter a string:')
n=int(input('Enter nth index:'))
t=s.replace(s[n],'')
print(t)
'''

#10. Write a Python program to change a given string to a new string
# where the first and last chars have been exchanged.
'''
s=input('Enter a string:')
for i in range(len(s)):
    if i==0:
        print(s[-1],end='')
    elif i==(len(s)-1):
        print(s[0],end='')
    else:
        print(s[i],end='')
'''

#11. Write a Python program to remove the characters which have odd index values of a given string.
'''
s=input('Enter a string:')
for i in range(len(s)):
    if i%2:
        pass
    else:
        print(s[i],end='')
'''

#12. Write a Python program to count the occurrences of each word in a given sentence.
'''
s=input('Enter a string:')
t=s.split()
d=set(t)
l=list(d)
for i in range(len(l)):
    c=t.count(l[i])
    print(l[i],':',c)
'''

#13. Write a Python script that takes input from the user and displays that input back in upper and lower cases.

'''
s=input('Enter a string:')
u=s.upper()
l=s.lower()
print('Display in upper case',u)
print('Display in lower case',l)
'''

#14. Write a Python program that accepts a comma separated sequence of words as input and
# prints the unique words in sorted form (alphanumerically).
# Sample Words : red, white, black, red, green, black
# Expected Result : black, green, red, white.
'''
s=input('Enter a string:')
p=s.split(sep=',')
q=set(p)
t=list(q)
t.sort()
for i in range(len(t)):
    print(t[i],end='')
    if i==(len(t)-1):
        print('.')
    else: print(',',end='')
'''

#15. Write a Python function to create the HTML string with tags around the word(s).
# Sample function and result :
# add_tags('i', 'Python') -> '<i>Python</i>'
# add_tags('b', 'Python Tutorial') -> '<b>Python Tutorial </b>'

'''
def add_tags(a,b):
    print("'<",a,">",b,"</",a,">'",sep='')

s=input('Enter a string:')
t=input('Enter second string:')
add_tags(s,t)
'''

#16. Write a Python function to insert a string in the middle of a string.
# Sample function and result :
# insert_sting_middle('[[]]', 'Python') -> [[Python]]
# insert_sting_middle('<<>>', 'Python') -> <<Python>>
# insert_sting_middle('{{}}', 'PHP') -> {{PHP}}

'''
def insert_string_middle(a,b):
    for i in range(0,len(a)):
        if i==(len(a)/2):
            print(b,end='')
        print(a[i],end='')

s=input('Enter a string')
t=input('Enter second string')
insert_string_middle(s,t)
'''

#17. Write a Python function to get a string made of 4 copies of the last two characters
# of a specified string (length must be at least 2).
# Sample function and result :
# insert_end('Python') -> onononon
# insert_end('Exercises') -> eseseses
'''
def insert_end(s):
    if len(s)<2:
        print(s)
    else:
        t=s[len(s)-2:len(s)]
        print(t*4)
s=input('Enter a string:')
insert_end(s)
'''

#18. Write a Python function to get a string made of its first three characters of a specified string.
# If the length of the string is less than 3 then return the original string.
# Sample function and result :
# first_three('ipy') -> ipy
# first_three('python') -> pyt
'''
def first_three(s):
    if len(s)>=3:
        print(s[0:3])
    else:
        print(s)
s=input('Enter a string:')
first_three(s)
'''


#19. Write a Python program to get the last part of a string before a specified character.
# https://www.w3resource.com/python-exercises
# https://www.w3resource.com/python

'''
s=input('Enter a string:')
t=s[::-1]
l=''
for i in t:
    if i.isalnum():
        l+=i
    else: break
print(l[::-1])
'''


#20. Write a Python function to reverses a string if it's length is a multiple of 4.

'''
def reverse_string_mul4(s):
    if (len(s)%4):
        print(s)
    else:
        print(s[::-1])
s=input('Enter a string:')
reverse_string_mul4(s)
'''

#21. Write a Python function to convert a given string to all uppercase
# if it contains at least 2 uppercase characters in the first 4 characters.

'''
def all_upper_if2_in_first4(s):
    count=0
    for i in range(4):
        if s[i].isupper():
            count+=1
    if count>=2:
        print(s.upper())
    else:
        print(s)
s=input('Enter a string:')
all_upper_if2_in_first4(s)
'''

#22.Write a Python program to sort a string lexicographically.
'''
s=input('Enter a string:')
l=[]
[l.append(i) for i in s]
l.sort()
t=''
for i in l:
    t+=i
print(t)
'''

#23.Write a Python program to remove a newline in Python.
'''
s='ak\njd\nnrn\nsk\n'
print(s)
t=s.replace('\n','')
print(t)
'''

#24. Write a Python program to check whether a string starts with specified characters.
'''
s=input('Enter a string:')
n=input('specified character')
t=s.find(n)
if t==0:
    print('the string starts with the character')
else:
    print('the string does not start with the character')
'''

'''
s=input('Enter a string:')
#if 'a'<=s[0]<='z' or 'A'<=s[0]<='Z' or '0'<=s[0]<='9' or s[0]==' ':
if s[0].isalnum() or s[0].isspace():
    print('the string does not start with specified character')
else:
    print('the string starts with the character', s[0])
'''

#25. Write a Python program to create a Caesar encryption.
'''
s=input('Enter a string:')
for i in s:
    o=ord(i)
    print(chr(o+3),end='')
'''

#26. Write a Python program to display formatted text (width=50) as output.

'''
s='Python is a widely used high-level, general-purpose, interpreted,dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'
t=len(s)
i=0
while t>0:
    print(s[i:i+50],end='')
    print()
    i+=50
    t-=50
'''
'''
s='Python is a widely used high-level, general-purpose, interpreted,dynamic programming language. Its design philosophy emphasizes code readability, and its syntax allows programmers to express concepts in fewer lines of code than possible in languages such as C++ or Java.'
import textwrap
t=textwrap.fill(s,width=50)
print(t)
'''

#27. Write a Python program to remove existing indentation from all of the lines in a given text.

'''
s="    Python is a widely used high-level, general \n    purpose, interpreted,dynamic programming language. \n    Its design philosophy emphasizes code readability,\n    and its syntax allows programmers to express \n    concepts in fewer lines of code than possible in \n    languages such as C++ or Java."
import textwrap
t=textwrap.dedent(s)
print(t)
'''

'''
s="    Python is a widely used high-level, general \n    purpose, interpreted,dynamic programming language. \n    Its design philosophy emphasizes code readability,\n    and its syntax allows programmers to express \n    concepts in fewer lines of code than possible in \n    languages such as C++ or Java."
t=s.split('\n')
for i in t:
    j=i.lstrip()
    print(j)
'''

#28. Write a Python program to add a prefix text to all of the lines in a string.
'''
s="Python is a widely used high-level, general \npurpose, interpreted,dynamic programming language. \nIts design philosophy emphasizes code readability,\nand its syntax allows programmers to express \nconcepts in fewer lines of code than possible in \nlanguages such as C++ or Java."
t=s.split('\n')
for i in t:
    print('"This is prefix"',i)
'''
'''
import textwrap
s="Python is a widely used high-level, general \npurpose, interpreted,dynamic programming language. \nIts design philosophy emphasizes code readability,\nand its syntax allows programmers to express \nconcepts in fewer lines of code than possible in \nlanguages such as C++ or Java."
t=textwrap.indent(s,'"This is prefix"')
print(t)
'''

#29. Write a Python program to set the indentation of the first line.

'''
s="Python is a widely used high-level, general \npurpose, interpreted,dynamic programming language. \nIts design philosophy emphasizes code readability,\nand its syntax allows programmers to express \nconcepts in fewer lines of code than possible in \nlanguages such as C++ or Java."
print('    '+s)
'''

'''
s="Python is a widely used high-level, general \npurpose, interpreted,dynamic programming language. \nIts design philosophy emphasizes code readability,\nand its syntax allows programmers to express \nconcepts in fewer lines of code than possible in \nlanguages such as C++ or Java."
t=s.splitlines(False)
t[0]='    '+t[0]
for i in t:
    print(i)
'''

#30. Write a Python program to print the following floating numbers upto 2 decimal places.

'''
s=float(input('Enter float number:'))
print("Formatted Number: ",s.__round__(2))
print("Formatted Number: ",round(s,2))
print("Formatted Number: %.2f"%s)
print("Formatted Number: {:.2f}".format(s))
'''

#31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.

'''
s=float(input('Enter float number:'))
print("Formatted Number: ",+s.__round__(2))
print("Formatted Number: ",+round(s,2))
print("Formatted Number: %+.2f"%s)
print("Formatted Number: {:+.2f}".format(s))
'''

#32. Write a Python program to print the following floating numbers with no decimal places.

'''
s=float(input('Enter float number:'))
print("Formatted Number: ",s.__round__())
print("Formatted Number: ",round(s))
print("Formatted Number: %.0f"%s)
print("Formatted Number: {:.0f}".format(s))
'''

#33. Write a Python program to print the following integers with zeros on the left of specified width.
'''
s=input('Enter a integer:')
u=s.zfill(5)
print(u)
'''

'''
t=int(input('Enter a integer:'))
print('{:0>5d}'.format(t))
'''

#34. Write a Python program to print the following integers with '*' on the right of specified width.

'''
t=int(input('Enter a integer:'))
print('{:*<5d}'.format(t))
'''

#35. Write a Python program to display a number with a comma separator.
'''
n=int(input('Enter a number:'))
print('{:,}'.format(n))
'''

#36. Write a Python program to format a number with a percentage.
'''
f=float(input('Enter a number:'))
print('{:.2%}'.format(f))
'''

#37. Write a Python program to display a number in left, right and center aligned of width 10.
'''
x = int(input('Enter a number:'))
print("Left aligned (width 10)   :"+"{:< 10d}".format(x));
print("Right aligned (width 10)  :"+"{:10d}".format(x));
print("Center aligned (width 10) :"+"{:^10d}".format(x));
'''

#38. Write a Python program to count occurrences of a substring in a string.
'''
os=input("Enter original string:")
ss=input("Enter substring:")
print(os.count(ss))
'''

#39. Write a Python program to reverse a string.
'''
s=input('Enter a string:')
print(s[::-1])
'''

#40. Write a Python program to reverse words in a string.
'''
s=input('Enter a string:')
l=s.split()
t=' '.join(reversed(l))
print(t)
'''

#41. Write a Python program to strip a set of characters from a string.
'''
s=input('Enter  string:')
char=input('Enter a set of characters:')
for i in s:
    if i not in char:
        print(i,end='')
'''

#42. Write a python program to count repeated characters in a string.
# Sample string: 'thequickbrownfoxjumpsoverthelazydog'
# Expected output : o 4 e 3 u 2 h 2 r 2 t 2

'''
s=input('Enter a string:')
set=set(s)
#{print(j, s.count(j)) for j in set if s.count(j)>1}
for j in set:
    if s.count(j)>1:
        print(j, s.count(j))
'''

'''
s=input('Enter a string:')
from collections import Counter
c=Counter(s)
{print(k,v) for k,v in c.items() if v>1}
'''

#43. Write a Python program to print the square and cube symbol in the area of a rectangle and volume of a cylinder.
# Sample output: The area of the rectangle is 1256.66cm2
# The volume of the cylinder is 1254.725cm3

'''
area = 1256.66
volume = 1254.725
q=input('What you want to be printed?:')
if q=='area':
    print("The area of the rectangle is {}cm\u00b2".format(area))
elif q=='volume':
    print("The volume of the cylinder is {} cm\u00b3".format(volume))
else:
    print('Kindly give an input "area" or "volume"')
'''

#44. Write a Python program to print the index of the character in a string.
# Sample string: w3resource
# Expected output:
# Current character w position at 0
# Current character 3 position at 1
# Current character r position at 2
# - - - - - - - - - - - - - - - - - - - - - - - -
# Current character c position at 8
# Current character e position at 9

'''
s=input('Enter a string:')
for i in range(len(s)):
    print('Current character',s[i],'position at',i)
'''

#45. Write a Python program to check if a string contains all letters of the alphabet.
#The quick brown fox jumps over the lazy dog

'''
import string
s=set(input('Enter a string:'))
l=set(string.ascii_lowercase)
print(s>=l)
'''

#46. Write a Python program to convert a string in a list.
'''
s=input('Enter a string:')
l=[]
[l.append(i) for i in s]
print(l)
'''

#47. Write a Python program to lowercase first n characters in a string.

'''
s=input('Enter a string:')
n=int(input('Enter number of characters:'))
print(s[:n].lower()+s[n:])
'''

#48. Write a Python program to swap comma and dot in a string.
# Sample string: "32.054,23" Expected Output: "32,054.23"
'''
s=input('Enter a string:')
t=s.translate(s.maketrans(',.','.,'))
print(t)
'''

#49. WrIte a Python program to count and display the vowels of a given text.

'''
s=input('Enter a string:')
v='aeiouAEIOU'
print([i for i in s if i in v])
print(len([i for i in s if i in v]))
'''

#50. Write a Python program to split a string on the last occurrence of the delimiter.
'''
s=input('Enter a string:')
t=s.rsplit(',',1)
print(t)
'''
