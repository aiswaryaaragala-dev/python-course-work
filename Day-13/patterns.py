#py pt ph po pn yt yh yo yn th to tn ho hn on
'''
s='python'
for i in range(len(s)):
    for j in range(i+1,len(s)):
        print(s[i],s[j],sep='',end=' ')
'''

#sum=45
'''
l=[[1,2,3,],[4,5,6],[7,8,9]]
sum=0
for i in l:
    for j in i:
        sum+=j
print(f'sum={sum}')        
'''
#dict
''''
d={
    '1234':{'pin':'4567','balance':2300},
    '1244':{'pin':'6356','balance':5300},
    '2334':{'pin':'2345','balance':4500},
    '3344':{'pin':'9874','balance':7800},
   }
for i in d:
    print('Account number',i)
    print('pin number',d[i]['pin'])
'''  
    
#
'''
for i in range(5):
    for j in range(2):
        print(i,end='')
'''
'''
for row in range(5):
    for col in range(2):
        print(row,end='')
    print()    

'''
#print patterns(*)
'''
n=int(input("Enter the size:"))
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()    
'''
'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print(col%2,end='')
    print()
'''
'''
n=int(input("Enter the size:"))
for row in range(n):
      for col in range(row+1):
          print('*',end='')
      print()
'''
'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n-row):
        print('*',end='')
    print()    
'''
'''
n=int(input("Enter the size:"))
for i in range(n):
    for sp in range(n-1-i):
        print(' ',end='')
    for j in range(i+1):
        print('*',end='')
    print()    
'''
'''
n=int(input("Enter the size:"))
for i in range(n):
    for sp in range(i):
        print(' ',end='')
    for j in range(n-i):
        print('*',end='')
    print()  
'''
'''
n=int(input("Enter the size:"))
for row in range(n):
    for col in range(n):
        print((row+col)%2,end='')
    print()    
'''

'''
n=int(input("Enter the size:"))
c=1
for row in range(n):
    for col in range(row+1):
        print(c,end='')
        c+=1
    print()    
'''
n=int(input("Enter the size:"))
c=1
for row in range(n):
    for col in range(row+1):
        print(str(c).zfill(2),end='')
        c+=1
    print()    







    























    
 
