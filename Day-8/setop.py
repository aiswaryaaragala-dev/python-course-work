Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s={1,2,3,4}
s
{1, 2, 3, 4}
s=set()
s
set()
s={1,2,1,1,1,2,3,4,5}
s
{1, 2, 3, 4, 5}
s={88,55,555,3,21,67,2,100}
s
{2, 3, 67, 100, 555, 21, 55, 88}

s.add(1)
s
{1, 2, 3, 67, 100, 555, 21, 55, 88}
s.add(58.55)
s
{1, 2, 3, 67, 100, 555, 21, 55, 88, 58.55}
s.add(888.88)
s
{1, 2, 3, 67, 100, 555, 888.88, 21, 55, 88, 58.55}
s.add((1,2,3,4))
s
{1, 2, 3, 67, 100, 555, (1, 2, 3, 4), 888.88, 21, 55, 88, 58.55}
4 in s
False
3 in s
True
s.add(False)
s
{False, 1, 2, 3, 67, 100, 555, (1, 2, 3, 4), 888.88, 21, 55, 88, 58.55}
False in s
True
4 not in s
True
(1,2,3,4)in s
True
a=(1,2,3,4,5,8,10)
b=(6,7,8,9)
a|b
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a|b
TypeError: unsupported operand type(s) for |: 'tuple' and 'tuple'
a={1,2,3,4,5,6,8,10)
SyntaxError: closing parenthesis ')' does not match opening parenthesis '{'
a={1,2,3,4,5,6,7,8}
b{6,7,8,9}
SyntaxError: invalid syntax
b={7,8,9}
a \ b
SyntaxError: unexpected character after line continuation character
a | b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
a.intersection(b)
{8, 7}
a & b
{8, 7}
a - b
{1, 2, 3, 4, 5, 6}
a ^ b
{1, 2, 3, 4, 5, 6, 9}
a
{1, 2, 3, 4, 5, 6, 7, 8}
#{1}{2}{3}{4}{1,3}{1,2}{7,8}

a<={1}
False
a>={1}
True
a<={1,2,3,4,5,6,7,8,9,10,11,12}
True
a>=
SyntaxError: invalid syntax
a>={6,7,10}
False
a>={6,10,8}
False
a.isdisjoint(b)
False
a.isdisjoint({90,100})
True
a
{1, 2, 3, 4, 5, 6, 7, 8}
a.add(17)
a
{1, 2, 3, 4, 5, 6, 7, 8, 17}
a.update({11,12,13})
a
{1, 2, 3, 4, 5, 6, 7, 8, 11, 12, 13, 17}
a.pop()
1
a.remove(6)
a
{2, 3, 4, 5, 7, 8, 11, 12, 13, 17}
a.discard(3)
a
{2, 4, 5, 7, 8, 11, 12, 13, 17}
a
{2, 4, 5, 7, 8, 11, 12, 13, 17}
a.clear()
a
set()
a={1,23,4,57,235}
b={1,2,34,4}
a.intersection(b)
{1, 4}
a
{1, 4, 23, 57, 235}
b
{1, 2, 34, 4}
a.intersection_update(b)
a
{1, 4}
b
{1, 2, 34, 4}
c=b
c.add(12)
c
{1, 2, 34, 4, 12}
b
{1, 2, 34, 4, 12}
d = c.copy()
d.add(10)
d
{1, 2, 34, 4, 10, 12}
b
{1, 2, 34, 4, 12}
len(c)
5
min(c)
1
max(c)
34
sorted(c)
[1, 2, 4, 12, 34]
sum(c)
53
