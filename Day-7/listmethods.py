Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[200,20,40,60,70,10,80,220]
l
[200, 20, 40, 60, 70, 10, 80, 220]
sorted(l)
[10, 20, 40, 60, 70, 80, 200, 220]
l.sort()
l
[10, 20, 40, 60, 70, 80, 200, 220]
min(l)
10
max(l)
220
l.reverse()
l
[220, 200, 80, 70, 60, 40, 20, 10]
sorted(l,reverse=True)
[220, 200, 80, 70, 60, 40, 20, 10]
l=[290,300,50,60,30,20,100]
l
[290, 300, 50, 60, 30, 20, 100]
sorted(l,reverse=True)
[300, 290, 100, 60, 50, 30, 20]
l.index(60)
3
l.index(225)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    l.index(225)
ValueError: 225 is not in list
l.count(100)
1
l.count(1000)
0
l
[290, 300, 50, 60, 30, 20, 100]
l=m
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l=m
NameError: name 'm' is not defined
m=l
m
[290, 300, 50, 60, 30, 20, 100]
m.append(700)
m
[290, 300, 50, 60, 30, 20, 100, 700]
l
[290, 300, 50, 60, 30, 20, 100, 700]
n=l.copy(800)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    n=l.copy(800)
TypeError: list.copy() takes no arguments (1 given)
n.append(800)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    n.append(800)
NameError: name 'n' is not defined
len(l)
8
sum(ll)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    sum(ll)
NameError: name 'll' is not defined. Did you mean: 'l'?
sum(l)
1550
# 0 0.0 [] {} () set() False
any9[1,2,4,5,5,0,0,0,0,0])
SyntaxError: unmatched ')'
any([1,2,4,5,5,0,0,0,0,0])
True
all([1,2,4,5,5,0,0,0,0,0])
False
any([0,0,0,0])
False
all([1,2,3,4,5])
True
