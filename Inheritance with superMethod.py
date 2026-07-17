class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car started")
    @staticmethod    
    def stop():
        print("car stop")    

class toyotaCar(car):
     def __init__(self,name,type):
        self.name=name 
        super().__init__(type)

car1=toyotaCar("Prius","electric")
print(car1.type)
print(car1.start())

