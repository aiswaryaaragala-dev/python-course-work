#lambda functions
'''
add=lambda a,b:a+b
print(add(12,14))
'''
'''
add=lambda a,b:a+b
print(add(12,14))
print(add(6,4))
print(add(4,14))
'''
'''
wish=lambda name:f'Welcome the python course {name}'
print(wish('honey'))
print(wish('aishu'))
#output
Welcome the python course honey
Welcome the python course aishu
'''
'''
gst=lambda price:price+price*0.18
print(gst(1000))
print(gst(600))
print(gst(89000))
'''
#Greatest number
'''
greatest=lambda a,b:a if a>b else b
print(greatest(9,4))
print(greatest(8,55))

'''
#even number 
'''
iseven=lambda a:f"{a}-Even number" if a%2==0 else f"{a}-odd number"
print(iseven(4))
print(iseven(7))
'''
#bill
'''
bill=lambda charge:charge if charge>99 else charge+30
print(bill(150))
print(bill(15))
print(bill(200))
print(bill(2))
'''
#nested if
'''
login=False
instock=False
status=lambda login,instock:("you can buy product" if instock else "product is out of stock")if login else"login to buy a product"
print(status(login,instock))
'''
#list
'''
l=[1,2,3,4,5,6,7]
res=list(map(lambda i:i**3,l))
print(res)
'''
#title
'''
names=['honey','aishu','chichu']
t=list(map(lambda i:i.title(),names))
print(t)
'''
'''
l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i%2==0,l))
print(res)
'''
'''
l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i>5,l))
print(res)
'''
'''
l=[1,2,3,4,5,6,7]
res=list(filter(lambda i:i%3==0,l))
print(res)
'''
'''
from functools import  reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
print(s,p)
'''
'''
from functools import  reduce
l=[1,2,3,4,5,6,7,8,9,10,11,12]
s=reduce(lambda sum,i:sum+i,l)
p=reduce(lambda pro,i:pro*i,l)
m=reduce(lambda max,i:max if max>i else i,l)
mi=reduce(lambda max,i:max if max>i else i,l)
print(s,p,m,mi)
'''

d={'honey':70,'aishu':67,'chichu':29,'chuchu':87}
print(dict(sorted(d.items())))
print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),reverse=True)))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))


















 




















