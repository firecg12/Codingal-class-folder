
class Employee:
   
   def __init__(self):
        print("Employee class initialized")
    
   def __del__(self):
        print("Employee class destroyed")

def Create_obj():
    print('Creating Employee object')
    obj = Employee()
    print('function is ending')
    return obj

print('Calling Create_obj() function')
obj = Create_obj()
print('program ended')