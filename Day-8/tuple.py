Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
t=(1,2,3,4,5)
t
(1, 2, 3, 4, 5)
t=()
t=(1,1,1,1,3,3,5)
t
(1, 1, 1, 1, 3, 3, 5)
t=(1,1.1,'trjf',[])
t
(1, 1.1, 'trjf', [])
t=(10,20,30)
t
(10, 20, 30)
h=(40,50,60)
h
(40, 50, 60)
t+h
(10, 20, 30, 40, 50, 60)
t*5
(10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30, 10, 20, 30)
t[1]
20
t[-3]
10
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
t[:3]
(10, 20, 30)
t[3:]
(40, 50)
t[:2]
(10, 20)
t[1:4]
(20, 30, 40)
t[2:]
(30, 40, 50)
t[::-1]
(50, 40, 30, 20, 10)
t=[-1:-4:-1]
SyntaxError: invalid syntax
t=[-4]
t[-1:-4:-1]
[-4]
t=(10,20,30,40,50)
t
(10, 20, 30, 40, 50)
t[-1:-4:-1]
(50, 40, 30)
t[::-1]
(50, 40, 30, 20, 10)
t[-1]
50
t[-1:-3:-1]
(50, 40)
10 in t
True
10 not in t
False
60 not in t
True
60 in t
False
len(t)
5
sorted(t)
[10, 20, 30, 40, 50]
min(t)
10
max(t)
50
sum(t)
150
t.count(10)
1
t.index(40)
3
t.index(10)
0
t=1,2,3,4,5,6
t
(1, 2, 3, 4, 5, 6)
a,b,c=(1,2,3)
a
1
b
2
c
3
a=(1,2,3)
a
(1, 2, 3)
x,y,z=a
x
1
y
2
z
3
t=(1,2,3,[4,5,6],7,8)
t
(1, 2, 3, [4, 5, 6], 7, 8)
t[3]
[4, 5, 6]
t[2]
3
t[5]
8
t[2]=4
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    t[2]=4
TypeError: 'tuple' object does not support item assignment
t[3].append(10)
t
(1, 2, 3, [4, 5, 6, 10], 7, 8)
