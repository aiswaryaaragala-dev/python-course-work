#local scope
'''
def display():
    n=10
    print("Inside:",n)#Inide 10
display()
print("Outside:",n)#error
'''
#Global access
'''
n=10
def display():
    print("Inside:",n)#Inide 10
display()
print("Outside:",n)#outside:10
'''
'''
def display(n):
    #global n
    n+=10
    print("Inside:",n)#Inide 10
n=10
display(n)
print("Outside:",n)
'''
'''
def display():
    global n
    n+=10
    print("Inside:",n)
n=10    
display()
print("Outside:",n)

#output

Inside: 20
Outside: 20
'''

#inner function
'''
def outer():
    n=10
    def inner():
        nonlocal n
        n+=10
        print("Inner function:",n)
    inner()
    print("outer function:",n)
outer()
#output
Inner function: 20-
outer function: 20
'''
'''
s='python'
print(len(s))#6
len=5
print(len(s))#error
'''
#pass by value/pass by refence
#int
'''
def update(n):
    n=10
    print("Inside:",n)
n=20
update(n)
print("Outside:",n)
'''
#float
'''
def update(n):
    n=10
    print("Inside:",n)
n=20.1
update(n)
print("Outside:",n)
'''
#complex
'''
def update(n):
    n=10
    print("Inside:",n)
n=20+3j
update(n)
print("Outside:",n)
'''
#string
'''
def update(n):
    n='python'
    print("Inside:",n)
n='py lang'
update(n)
print("Outside:",n)
'''
'''
def update(n):
    n='python'
    n+='java'
    print("Inside:",n)
n='py lang'
update(n)
print("Outside:",n)
'''
#tuple
'''
def update(n):
    n=(10,11)
    print("Inside:",n)
n=(1,2,3,4,5)
update(n)
print("Outside:",n)
'''
#list
'''
def update(n):
    n.append(8)
    print("Inside:",n)
n=[1,2,3,4,5]
update(n)
print("Outside:",n)
'''
#set
'''
def update(n):
    n.add(10)
    print("Inside:",n)
n={1,2,3,4,5}
update(n)
print("Outside:",n)

'''
#dict
'''
def update(n):
    n[4]=8
    print("Inside:",n)
n={1:5,2:7,3:4}
update(n)
print("Outside:",n)
'''
#bool
'''
def update(n):
    n=True
    print("Inside:",n)
n=False
update(n)
print("Outside:",n)
'''

















































