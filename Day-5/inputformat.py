Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name=input()
honey
name
'honey'
name=input("enter your name:")
enter your name:Honey
name
'Honey'
age=input()
20
age
'20'
name
'Honey'
age=input("enter your age:")
enter your age:21
age
'21'
cgpa=float
cgpa=float(input("enter your cgpa:"))
enter your cgpa:8.0
cgpa
8.0
type(cgpa)
<class 'float'>
'honey','revathi','usha'
('honey', 'revathi', 'usha')
('honey', 'revathi', 'usha')
('honey', 'revathi', 'usha')
'honey revathi usha'
'honey revathi usha'
'honey revathi usha'.split('-')
['honey revathi usha']
['honey revathi usha']'honey revathi usha'.split(' ')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
'honey revathi usha'.split(' ')
['honey', 'revathi', 'usha']
names=input("enter the names:").split
enter the names:honey revathi usha 
names
<built-in method split of str object at 0x000002D803803A00>
names=input("enter the names:").split()
enter the names:honey revathi usha
names
['honey', 'revathi', 'usha']
topics=tuple(input("enter your topics:").split())
enter your topics:token statement
topics
('token', 'statement')
op=set(input("enter your oper:").split())
enter your oper:in not in is is not and or not
op
{'or', 'is', 'in', 'and', 'not'}
list(map(int,imput("enter your readings:").split()))
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    list(map(int,imput("enter your readings:").split()))
NameError: name 'imput' is not defined. Did you mean: 'input'?
list(map(int,input("enter your readings:").split()))
enter your readings:1 2 3 4 5 6
[1, 2, 3, 4, 5, 6]
prices=tuple(map(int,input("enter your readings:").split()))
enter your readings:1 3 33 4 55 
prices
(1, 3, 33, 4, 55)
rating=set(map(int,input("enter your reading:").split()))(1, 3, 33, 4, 55)
enter your reading:2 3  4 4  4
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    rating=set(map(int,input("enter your reading:").split()))(1, 3, 33, 4, 55)
TypeError: 'set' object is not callable
rating=set(map(int,input("enter your reading:").split()))
enter your reading:2 3 4 5 6
rating
{2, 3, 4, 5, 6}
percentage=list(map(int,input("enter your oper:").split()))
enter your oper:44.7 99.10 88.44
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    percentage=list(map(int,input("enter your oper:").split()))
ValueError: invalid literal for int() with base 10: '44.7'
percentage=list(map(int,input("enter your oper:").split()))
enter your oper:2 3 4
percentage
[2, 3, 4]
percentage=list(map(float,input("enter your oper:").split()))
enter your oper:44.7 88.9 77.0
\
percentage
[44.7, 88.9, 77.0]
[44.7, 88.9, 77.0]
[44.7, 88.9, 77.0]
prices=tuple(map(float,input("enter your prices:").split()))
enter your prices:60.9 77.9 4.9 66.8
prices
(60.9, 77.9, 4.9, 66.8)
a,b=10,20
a
10
b
20
a,b=[10,20]
a
10
b
20
username,password,=input("enter the username&password:").split()
enter the username&password:honey hny@123
username
'honey'
password
'hny@123'
a,b,c,d=list(map(int(input("enter the 4 sides:").split())))
enter the 4 sides:1 2 3 4 5
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    a,b,c,d=list(map(int(input("enter the 4 sides:").split())))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a,b,c,d=list(map(int(input("enter the 4 sides:").split())))

enter the 4 sides:2 0 2 0 3
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    a,b,c,d=list(map(int(input("enter the 4 sides:").split())))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a,b,c,d=list(map(int(input("enter the 4 sides:").split())))
enter the 4 sides:2 0 0 3
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    a,b,c,d=list(map(int(input("enter the 4 sides:").split())))
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
a,b,c,d=list(map(int,input("enter the 4 sides:").split()))
enter the 4 sides:2 0 0 3
a
2
b
0
c
0
d
3
prices,discount=list(map(float,input("enter the prices&discount:").split()))
enter the prices&discount:345 7 55 5
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    prices,discount=list(map(float,input("enter the prices&discount:").split()))
ValueError: too many values to unpack (expected 2)
prices,discount=list(map(float,input("enter the prices&discount:").split()))
enter the prices&discount:333 5
prices
333.0
discount
5.0
a=eval(input())
5678
a
5678
a=eval(input())
(1,2,3)
a
(1, 2, 3)
a=eval(input())
{1,2,3}
a
{1, 2, 3}
a=eval (input())
{3
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    a=eval (input())
  File "<string>", line 1
    {3
    
SyntaxError: '{' was never closed
;
a=eval(input())
     
{2:4 ,4:4}
a
     
{2: 4, 4: 4}
