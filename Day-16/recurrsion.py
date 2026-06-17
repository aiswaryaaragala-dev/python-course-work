#Recursion
'''
def func():
    if base condition:
        return
    func()
'''
'''
def func(num):
    if num==0:
        return
    print(num,end=' ')
    func(num-1)
    print(num,end=' ')
func(5)    

# output:5 4 3 2 1 1 2 3 4 5
'''
'''
def func(num):
    if num==0:
        return
    print(num,end=' ')
    func(num-1)
    #print(num,end=' ')
func(5)    
#output:5 4 3 2 1
'''
#sum of digits
'''
def sum(n):
    if n==0:
        return 0
    return n+sum(n-1)
print(sum(10))
'''
#product
'''
def sum(n):
    if n==0:
        return 1
    return n*sum(n-1)
print(sum(4))
'''
'''
def power(base,pow):
    if pow==0:
        return 1
    return base*power(base,pow-1)
print(power(2,4))
print(power(3,3))
'''
def reverseofstr(s,ind):
    if  ind==0:
        return s[0]
    return s[ind]+reverseofstr(s,ind-1)
l="Python Programming"
print(reverseofstr(l,len(l)-1))





























