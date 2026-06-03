Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
float(a)
10.0
complex(a)
(10+0j)
str(a)
'10'
list(a)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
tuple(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
dict
<class 'dict'>
(
dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
bool(a)
True
f=10.10
int(f)
10
complex(f)
(10.1+0j)
string(f)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    string(f)
NameError: name 'string' is not defined
str(a)
'10'
list(f)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
bool(f)
True
c=11+1j
int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(c)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
float(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(c)
TypeError: float() argument must be a string or a real number, not 'complex'
str(f)
'10.1'
list(f)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(f)
TypeError: 'float' object is not iterable
tuple(f)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    tuple(f)
TypeError: 'float' object is not iterable
set(f)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    set(f)
TypeError: 'float' object is not iterable
dict(f)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(f)
TypeError: 'float' object is not iterable
bool(f)
True
s='python'
s='454632'
s='7589.4433'
int(s)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: '7589.4433'
s='python'
a='12349'
b='1234.5678'
int(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    int(s)
ValueError: invalid literal for int() with base 10: 'python'
int(a)
12349
int(b)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    int(b)
ValueError: invalid literal for int() with base 10: '1234.5678'
float(s)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    float(s)
ValueError: could not convert string to float: 'python'
float(a)
12349.0
float(b)
1234.5678
list(s)
['p', 'y', 't', 'h', 'o', 'n']
list(a)
['1', '2', '3', '4', '9']
list(b)
['1', '2', '3', '4', '.', '5', '6', '7', '8']
tuple(s)
('p', 'y', 't', 'h', 'o', 'n')
tuple(a)
('1', '2', '3', '4', '9')
tuple(b)
('1', '2', '3', '4', '.', '5', '6', '7', '8')
set(s)
{'p', 'y', 't', 'o', 'n', 'h'}
set(a)
{'9', '1', '3', '2', '4'}
set(b)
{'8', '5', '1', '3', '2', '7', '4', '.', '6'}
dict(s)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(a)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    dict(a)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
dict(b)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    dict(b)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
bool(a)
True
bool(s)
True
bool(b)
True
l=[1,2,3,4,5,6]
l
[1, 2, 3, 4, 5, 6]
int(l)
Traceback (most recent call last):
  File "<pyshell#59>", line 1, in <module>
    int(l)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list'
float(l)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    float(l)
TypeError: float() argument must be a string or a real number, not 'list'
complex(l)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    complex(l)
TypeError: complex() first argument must be a string or a number, not 'list'
tuple
<class 'tuple'>
tuple(l)
(1, 2, 3, 4, 5, 6)
set(l)
{1, 2, 3, 4, 5, 6}
dict(l)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict(l)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(l)
True
t=(1,2,3,4)
t
(1, 2, 3, 4)
iny(t)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    iny(t)
NameError: name 'iny' is not defined. Did you mean: 'any'?
int(t)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    int(t)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'tuple'
float(t)
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    float(t)
TypeError: float() argument must be a string or a real number, not 'tuple'
complex(t)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    complex(t)
TypeError: complex() first argument must be a string or a number, not 'tuple'
str(t)
'(1, 2, 3, 4)'
list(t)
[1, 2, 3, 4]
aet(t)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    aet(t)
NameError: name 'aet' is not defined. Did you mean: 'set'?
set(t)
{1, 2, 3, 4}
dict(t)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    dict(t)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(t)
True
s={1,2,3}
s
{1, 2, 3}
int(s)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    int(s)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'set'
float(s)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    float(s)
TypeError: float() argument must be a string or a real number, not 'set'
str(s)
'{1, 2, 3}'
list(s)
[1, 2, 3]
tuple(s)
(1, 2, 3)
set(s)
{1, 2, 3}
dict(s)
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    dict(s)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
bool(s)
True
complex(s)
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    complex(s)
TypeError: complex() first argument must be a string or a number, not 'set'
d={'name':'hny','rno':'508'}
int(d)
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    int(d)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'dict'
float(d)
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    float(d)
TypeError: float() argument must be a string or a real number, not 'dict'
