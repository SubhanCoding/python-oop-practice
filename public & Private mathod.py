class Account:
    def __init__(self,accNo,accPass):
        self.accNo=accNo
        self.__accPass=accPass
    def showPass(self):
        print(self.__accPass)    
a1=Account(123345,"asdfg") 
print(a1.accNo)
# print(a1.accPass)  THis wouldn't be access outside the class
print(a1.showPass())
