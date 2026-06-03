Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
s='python programming'
len(s)
18
sorted(s)
[' ', 'a', 'g', 'g', 'h', 'i', 'm', 'm', 'n', 'n', 'o', 'o', 'p', 'p', 'r', 'r', 't', 'y']
min(s)
' '
max(s)
'y'
ord('a')
97
ord('A')
65
chr
<built-in function chr>
chr(98)
'b'
chr(120)
'x'
chr(30)
'\x1e'
chr(35)
'#'
chr(37)
'%'
s='python Programming'
s.upper()
'PYTHON PROGRAMMING'
s.lower()
'python programming'
s.capitalize()
'Python programming'
s.title()
'Python Programming'
s.swapcase()
'PYTHON pROGRAMMING'
s.casefold()
'python programming'
s
'python Programming'
s.center(28,'-')
'-----python Programming-----'
s.center(38,'*')
'**********python Programming**********'
s.ljust(28,'-')
'python Programming----------'
s.rjust(28,'-')
'----------python Programming'
'123'.zfill(10)
'0000000123'
'123'.zfill(5)
'00123'
'123'.zfill(3)
'123'
'123'.zfill(2)
'123'
s
'python Programming'
s.find('g')
10
s.rfind('o')
9
s.find('z')
-1
s.index('o')
4
s.rindex('o')
9
s.index('z')
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s
'python Programming'
s.count('y')
1
s.count('m')
2
s.count('g')
2
s
'python Programming'
s.replace('python','java')
'java Programming'
s.maketrans('python','123456')
{112: 49, 121: 50, 116: 51, 104: 52, 111: 53, 110: 54}
s.translate(s.maketrans('python','123456'))
'123456 Pr5grammi6g'
s='java,python,javascript,c,c++'
s.split(',')
['java', 'python', 'javascript', 'c', 'c++']
s,split(',',2)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    s,split(',',2)
NameError: name 'split' is not defined
s.split(',',2)
['java', 'python', 'javascript,c,c++']
s.rsplit(',',2)
['java,python,javascript', 'c', 'c++']
g='sdfgh'
g='''dsfghjk'''
g='''dfghjk
fghjkl;
gfhjkl
drtyuhj'''
g
'dfghjk\nfghjkl;\ngfhjkl\ndrtyuhj'
s.splitlines()
['java,python,javascript,c,c++']
g.splitlines()
['dfghjk', 'fghjkl;', 'gfhjkl', 'drtyuhj']
l=['java', 'python', 'javascript', 'c', 'c++']
''.join(l)
'javapythonjavascriptcc++'
'-'.join(l)
'java-python-javascript-c-c++'
'@'.join(l)
'java@python@javascript@c@c++'
' '.join(l)
'java python javascript c c++'
','.join(l)
'java,python,javascript,c,c++'
s
'java,python,javascript,c,c++'
s.partition(',')
('java', ',', 'python,javascript,c,c++')
s.rpartition(',')
('java,python,javascript,c', ',', 'c++')
t="Hello"
t.encode()
b'Hello'
b'Hello'.decode()
'Hello'
