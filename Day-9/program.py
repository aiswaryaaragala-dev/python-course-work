#simple if
s='python programmming'
if 'python' in s:
    print('python found')


if s[0]=='p':
    print("string is starting with p")

#if else
    
data=('abc','1234')

username,password=input("Enter the username and password").split()
if data ==(username,password):
      print("Login successful")
else:
    print("Invalid login")

#if-elif-else

    
n=int(input("Enter the num:"))
if n>0:
    print("+ve")
elif n<0:
    print("-ve")
else:
    print("Zero")

#Nested else

products={
    'laptop':0,
    'mouse':10,
    'charger':4,
    'phones':40,
    'keynoard':0
}

product =input("Enter the product:")
if product in products:
    if products[product]!=0:
        print(f"you can buy{product}!!")
    else:
            print(f"{product}out of stock")
    
else:
    print(f"{product} is not available")
    
      
      
