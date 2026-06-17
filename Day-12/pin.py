'''
seq:str,list,tuple,set,dict,range
for i in seq:
    #stmts
'''

pin=1234
for i in range(5):
    p_pin=int(input("Enter the pin:"))
    if p_pin == pin:
        print("Unlock the phone")
        break
    else:
        print("Incorrect pin")
else:
    print("Try again,agter 60 seconds")
