class employee:
    def __init__(self,role,department,salary):
        self.role=role
        self.department=department
        self.salary=salary

    def showdetails(self):
       print("Name=",self.name)
       print("Age=",self.age)
       print("Role=",self.role)
       print("Department=",self.department)
       print("salary=",self.salary)
       
class engineer(employee):
    def __init__(self,name,age):
        self.name=name
        self.age=age
        super().__init__("DataAnalyst","DataScience","250k")
    
e1=engineer("Subhan",24)
e1.showdetails()