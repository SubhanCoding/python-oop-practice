class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
          
    @property
    def percentage(self):      
        return (str((self.phy+self.chem+self.math)/3)+"%")
s1=student(90,70,80)
print(s1.percentage)    
s1.phy=100
print(s1.percentage)    

#instead  of
class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
          
        self.percentage=str((self.phy+self.chem+self.math)/3)+"%"
s1=student(90,70,80)
print(s1.percentage)    
s1.phy=100
print(s1.percentage)    