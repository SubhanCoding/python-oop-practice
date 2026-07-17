class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def display(self):
        print(self.real,"i",self.img,"j")
    
   
    def __add__(num1,num2):
        newReal=num1.real+num2.real
        newImg=num1.img + num2.img
        return complex(newReal,newImg)    

num1=complex(10,20)
num1.display()     


num2=complex(5,10)
num2.display() 


num3=num1+num2
num3.display() 



