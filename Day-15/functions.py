#Functions
'''
def function_name(arg):
    #stmts
    return
function_name(para)
'''
'''
def wish(name):
    print(f'welcome to the python course {name}!')
wish('Honey')
wish('Aishu')    
wish('Usha Rani')    
wish('Revathi')    
'''
#even or odd
'''
def even(num):
    if num%2==0:
        return f"{num}-Even Number"
    else:
        return f"{num}-Odd Number"
print(even(12))
print(even(13))
'''
#factorial
'''
def factorial(num):
    fact=1
    for i in range(1,num+1):
        fact*=i
    return fact
num=int(input("Enter the number:"))
print("factorial:",factorial(num))
'''
#prime number
'''
def prime(num):
    for i in range(2,num//2):
        if num%i==0:
            return f"{num}-Not prime Number"
    return f"{num}-Prime Number"
num=int(input("Enter the number:"))
print(prime(num))
'''
#positional arrguments
''''
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display('honey','honey10@gmail.com','hny@123')    
display('honey10@gmail.com','honey','hny@123')    
display('honey10@gmail.com','hny@123','honey')    
'''

#keyword
'''
def display(name,email,pwd):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)
display(name='honey',email='honey10@gmail.com',pwd='hny@123')    
display(email='honey10@gmail.com',name='honey',pwd='hny@123')    
display(email='honey10@gmail.com',pwd='hny@123',name='honey')    
'''

#default
'''
def display(name,email,pwd=''):
    print("Name:",name)
    print("Email:",email)
    print("Password:",pwd)

display('honey','honey10@gmail.com','hny@123')    
display('honey','honey10@gmail.com')    
'''
#variable
'''
def display(*names):
    print("Names:",names)

display('honey','aishu','usha','revu','subha')    
display('honey','aishu','usha','revu')    
display('honey','usha','revu','subha')    
display('honey')
display('honey','aishu')    
'''
#kaywordvariables
def display(**names):
    print("Names:",names)

display(k1='honey',k2='aishu',k3='usha')   
display(k1='honey')    























































