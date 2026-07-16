class student:
    name="ananymous"
    def __init__(self,fullname=None,age=None):
     if fullname is not None: 
      self.name=fullname
     self.age=age


s1=student("Subhan",24)    
print(s1.name,s1.age) 

s2=student()
print(s2.name)


