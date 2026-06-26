'''
def display(s,ind):
    if ind==len(s):
        return
    print(s[:ind+1])
    display(s,ind+1)
display("abcdefg",0)
#output
a
ab
abc
abcd
abcde
abcdef
abcdefg
'''
'''
def display(s,ind,l):
    if ind==len(s)-l+l:
        return
    print(s[ind:ind+l])
    display(s,ind+1,l)
display("abcdef",0,3)
'''
'''
def display(l,ind):
    if ind==len(l):
        return 0
    return l[ind]+display(l,ind+1)
l=[1,2,3,4,6,8]
print(display(l,0))
'''
#count vowel
'''
def display(s,i):
    if i==len(s):
         return 0
    if s[i] in 'aeiouAEIOU':
        return 1+display(s,i+1)
    else:
        return display(s,i+1)
s='python programming'
print(display(s,0))
'''
#sum of digits

def display(s):
    sum=0
    for i in range(len(s)):
        sum+=s(i)
    return sum
s=7654
print(display(s))

























