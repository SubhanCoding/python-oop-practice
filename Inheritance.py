class car:
    color="Black"
    @staticmethod
    def start():
        print("car started")
    @staticmethod    
    def stop():
        print("car stop")    

class toyotaCar(car):
    def __init__(self,name):
        self.name=name 

c1=toyotaCar("Fortuner")
c2=toyotaCar("Prado")            


print(c1.color,c1.name)   #You can access all the features of parent class
print(c1.start())