#Problem Statements: Lists

#1. Write a Python program to sum all the items in a list.

'''
l=[1,2,-8]
print('sum of item in',l,'is:',sum(l))
'''

'''
l=[1,2,-8]
sum=0
for i in l:
    sum+=i
print(sum)
'''

'''
l=[1,2,-8]
sum=0
while len(l)>0:
    sum+=l[-1]
    l.pop()
print(sum)
'''

'''
from functools import reduce
l=[1,2,-8]
sum=reduce(lambda x,y:x+y,l)
print(sum)
'''

#2. Write a Python program to multiplies all the items in a list.
'''
l=[5,2,-8]
mul=1
for i in l:
    mul*=i
print(mul)
'''
'''
from functools import reduce
l=[5,2,-8]
m=reduce(lambda x,y:x*y,l)
print('multiplies of items in',l,'is:',m)
'''

#3. Write a Python program to get the largest number from a list.
'''
l=[10,5,80,2,69]
print(max(l))
'''
'''
l=[1, 2, -8, 0]
m=l[0]
for i in l:
    if i > m:
        m = i
print(m)
'''

#4. Write a Python program to get the smallest number from a list.

'''
l=[10,5,80,2,69]
print(min(l))
'''

'''
l=[1, 2, -8, 0]
m=l[0]
for i in l:
    if i < m:
        m = i
print(m)
'''

#5. Write a Python program to count the number of strings where the string length is 2 or more
# and the first and last character are same from a given list of strings.
# Sample List : ['abc', 'xyz', 'aba', '1221'] Expected Result : 2

'''
list=['abc', 'xyz', 'aba', '1221']
print(len([i for i in list if len(i)>=2 and i[0]==i[-1]]))
'''

#6. Write a Python program to get a list, sorted in increasing order by
# the last element in each tuple from a given list of non-empty tuples.
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

'''
list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
tl=[]
for i in list:
    tl.append(i[::-1])
tl.sort()
result=[]
for i in tl:
    result.append(i[::-1])
print(result)
'''

'''
list=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#def last(n): return n[-1]
print(sorted(list,key=lambda x:x[-1]))
'''

#7. Write a Python program to remove duplicates from a list.
'''
l=[1,2,3,4,5,1,2,3,4,5,8]
print(list(set(l)))
'''

'''
l=[1,2,3,7,4,5,1,2,3,4,5,8]
for i in l:
    if l.count(i)>1:
        l.remove(i)
print(l)
'''

#8. Write a Python program to check a list is empty or not.
'''
l=[]
if l:print('List is not empty')
else: print('List is empty')
'''

#9. Write a Python program to clone or copy a list.
'''
l=[1,2,3]
lc=l.copy()
print(lc)
'''


#10. Write a Python program to find the list of words that are longer than n from a given list of words.
'''
l=['Hello','World','Python','Data','Science','Numpy','list','set','num']
print([i for i in l if len(i)>3])
'''

#11. Write a Python function that takes two lists
# and returns True if they have at least one common member.
'''
def Com_Mem(l1,l2):
    if (set(l1) & set(l2)):
        print(True)
    else:
        print(False)
l1=[1,2,3,4]
l2=[5,6,7,8]
Com_Mem(l1,l2)
'''

#12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']
'''
l=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print([l[i] for i in range(len(l)) if i not in [0,4,5]])

result=[]
for i in range(len(l)):
    if i==0 or i==4 or i==5:
        continue
    result.append(l[i])
print(result)
'''

#13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
'''
array=[[['*' for col in range(6)]for col in range(4)]for row in range(3)]
print(array)
'''
'''
a=[[['*']*6]*4]*3
print(a)
'''

#14. Write a Python program to print the numbers of a specified list after removing even numbers from it.
'''
l=[1,2,3,4,5,6,7,8,9,10]
print(l)
print([i for i in l if i%2])
'''

#15. Write a Python program to shuffle and print a specified list.
'''
import random
l1=[4,5,6]
random.shuffle(l1)
print(l1)
'''

#16. Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included).
'''
l1=list(range(1,31))
print([(i**2) for i in l1[:5]+l1[-5:]])
'''

#17. Write a Python program to generate and print a list except for the first 5 elements,
# where the values are square of numbers between 1 and 30 (both included).

'''
l1=list(range(1,31))
print([(i**2) for i in l1[5:]])
'''

#18. Write a Python program to generate all permutations of a list in Python.
'''
import itertools
l=[1,2,3]
print(list(itertools.permutations(l)))
'''

#19. Write a Python program to get the difference between the two lists.

'''
l1=[1,2,3,4]
l2=[3,4,5,6]
print(set(l1)^set(l2))
'''

#20. Write a Python program access the index of a list.

'''
l=[1,2,3,4,5,6]
print([(i,x) for i,x in enumerate(l)])
'''

#21. Write a Python program to convert a list of characters into a string.
'''
l=['a','b','c','d',5]
[print(i,end='') for i in l]
'''

#22. Write a Python program to find the index of an item in a specified list.
'''
l=[1,2,5,2,6,7,9]
print(l.index(6))
'''

#23. Write a Python program to flatten a shallow list.
'''
import itertools
l=[[1,2,3],['a','b','c'],[4],[-2,-8]]
print(list(itertools.chain(*l)))
'''

#24. Write a Python program to append a list to the second list.
'''
l1=[1,2,3,4,'a']
l2=[4,5,6,7]
print(l1+l2)
'''

#25. Write a Python program to select an item randomly from a list.
'''
import random
l=[1,2,3,4,5]
a=random.choice(l)
print(a)
'''

#26. Write a python program to check whether two lists are circularly identical.
'''
l1=[1,2,3,5,4,'a']
l2=[5,4,'a',1,2,3]
print(''.join(map(str,l1)) in ''.join(map(str,l2*2)))
print(''.join(str(i) for i in l1) in ''.join(str(i) for i in l2*2))
'''

#27. Write a Python program to find the second smallest number in a list.
'''
list=[10,20,10,10,30,40,50,15]
s=set()
new_list=[]
for i in list:
    if i not in s:
        s.add(i)
        new_list.append(i)
new_list.sort()
print(new_list[1])
'''

#28. Write a Python program to find the second largest number in a list.
'''
list=[10,20,30,40,50,50,15]
s=set()
new_list=[]
for i in list:
    if i not in s:
        s.add(i)
        new_list.append(i)
new_list.sort(reverse=True)
print(new_list[1])
'''


#29. Write a Python program to get unique values from a list.
'''
l=[1,2,8,7,5,1,3,6,4,0,9,2,7,0,3,9,7,5,4]
print(list(set(l)))
'''

#30. Write a Python program to get the frequency of the elements in a list.
'''
l=[1,2,8,5,1,3,6,4,0,9,2,0,3,9,5,4]
print({i:l.count(i) for i in l})
'''

#31. Write a Python program to count the number of elements in a list within a specified range.

'''
l=[1,2,8,5,7,1,3,6,4,0,7,9,2,0,3,9,5,4]
print(len([i for i in l if 4<i<10 ]))
'''

#32. Write a Python program to check whether a list contains a sublist.
'''
l=[1,2,8,5,1,3,6,4,0,9,7,2,0,3,9,5,4]
s=[1,2,7]
if s==[]:
    print(True)
elif s==l:
    print(True)
elif ''.join([str(i) for i in s]) in ''.join([str(i) for i in l]):
    print(True)
else:
    print(False)
'''

#33. Write a Python program to generate all sublists of a list.
'''
import itertools
l=['X','Y','Z']
r=[list(j) for i in range(len(l)+1) for j in itertools.combinations(l,i)]
print(r)
'''

#34. Write a Python program using Sieve of Eratosthenes method
# for computing primes upto a specified number.

'''
n=int(input('Enter a number:'))
list=list(range(2,n+1))
Comp_List=[]
Prime_List=[]
for i in list:
    if i not in Comp_List:
        Prime_List.append(i)
        for j in range(i*2,n+1,i):
            Comp_List.append(j)
print(Prime_List)
print(Comp_List)
'''

'''
def prime_eratosthenes(n):
    prime_list = []
    l=[]
    for i in range(2, n+1):
        if i not in prime_list:
            l.append(i)
            for j in range(i*2, n+1, i):
                prime_list.append(j)
    print(l)
    return prime_list

print(prime_eratosthenes(100))
'''

#35. Write a Python program to create a list by concatenating a given list
# which range goes from 1 to n.
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

'''
list=['p','q']
n=int(input('Enter range:'))
print([i+str(j) for j in range(1,n+1) for i in list])
'''

#36. Write a Python program to get variable unique identification number or string.
'''
x=100
print(format(id(x),'x'))
n='narendra'
print(format(id(n),'b'))
'''

#37. Write a Python program to find common items from two lists.
'''
l1=[1,2,3,4,5]
l2=[4,5,6,7,8]
print(set(l1)&set(l2))
'''

#38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]

'''
list=[0,1,2,3,4,5]
for i in range(0,len(list)-1,2):
    list[i],list[i+1]=list[i+1],list[i]
print(list)
'''

#39. Write a Python program to convert a list of multiple integers into a single integer.
# Sample list: [11, 33, 50] Expected Output: 113350

'''
list=[11,33,50]
print(int(''.join(str(i) for i in list)))
'''

#40. Write a Python program to split a list based on first character of word.
'''
l=['apple','bat','cat','ant','dog','any','ball','doll','carrom']
la=[]
lb=[]
lc=[]
ld=[]
for i in l:
    if i[0]=='a':
        la.append(i)
    elif i[0]=='b':
        lb.append(i)
    elif i[0]=='c':
        lc.append(i)
    else: ld.append(i)
print('List of a:',la)
print('List of b:',lb)
print('List of c:',lc)
print('List of d:',ld)
'''

'''
from itertools import groupby
from operator import itemgetter

word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    print(list(words))
'''

#41. Write a Python program to create multiple lists.
'''
print([[] for i in range(20)])
'''

#42. Write a Python program to find missing and additional values in two lists.
# Sample data :
# Missing values in second list: b,a,c
# Additional values in second list: g,h

'''
l1=['a','b','c','d','e','f']
l2=['d','e','f','g','h']
print('Missing values in second list:',set(l1)-set(l2))
print('Additional values in second list:',set(l2)-set(l1))
'''

#43. Write a Python program to split a list into different variables.

'''
v1,v2,v3=[('a','b','c'),('d','e'),('f')]
print(v1,v2,v3)
'''

#44. Write a Python program to generate groups of five consecutive numbers in a list.
'''
l=[5,6,8,7,9,1,2,3,5,6,4,8,5,0,2,9,7,3,5]
for i in range(0,len(l),5):
    print(l[i:5+i])
'''

#45. Write a Python program to convert a pair of values into a sorted unique array.

'''
L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),(7, 8), (9, 10)]
print("Original List: ", L)
print("Sorted Unique Data:",sorted(set().union(*L)))
'''

#46. Write a Python program to select the odd items of a list.

'''
l=[5,2,3,6,7,8,9,1,2,5,6,7,3,2,9,1,8]
print([i for i in l if i%2])
'''

#47. Write a Python program to insert an element before each element of a list.
'''
l=['a','b','c','d','e','f']
[l.insert(i,'*') for i in range(0,len(l)*2,2)]
print(l)


l=['a','b','c','d','e','f']
print([v for i in l for v in ['*',i]])
'''

#48. Write a Python program to print a nested lists(each list on a new line)
# using the print() function.
'''
l=[[1,2,3,4,5],[6,7,8,9],[10,11,12],[13,14],[15],['Black']]
[print(i) for i in l]

colors = [['Red'], ['Green'], ['Black']]
print('\n'.join([str(lst) for lst in colors]))
'''

#49. Write a Python program to convert list to list of dictionaries.
# Sample lists:
# ["Black", "Red", "Maroon", "Yellow"],
# ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output:
# [{'color_name': 'Black', 'color_code': '#000000'},
# {'color_name': 'Red', 'color_code': '#FF0000'},
# {'color_name': 'Maroon', 'color_code': '#800000'},
# {'color_name': 'Yellow', 'color_code': '#FFFF00'}]

'''
color=["Black", "Red", "Maroon", "Yellow"]
code=["#000000", "#FF0000", "#800000", "#FFFF00"]
print([{'color_name':i[0],'color_code':i[1]} for i in zip(color,code)])
'''

#50. Write a Python program to sort a list of nested dictionaries.

'''
l=[{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
print(sorted(l,key=lambda x:x['key']['subkey'],reverse=True))
'''

#51. Write a Python program to split a list every Nth element.
# Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]

'''
list=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
n=int(input('Enter n:'))
print([[list[i] for i in range(j*1,len(list),n)] for j in range(n)])
print([list[i::n] for i in range(n)])
'''

#52. Write a Python program to compute the similarity between two lists.
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output: Color1-Color2: ['white', 'orange', 'red'] Color2-Color1: ['black', 'yellow']

'''
from collections import Counter
color1=["red", "orange", "green", "blue", "white"]
color2=["black", "yellow", "green", "blue"]
c1=(Counter(color1))
c2=(Counter(color2))
print('Color1-Color2:',list(c1-c2))
print('Color2-Color1:',list(c2-c1))
print('Color2&Color1:',list(c2&c1))
'''

#53. Write a Python program to create a list with infinite elements.
'''
l=[]
i=0
while True:
    l.append(i)
    i+=1
    print(l)
'''

#54. Write a Python program to concatenate elements of a list.
'''
l=['n','a','r','e','n','d','r','a','@',1,2,3]
print(''.join(str(i) for i in l))
'''

#55. Write a Python program to remove key values pairs from a list of dictionaries.
'''
l=[{'a':1,'b':2},{'a':3,'b':4}]
print([{k:v} for i in l for k,v in i.items() if k!='a'])
'''

#56. Write a Python program to convert a string to a list.
'''
s='narendra@123'
print([i for i in s])
'''

#57. Write a Python program to check if all items of a list is equal to a given string.
'''
s='narendra@123'
l=['n', 'a', 'r', 'e', 'n', 'd', 'r', 'a', '@', '1', '2', '3']
print(all([s[i]==l[i] for i in range(len(s))]))
'''
'''
color1 = ["green", "orange", "black", "white"]
color2 = ["green", "green", "green", "green"]
print(all(c == 'blue' for c in color1))
print(all(c == 'green' for c in color2))
'''

#58. Write a Python program to replace the last element in a list with another list.
# Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]
'''
l1=[1, 3, 5, 7, 9, 10]
l2=[2, 4, 6, 8]
l1.pop()
l1.extend(l2)
print(l1)
'''
'''
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]
num1[-1:] = num2
print(num1)
'''

#59. Write a Python program to check if the n-th element exists in a given list.
'''
l=[1,2,3,4,5]
n=int(input('Enter n:'))
if n<=len(l): print(True)
else: print(False)
'''

#60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
'''
l=[(1,2),(4,3),(6,5),(7,8),(2,3),(7,5),(6,8)]
print(min(sorted(l,key=lambda x:x[1])))
'''

#61. Write a Python program to create a list of empty dictionaries.
'''
print([{} for k in range(5)])
'''

#62. Write a Python program to print a list of space-separated elements.

'''
l=['n', 'a', 'r', 'e', 'n', 'd', 'r', 'a']
[print(i,end=' ') for i in l]
print(*l)
'''

#63. Write a Python program to insert a given string at the beginning of all items in a list.
# Sample list : [1,2,3,4], string : emp
# Expected output : ['emp1', 'emp2', 'emp3', 'emp4']
'''
l=[1,2,3,4]
s=input('Enter string:')
print([s+str(i) for i in l])
'''

#64. Write a Python program to iterate over two lists simultaneously.

'''
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
[print(l1[i],l2[i]) for i in range(len(l1))]
[print(a,b) for a,b in zip(l1,l2)]
'''

#65. Write a Python program to access dictionary keys element by index.
'''
d={0:'a',1:'b',2:'c'}
print(list(d)[2])
'''

#66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]
'''
l=[[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
s=[sum(i) for i in l]
print(l[s.index(max(s))])

num = [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
print(max(num, key=sum))
'''

#67. Write a Python program to find all the values in a list are greater than a specified number.
'''
l=[1,3,8,7,9,5,6,4,2,0]
print([i for i in l if i>5])
'''

#68. Write a Python program to extend a list without append.
# Sample data: [10, 20, 30] [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]
'''
l1=[10, 20, 30]
l2=[40, 50, 60]
print(l2+l1)
l1[:0]=l2
print(l1)
'''

#69. Write a Python program to remove duplicates from a list of lists.
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

'''
l=[[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
n=[]
[n.append(i) for i in l if i not in n]
print(n)
'''

#70. Write a Python program to get the depth of a dictionary.
'''
def dict_depth(d):
    if isinstance(d, dict):
        return 1 + (max(map(dict_depth, d.values())) if d else 0)
    return 0
dic = {'a':1, 'b': {'c': {'d': {}}},'e':{'f':{'g':{'h':{'i':{'j':{}}}}}}}
print(dict_depth(dic))
'''

'''
dic = {'a':1, 'b': {'c': {'d': {}}}}
count = 0
for x in str(dic):
    if x == '{':
        count+= 1
print(count)
'''

#71. Write a Python program to check if all dictionaries in a list are empty or not.
# Sample list : [{},{},{}] Return value : True
# Sample list : [{1:2},{},{}] Return value : False

'''
l=[{},{},{}]
print(all([not i for i in l]))
'''
