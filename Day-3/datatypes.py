Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
a=10
type(a)
<class 'int'>
f=99.99
type(f)
<class 'float'>
c=11+11a
SyntaxError: invalid decimal literal
c=11=1a
SyntaxError: invalid decimal literal
c=11+1j
type(c)
<class 'complex'>
s='python'
type(s)
<class 'str'>
s="python"
type(s)
<class 'str'>
s='''python'''
type(s)
<class 'str'>
s='python'
s='java'
s
'java'
s='python'
id(s)
2104680893168
s='java'
id(s)
2104645013616
l[]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l=[]
l=list[]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l=list()
type(1)
<class 'int'>
type(l)
<class 'list'>
l=[1,2,3]
l.append[20]
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l.append[20]
TypeError: 'builtin_function_or_method' object is not subscriptable
l.append(10)
l.append(30)
l
[1, 2, 3, 10, 30]
t=()
t=(1,3,4,5,6)
t
(1, 3, 4, 5, 6)
t=(1,2,3,2,1,5)
t
(1, 2, 3, 2, 1, 5)
s={}
s{1,2,3,4,5}
SyntaxError: invalid syntax
s={1,2,3,4,5}
s
{1, 2, 3, 4, 5}
type(s)
<class 'set'>
s={1,1,1,1,1,2,2,3,4}
s
{1, 2, 3, 4}
d={'name':'hny','age':'11'}
d
{'name': 'hny', 'age': '11'}
a=None
type(a)
<class 'NoneType'>
