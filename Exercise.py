#Problem Statements : if-else

#1. Write a Python program to find maximum between two numbers.
'''
x=int(input('Enter first number:'))
y=int(input('Enter second number:'))
if x>=y:
    largest=x
else:largest=y
print('The maximum number between',x,'and',y,'is',largest)
'''

#2. Write a Python program to find maximum among three numbers.
'''
x = int(input('Enter first number:'))
y = int(input('Enter second number:'))
z = int(input('Enter third number:'))
if x>=y and x>=z:
    print('Maximum is:', x)
elif y>=z:
    print('Maximum is:', y)
else:
    print('Maximum is:', z)
'''

#3. Write a Python program to check whether a number is negative, positive or zero.
'''
x = int(input('Enter a number:'))
if x<0:
    print(x,'is negative number')
elif x>0:
    print(x,'is positive number')
else:
    print(x,'is zero')
'''

#4. Write a Python program to check whether a number is divisible by 5 and 11 or not.
'''
x = int(input('Enter a number:'))
if x%5==0 and x%11==0:
    print(x,'is divisible by 5 and 11')
elif x%5==0:
    print(x,'is divisible by 5 only')
elif x%11==0:
    print(x,'is divisible by 11 only')
else:
    print(x,'is not divisible by 5 and 11')
'''

#5. Write a Python program to check whether a number is even or odd.
'''
x = int(input('Enter a number:'))
if x%2==0:
    print('Given number',x,'is even')
else: print('Given number',x,'is odd')
'''

#6. Write a Python program to check whether a year is leap year or not.
'''
year=int(input('Enter a year:'))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,'is leap year')
        else:
            print(year,'is not leap year')
    else:
        print(year,'is leap year')
else:
    print(year,'is not leap year')

'''
'''
if year%400==0:
    print(year,'is leap year')
elif year%100==0:
    print(year,'is not leap year')
elif year%4==0:
    print(year,'is leap year')
else: print(year,'is no leap year')
'''

#7. Write a Python program to check whether a character is alphabet or not.
'''
char=input('Enter any character:')
if 'a'<=char>='z' or 'A'<=char>='Z':
    print('Given',char,'is an alphabet')
else: print('Given',char,'is not an alphabet')
'''

#8. Write a Python program to input any alphabet and check whether it is vowel or consonant.
'''
alphabet=input('Enter any alphabet:')
vowels=['a','e','i','o','u','A','E','I','O','U']
if alphabet in vowels:
    print('Given',alphabet,'is a vowel')
else: print('Given',alphabet,'is consonant')
'''
'''
alphabet=input('Enter any alphabet:')
if alphabet=='a'or 'e' or 'i' or 'o' or 'u' or 'A' or 'E' or 'I' or 'O' or 'U':
    print('Given',alphabet,'is a vowel')
else: print('Given',alphabet,'is consonant')
'''

#9. Write a Python program to check whether a character is uppercase or lowercase alphabet.
'''
char=input('Enter any character:')
if char.isupper():
    print('Given',char,'is an uppercase alphabet')
elif char.islower():
    print('Given',char,'is a lowercase alphabet')
else:
    print('Given',char,'is not an alphabet')
'''

#10.Write a Python program to count total number of notes in given amount.
'''
amt=int(input('Enter amount:'))
if amt>=2000:
    note2000=amt//2000
    print('Notes of 2000:', note2000)
    amt-=note2000*2000
if amt >= 500:
    note500 = amt // 500
    print('Notes of 500:', note500)
    amt -= note500 * 500
if amt >= 200:
    note200 = amt // 200
    print('Notes of 200:', note200)
    amt -= note200 * 200
if amt >= 100:
    note100 = amt // 100
    print('Notes of 100:', note100)
    amt -= note100 * 100
if amt >= 50:
    note50 = amt // 50
    print('Notes of 50:', note50)
    amt -= note50 * 50
if amt >= 20:
    note20 = amt // 20
    print('Notes of 20:', note20)
    amt -= note20 * 20
if amt >= 10:
    note10 = amt // 10
    print('Notes of 10:', note10)
    amt -= note10 * 10
if amt >= 5:
    note5 = amt // 5
    print('Notes of 5:', note5)
    amt -= note5 * 5
if amt >= 2:
    note2 = amt // 2
    print('Notes of 2:', note2)
    amt -= note2 * 2
if amt >= 1:
    note1 = amt // 1
    print('Notes of 1:', note1)
'''


#11.Write a Python program to input angles of a triangle and check whether triangle is valid or not.
'''
x=int(input('Enter an angle of triangle:'))
y=int(input('Enter second angle of triangle:'))
z=int(input('Enter third angle of triangle:'))
if x>0 and y>0 and z>0:
    if x+y+z==180:
        print('Triangle is valid')
else: print('Triangle is not valid')
'''

#12.Write a Python program to input all sides of a triangle and check whether triangle is valid or not.
'''
x=int(input('Enter a side of triangle:'))
y=int(input('Enter second side of triangle:'))
z=int(input('Enter third side of triangle:'))
if x>0 and y>0 and z>0:
    if x+y>z or y+z>x or x+z>y:
        print('Triangle is valid')
else: print('Triangle is not valid')
'''

#13.Write a Python program to check whether the triangle is equilateral, isosceles or scalene triangle.
'''
x=int(input('Enter a side of triangle:'))
y=int(input('Enter second side of triangle:'))
z=int(input('Enter third side of triangle:'))
if x==y==z:
    print('Given triangle is equilateral')
elif x==y!=z or y==z!=x or z==x!=y:
    print('Given triangle is isosceles')
elif x!=y!=z:
    print('Given triangle is scalene')
else:
    print('Enter a valid measures of triangle')
'''

#14.Write a Python program to calculate profit or loss. Input is selling cost and actual cost.
'''
x=int(input('Enter the actual cost:'))
y=int(input('Enter the selling cost:'))
if x>y:
    print('Loss=',x-y)
elif x<y:
    print('Profit=',y-x)
else:print('No profit No loss')
'''

#15.Write a Python program to input marks of five subjects Physics, Chemistry, Biology, Mathematics and Computer.
# Calculate percentage and grade according to following:
# Percentage >= 90% : Grade A
# Percentage >= 80% : Grade B
# Percentage >= 70% : Grade C
# Percentage >= 60% : Grade D
# Percentage >= 40% : Grade E
# Percentage < 40% : Grade F
'''
sub1=float(input('Enter the marks of Physics:'))
sub2=float(input('Enter the marks of Chemistry:'))
sub3=float(input('Enter the marks of Biology:'))
sub4=float(input('Enter the marks of Mathematics:'))
sub5=float(input('Enter the marks of Computer:'))
percentage=(sub1+sub2+sub3+sub4+sub5)/5
if percentage>=90:
    print('Percentage=',percentage,'% : Grade A')
elif percentage>=80:
    print('Percentage=',percentage,'% : Grade B')
elif percentage>=70:
    print('Percentage=',percentage,'% : Grade C')
elif percentage>=60:
    print('Percentage=',percentage,'% : Grade D')
elif percentage>=40:
    print('Percentage=',percentage,'% : Grade E')
else:
    print('Percentage=',percentage,'% : Grade F')
'''

#16.Write a Python program to input basic Python salary of an employee and
# calculate its Gross salary according to following:
# Basic Salary <= 10000 : HRA = 20%, DA = 80%
# Basic Salary <= 20000 : HRA = 30%, DA = 90%
# Basic Salary > 20000 : HRA = 35%, DA = 95%
'''
BS=int(input('Enter Basic Salary:'))
if BS<=10000:
    HRA=20/100*BS
    DA=80/100*BS
    Gross=BS+HRA+DA
    print('Basic Salary=',BS,', HRA=',HRA,', DA=',DA,', Gross Salary=',Gross)
elif BS<=20000:
    HRA=30/100*BS
    DA=90/100*BS
    Gross=BS+HRA+DA
    print('Basic Salary=',BS,', HRA=',HRA,', DA=',DA,', Gross Salary=',Gross)
else:
    HRA=35/100*BS
    DA=95/100*BS
    Gross=BS+HRA+DA
    print('Basic Salary=',BS,', HRA=',HRA,', DA=',DA,', Gross Salary=',Gross)
'''

#17.Write a Python program to input electricity unit charges and
# calculate total electricity bill according to the given condition:
# For first 50 units Rs. 0.50/unit
# For next 100 units Rs. 0.75/unit
# For next 100 units Rs. 1.25/unit
# For unit above 250 Rs. 1.50/unit
# An additional surcharge of 17% is added to the bill
'''
Units=float(input('Enter total units:'))
if 0<=Units<=50:
    UCharges=0.50*Units
elif 50<Units<=150:
    UCharges=0.50*50
    Units-=50
    UCharges+=0.75*Units
elif 150<Units<=250:
    UCharges=0.50*50
    Units-=50
    UCharges+=0.75*100
    Units-=100
    UCharges+=1.25*Units
else:
    UCharges=0.50*50
    Units-=50
    UCharges+=0.75*100
    Units-=100
    UCharges+=1.25*100
    Units-=100
    UCharges+=1.50*Units
Surcharge=17/100*UCharges
print('Electricity bill amount is',UCharges+Surcharge)
'''
