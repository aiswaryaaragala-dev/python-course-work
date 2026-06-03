Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=20
b=20
a
20
b
20
a+b
40
a-b
0
a*b
400
a/b
1.0
a//b
1
a**b
104857600000000000000000000
a*2
40
6**b
3656158440062976
6**3
216
a%b
0
17%4
1
a
20
b
20
a<b
False
a<=b
True
a>b
False
a>=b
True
a==b
True
a!=b
False
y=5
y
5
y=y+5
y
10
y+=10
y
20
y+=10
y
30
y+=5
y
35
y-=5
y
30
y*=4
y
120
y//=10
y
12
y%=2
y
0
y/=2
y
0.0
y+=10
y
10.0
a=20
b=10
a%10==0
True
a%20==0 or b%20=0 or a>b
SyntaxError: cannot assign to expression
a%20==0 or b%20==0 or a>b
True
a%20==0 and b%20=0 and a>b
SyntaxError: cannot assign to expression
a%20==0 and b%20==0 and a>b
False
 not a>b
 
SyntaxError: unexpected indent
not a>b
False
a='python programming'
a
'python programming'
'y' in a
True
'g' in a
True
'q' in a
False
l=['java','python','mysql','c','html']
l
['java', 'python', 'mysql', 'c', 'html']
'html' in l
True
'c' in l
True
t=('laptop','mobile','mouse','keyboard')
t
('laptop', 'mobile', 'mouse', 'keyboard')
'mouse' in t
True
t=(1,2,3,4,9,8)
t
(1, 2, 3, 4, 9, 8)
5 in t
False
9 in t
True
d={'egg':8,'oil':120,'sugar':80}
d
{'egg': 8, 'oil': 120, 'sugar': 80}
'oil' in d
True
index[0]
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    index[0]
NameError: name 'index' is not defined
'egg' in d
True
l=[1,2,3,4,5]
l
[1, 2, 3, 4, 5]
m=[6,7,8,9,2]
l==m
False
n=m
n
[6, 7, 8, 9, 2]
n==m
True
l is m
False
n is m
True
id(l)
3220434586176
id(m)
3220434584064
id(n)
3220434584064
l is not m
True
n is not m
False
8&14
8
817
817
8|7
15
10^11
1
~14
-15
~26
-27
8>>2
2
15>>2
3
15>>3
1
16<<1
32

4<<2
16
