#list comprehenstion
#syntax
'''
l=[val for var in seq]
l=[val for var in seq if condition]
l=[val if condition else val for var in seq]
'''
'''
res1=[]
for i in range(1,11):
    res1.append(i)
res2=[i for i in range(1,11)]
print(res1)
print(res2)
'''
'''
res3=[]
res3=[i for i in range(3,31,3)]
print(res3)      
'''

#even numbers 2 to 50
'''
res4=[]
res4=[i for i in range(2,51,2)]
print(res4)
'''
#using if
'''
a='python programming'
l=[]
for i in a:
    if i in 'aeiouAEIOU':
        l.append(i)
print(l)

l1=[i for i in a if i in 'aeiouAEIOU']
print(l1)
'''
'''
a=[1,2,3,4,5,6,7,8,11,32,65,67,87,75]
l=[]
for i in a:
    if i%2==0:
        l.append(i)
    else:
        l.append(0)
print(l)

l1=[i if i%2==0 else 0 for i in a]
print(l1)
'''
'''
l=[int(input(f"Enter the number-{i+1}:"))for i in range(10)]
print(l)
'''











