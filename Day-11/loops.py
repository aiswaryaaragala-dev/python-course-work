#str list tuple set dict range()
'''
for var in seq:
    print(var)
'''    

#string
'''
s='python programming'
for ch in s:
    print(ch)
'''
    
#list
'''
l=['sugar','salt','oil','eggs']
for item in l:
    print(item)
'''

#tuple
'''
t=('1.intro','2.tokens','3.data types')
for i in t:
    print(i)
'''    

#dict

'''
d={'name':'honey','batch':55,'course':'pfs','skills':['python','html','css','java']}
for i in d:
    print(i,d[i])
'''
#range(start,stop+1,step)=>(0,n,1)
'''
for i in range(30,2,-3):
    print(i)
    
for i in range(1,11):
    print(i)

for i in range(2,51,2):
    print(i)
    

for i in range(5,101,5):
    print(i)


for i in range(20,0,-1):
    print(i)

for i in range(1,50,2):
    print(i)


s='looping statements'
for i in range(len(s)):
    print(i,s[i])


l=[7,3,4,6,8,2,5]
for i in range(len(l)):
    print(i,l[i])


t=(7,3,4,6,8,2,5)
for i in range(len(t)):
    print(i,t[i])
    


s='looping statements'
for i in enumerate(s):
    print(i[0],i[1])



l=[7,3,4,6,8,2,5]
for i in enumerate(l):
    print(i[0],i[l])



t=(7,3,4,6,8,2,5)
for i in enumerate(t):
    print(i[0],i[1])
'''
#pass
'''
for i in range(10):
    pass
'''    
#break
'''
for i in range(10):
    if i==5:
        break
    print(i)
'''
#continue
'''
for i in range(10):
    if i==5:
        continue
    print(i)
'''





















