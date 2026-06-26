#list lambda
'''
d={'sugar':40,'salt':20,'cooking oil':60,'chilli':80}
res=dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))
res1=dict(map(lambda i:(i[0],i[1]-i[1]*0.5),d.items()))
print(res)
print(res1)
'''
'''
d={'sugar':40,'salt':20,'cooking oil':60,'chilli':80}
res=dict(filter(lambda i:i[1]>50,d.items()))
res1=dict(filter(lambda i:i[1]<50,d.items()))

print(res,res1)
'''

#[1, 2, 3, 1, 2, 3, 1, 2, 3]
'''
l=[]
for i in range(3):
    for j in range(1,4):
        l.append(j)
print(l)        
'''
#[[1,2,3],[1,2,3],[1,2,3]]
'''
l=[]
for i in range(3):
    temp=[]
    for j in range(1,4):
        temp.append(j)
        l.append(temp)
print(l)   
'''
'''
l=[[j for j in range(1,4)] for i in range(3)]
print(l)
'''
'''
s=set()
for i in range(1,11):
    s.add(i)
s1={i for i in range(1,11)}
print(s,s1)
'''
'''
s1=set()
s1={i for i in range(1,11)}    
print(s1)
'''
'''
d={}
for i in range (1,11):
    d[i]=i*i
print(d)    
res={i:i*i for i in range(1,11)}
print(res)
'''
'''
def display(name,marks):
    print("Name:",name)
    print("Marks:",marks)
display(name='honey',marks=35)
#Name: honey
#Marks: 35
'''
#print 5 students name and mark
'''
res={input("Enter the name:"):int(input("Enter the mark:"))
     for i in range(5)}
print(res)
'''
#Generator
def display():
    l=['1..50','51..100','101..150','151..200']
    yield l[0]
    yield l[1]
    yield l[2]
    yield l[3]
scroll=display()
print(next(scroll))
print(next(scroll))
print(next(scroll))
print(next(scroll))






























































