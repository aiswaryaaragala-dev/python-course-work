Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
d={}
d
{}
type(d)
<class 'dict'>
d={'k1':'v1','k2':'v2'}
d
{'k1': 'v1', 'k2': 'v2'}
d={}
d[1]='int'
d
{1: 'int'}
d[12.4]='float'
d
{1: 'int', 12.4: 'float'}
d[3]='honey'
d
{1: 'int', 12.4: 'float', 3: 'honey'}
d[4]='12+4j'
d
{1: 'int', 12.4: 'float', 3: 'honey', 4: '12+4j'}
d['honey']='str'
d
{1: 'int', 12.4: 'float', 3: 'honey', 4: '12+4j', 'honey': 'str'}
d[12+2j]='complex'
d
{1: 'int', 12.4: 'float', 3: 'honey', 4: '12+4j', 'honey': 'str', (12+2j): 'complex'}
d[False]='bool'
\

d
{1: 'int', 12.4: 'float', 3: 'honey', 4: '12+4j', 'honey': 'str', (12+2j): 'complex', False: 'bool'}
d={}
d[1]=1
d
{1: 1}
d[22]=23.4
d
{1: 1, 22: 23.4}
d[3]='ujik'
d
{1: 1, 22: 23.4, 3: 'ujik'}
d[4]=3+3j
d[5]=[1,2,3]
d
{1: 1, 22: 23.4, 3: 'ujik', 4: (3+3j), 5: [1, 2, 3]}
{1: 1, 22: 23.4, 3: 'ujik', 4: (3+3j), 5: [1, 2, 3]}
{1: 1, 22: 23.4, 3: 'ujik', 4: (3+3j), 5: [1, 2, 3]}
d[6]=(1,2,3)
d[7]={1:1,2:2}
d[9]=False
d
{1: 1, 22: 23.4, 3: 'ujik', 4: (3+3j), 5: [1, 2, 3], 6: (1, 2, 3), 7: {1: 1, 2: 2}, 9: False}
d={}
d[1]=1
d[2]=2
d[3]=2
d[4]=2
d
{1: 1, 2: 2, 3: 2, 4: 2}
d[3]
2
d={1:2,2:4,3:6,4:8,5:10,6:12}
d[4]
8
d[5]
10
d[1]
2
d[6]
12
d={'honey':12,'aishu':44,'revathi':60,'usha':50}
d
{'honey': 12, 'aishu': 44, 'revathi': 60, 'usha': 50}
d['usha']
50
d['honey']
12
d.get('subha')
d.get('harika','user not found')
'user not found'
d.get('revathi')
60
d
{'honey': 12, 'aishu': 44, 'revathi': 60, 'usha': 50}
'honey' in d
True
'maha' not in d
True
'maha' in d
False
d.keys()
dict_keys(['honey', 'aishu', 'revathi', 'usha'])
d.values()
dict_values([12, 44, 60, 50])
d.items()
dict_items([('honey', 12), ('aishu', 44), ('revathi', 60), ('usha', 50)])
sorted(d)
['aishu', 'honey', 'revathi', 'usha']
max(d)
'usha'
min(d)
'aishu'
len(d)
4
d
{'honey': 12, 'aishu': 44, 'revathi': 60, 'usha': 50}
d['honey']
12
d['honey']=100
d
{'honey': 100, 'aishu': 44, 'revathi': 60, 'usha': 50}
d['aishu']=88
d
{'honey': 100, 'aishu': 88, 'revathi': 60, 'usha': 50}
d.update({'subha':56,'harika':99})
d
{'honey': 100, 'aishu': 88, 'revathi': 60, 'usha': 50, 'subha': 56, 'harika': 99}
d.popitem()
('harika', 99)
d
{'honey': 100, 'aishu': 88, 'revathi': 60, 'usha': 50, 'subha': 56}
d.popitem()
('subha', 56)
del d['honey']
d
{'aishu': 88, 'revathi': 60, 'usha': 50}
d.clear()
d
{}
d={'honey': 100, 'aishu': 88, 'revathi': 60, 'usha': 50, 'subha': 56, 'harika': 99}
d
{'honey': 100, 'aishu': 88, 'revathi': 60, 'usha': 50, 'subha': 56, 'harika': 99}
d.setdefault('maha',0)
0
d
{'honey': 100, 'aishu': 88, 'revathi': 60, 'usha': 50, 'subha': 56, 'harika': 99, 'maha': 0}
