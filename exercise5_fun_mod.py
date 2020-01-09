#Problem Statements on Functions

#1. Write Python Program to write function to Find HCF or GCD

'''
def hcf(m,n):
    list1=[i for i in range(1,m+1) if not m%i]
    list2=[i for i in range(1,n+1) if not n%i]
    return max(set(list1)&set(list2))

x,y=20,21
print('HCF of',x,'&',y,'is:',hcf(x,y))
'''

#2. Write Python Program to write to Find LCM of numbers

'''
def lcm(m,n):
    a,b=max(m,n),min(m,n)
    i=1
    while a*i%b:
        i+=1
    else:return a*i

x,y=11,13
print('LCM of {} & {} is:'.format(x,y),lcm(x,y))
'''

#3. Write Python Program to Make a Simple Calculator based on function

'''
print('Welcome to my calculator!!')
def sum(a,b):
    return a+b
def diff(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

ch=int(input('Menu:\n1.Addition\n2.Difference\n3.Multiplication\n4.Division\nEnter your choice:'))
x=float(input('Enter first number:'))
y=float(input('Enter second number:'))

if ch==1:
    print('Addition is:',sum(x,y))
elif ch==2:
    print('Difference is:',diff(x,y))
elif ch==3:
    print('Multiplication is:',mul(x,y))
elif ch==4:
    print('Division is:',div(x,y))
else:
    print('Invalid input provided')
'''

#4. Write a function to find Fibonacci series from a number.
'''
n=int(input('enter your no:'))
f1=0
f2=1
while f2!=n:
    f3=f1+f2
    f1=f2
    f2=f3
series = [f2]
for count in range(10):
    f3 = f1 + f2
    series.append(f3)
    f1 = f2
    f2 = f3
print(series)
'''

#5. Write a Python function to find whether the number if prime or not. def isPrime(num)
'''
def isPrime(num):
    for i in range(2,num):
        if num%i:
            print ('Prime Number')
        else:
            print ('Not prime number')
        break
isPrime(10)
'''

#Problem Statements on Modules

#1. Create a module with function to find area of circle, area of triangle and perimeter of circle.
# Demonstrate the use of these functions by importing module
'''
from ExModule1 import *
print(areaofcircle(8))

print(areaoftriangle(2,4))

print(perimeterofcircle(5))
'''

#2. Create a package named ‘cricket’ which will contain modules named batsman and bowler.
# Create following functions in respective modules.
# batsman: findaverage(runs,matches), strikerate(runs,balls)
# bowler: findavg(runs,wickets), economyrate(overs, runs)
# Import the package and call all these functions in your program

'''
from cricket import batsman,bowler

print(batsman.findaverage(11520,239-39))
print(batsman.strikerate(11520,12576))

print(bowler.findavg(9114,358))
print(bowler.economyrate(3213,9114))
print(bowler.strikerate(19278,358))
'''

