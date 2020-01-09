#Loop Control Structures:
#1. Write a Python program to print all natural numbers from 1 to n.
# - using while loop
'''
n=int(input('Enter the last natural number:'))
count=1
while count<=n:
    print(count, end=' ')
    count+=1
'''
#2. Write a Python program to print all natural numbers in reverse (from n to 1).
# - using while loop
'''
n=int(input('Enter the last natural number:'))
count=n
while count>=1:
    print(count, end=' ')
    count-=1
'''

#3. Write a Python program to print all alphabets from a to z.
# - using while loop
'''
char='a'
count=ord(char)
while count<=ord('z'):
    char=chr(count)
    print(char,end=' ')
    count+=1
'''

#4. Write a Python program to print all even numbers between 1 to 100. - using while loop

'''
count=2
while 1<=count<=100:
    print(count,end=' ')
    count+=2
'''

#5. Write a Python program to print all odd number between 1 to 100.
'''
count=1
while 1<=count<=100:
    print(count,end=' ')
    count+=2
'''

#6. Write a Python program to find sum of all natural numbers between 1 to n.
'''
n=int(input('Enter the last natural number:'))
count,sum=1,0
while 1<=count<=n:
    sum+=count
    count+=1
print('Sum of all natural numbers between 1 to',n,'is',sum)
'''

'''
n=int(input('Enter the last natural number:'))
sum=0
for i in range(1,n+1):
    sum+=i
print('Sum of all natural numbers between 1 to',n,'is',sum)
'''

#7. Write a Python program to find sum of all even numbers between 1 to n.
'''
print('Find sum of all even numbers between 1 to n')
n=int(input('Enter the "n":'))
sum, count=0,2
while count<=n:
    sum+=count
    count+=2
print('Sum of all even numbers between 1 to',n,'is',sum)
'''
'''
print('Find sum of all even numbers between 1 to n')
n=int(input('Enter the "n":'))
sum=0
for i in range(2,n+1,2):
    sum+=i
print('Sum of all even numbers between 1 to',n,'is',sum)
'''

#9. Write a Python program to find sum of all odd numbers between 1 to n.
'''
print('Find sum of all odd numbers between 1 to n')
n=int(input('Enter the "n":'))
sum,count=0,1
while count<=n:
    sum+=count
    count+=2
print('Sum of all odd numbers between 1 to',n,'is',sum)
'''

'''
print('find sum of all odd numbers between 1 to n')
n=int(input('Enter the "n":'))
sum=0
for i in range(1,n+1,2):
    sum+=i
print('Sum of all odd numbers between 1 to',n,'is',sum)
'''

#10.Write a Python program to print multiplication table of any number. Take user input.
'''
print('Multiplication table of any number')
n=int(input('Enter any number:'))
count=1
while count<=10:
    print(n*count)
    count+=1
'''
'''
print('Multiplication table of any number')
n=int(input('Enter any number:'))
for i in range(1,11):
    print(n*i)
'''

#11.Write a Python program to count number of digits in a number.
'''
print('Count number of digits in a number')
n=int(input('Enter any number:'))
count=0
while n>0:
    n//=10
    count+=1
print('Number of digits in the given number is',count)
'''

#12.Write a Python program to find first and last digit of a number.
'''
print('Find first and last digit of a number')
n=int(input('Enter a number:'))
last_digit=n%10
while n>10:
    n=n//10
first_digit=n
print('first digit and last digit of the given number is {} and {}'.format(first_digit,last_digit))
'''

#13.Write a Python program to find sum of first and last digit of a number.
'''
print('Find sum of first and last digit of a number')
n=int(input('Enter a number:'))
last_digit=n%10
while n>10:
    n=n//10
first_digit=n
print('sum of first and last digit of the given number is',first_digit+last_digit)
'''

#14.Write a Python program to swap first and last digits of a number.
'''
print('swap first and last digit of a number')
n=int(input('Enter a number:'))
m=n
last=m%10
while m>10:
    m=m//10
first=m
from math import log10
count=int(log10(n))
swap=last*pow(10,count)+first+(n-(first*pow(10,count)+last))
print('After swapping first and last digit of the given number, o/p is',swap)
'''

#15.Write a Python program to calculate sum of digits of a number.
'''
print('calculate sum of digits of a number')
n=int(input('Enter any number:'))
sum=0
while n>0:
    r=n%10
    sum+=r
    n//=10

print('sum of digits of the given number is',sum)
'''

#16.Write a Python program to calculate product of digits of a number.

'''
print('calculate product of digits of a number')
n=int(input('Enter any number:'))
product=1
while n>0:
    r=n%10
    product*=r
    n//=10

print('product of digits of the number is',product)
'''

#17.Write a Python program to enter a number and print its reverse.

'''
print('Enter a number and print its reverse.')
n=int(input('Enter a number:'))
reverse=0
from math import log10
while n>0:
    r=n%10
    count=int(log10(n))
    d=r*pow(10,count)
    reverse+=d
    n//=10
print('reversed to',reverse)
'''

#18.Write a Python program to check whether a number is palindrome or not.
'''
print('check whether a number is palindrome or not')
n=int(input('Enter a number:'))
m=n
reverse=0
from math import log10
while m>0:
    r=m%10
    count=int(log10(m))
    d=r*pow(10,count)
    reverse+=d
    m//=10
print('reversed to',reverse)
if n==reverse:
    print('Given number is palindrome.')
else:
    print('Given number is not palindrome.')
'''

#19.Write a Python program to find frequency of each digit in a given integer.
'''
print('find frequency of each digit in a given integer')
num=int(input('Enter a number:'))
for i in range(10):
    frq=0
    n=num
    while n!=0:
        last=n%10
        n//=10
        if i==last:
            frq+=1
    m=str(num)
    if str(i) in m:
        print(i,'=',frq)
'''

#20.Write a Python program to enter a digit and print it in words.
'''
print('Enter a digit and print it in words')
n=int(input('Enter a number:'))
i=str(n)
d1={1:'One',2:'Two',3:'Three',4:'Four',5:'Five',6:'Six',7:'Seven',8:'Eight',9:'Nine',0:'Zero'}
for j in i:
    k=int(j)
    if dict.keys(d1):
        print(d1[k],end=' ')
'''

#21.Write a Python program to find power of a number using for loop.
'''
print('find power of a number using for loop.')
n=int(input('Enter a number:'))
m=int(input('Enter a exponent:'))
power=1
for i in range(m):
    power*=n
print(power)
'''

#22.Write a Python program to calculate factorial of a number.
'''
print('calculate factorial of a number.')
n=int(input('Enter a number:'))
fact=1
while n>0:
    fact*=n
    n-=1
print(fact)
'''

#23.Write a Python program to find HCF (GCD) of two numbers.
'''
print('find HCF (GCD) of two numbers')
m=int(input('Enter first number:'))
n=int(input('Enter second number:'))
m_copy=m
n_copy=n
list1=[]
while m_copy>0:
    if m%m_copy==0:
        list1.append(m_copy)
    m_copy-=1
s1=(set(list1))
list2=[]
while n_copy>0:
    if n%n_copy==0:
        list2.append(n_copy)
    n_copy-=1
s2=(set(list2))
cd=s1.intersection(s2)
#print(cd)
print('GCD is:',max(cd))
'''

#24.Write a Python program to find LCM of two numbers.
'''
print('find LCM of two numbers')
x=int(input('Enter first number:'))
y=int(input('Enter second number:'))
m=max(x,y)
n=min(x,y)
i=1
while(m*i)%n!=0:
    i+=1
else: print('LCM is',m*i)
'''

#25.Write a Python program to check whether a number is Prime number or not.
'''
print('check whether a number is Prime number or not')
num=int(input('Enter a number:'))
i=(num-1)
while i>1:
    if num%i==0:
        print('Given number is composite')
        break
    i-=1
else: print('Given number is prime')
'''

#26.Write a Python program to print all Prime numbers between 1 to n.
'''
print('print all Prime numbers between 1 to n')
n=int(input('Enter a number:'))
list=[]
for i in range(2,n):
    j=i-1
    while j>1:
        if i%j==0:
            break
        j-=1
    else: list.append(i)
print('all Prime numbers between 1 to n are:',list)
'''

#27.Write a Python program to find sum of all prime numbers between 1 to n.
'''
print('find sum of all prime numbers between 1 to n')
n=int(input('Enter a number:'))
sum=0
for i in range(2,n):
    j=i-1
    while j>1:
        if i%j==0:
            break
        j-=1
    else: sum+=i
print('find sum of all prime numbers between 1 to n is:',sum)
'''

#28.Write a Python program to check whether a number is Armstrong number or not.
'''
print('check whether a number is Armstrong number or not')
n=int(input('Enter a number:'))
num=str(n)
l=len(num)
sum=0
for i in num:
    sum+=int(i)**l
print('Sum is:',sum)
if n==sum:
    print('Given number is Armstrong number')
else:print('Given number is not Armstrong number')
'''

#29.Write a Python program to print all Armstrong numbers between 1 to n.
'''
print('print all Armstrong numbers between 1 to n')
n=int(input('Enter a number:'))
list=[]
for i in range(1,n):
    num=str(i)
    l=len(num)
    sum=0
    for j in num:
        sum+=int(j)**l
    if i==sum:
        list.append(i)
print('all Armstrong numbers between 1 to n are:',list)
'''

#30.Write a Python program to print Fibonacci series up to n terms.
'''
print('print Fibonacci series up to n terms')
n=int(input('Enter a number:'))
list=[1,1]
for i in range(1,n-1):
    m=list[-1]+list[-2]
    list.append(m)
print(list)
'''

#31.Write a Python program to print the given star patterns.
# *
# * *
# * * *
# * * * *
# * * * * *
'''
print('print the given star patterns')
for i in range(1,6):
    print(i*'*',end='')
    print()
'''

#32.Write a Python program to print the given number patterns.
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
'''
print('print the given number patterns')
for i in range(1,6):
    print(i*str(i),end='')
    print()
'''

