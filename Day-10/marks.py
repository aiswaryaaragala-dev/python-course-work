
data={
    'honey':{'status':True,'python':89,'mysql':90,'flask':99},
    'revathi':{'status':True,'python':79,'mysql':77,'flask':90},
    'usha':{'status':False,'python':None,'mysql':None,'flask':None},
    'subha':{'status':True,'python':45,'mysql':30,'flask':29},
    'harika':{'status':False,'python':None,'mysql':None,'flask':None},
    }

name=input("Enter the name:")
if name in data:
    if data[name]['status']:
        total=data[name]['python']+data[name]['mysql']+data[name]['flask']
        avg=total/3
        if avg>90:
            print(f"congrations{name},you got first class!!!")
        elif avg>70:
            print(f"Good{name},keep it up!!")
        elif avg>35:
            print(f"Better{name},work hard!")
        else:
            print(f"{name},you failed in the exam.Bring your parents.")

    else:
        print(f"{name}didn't write the exam.Bring your parents")
else:
    print(f"{name}'s data is not found")




    





    
            

            





    
