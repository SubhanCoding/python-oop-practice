# Method 1
class person:
    name="anonymous"
    @classmethod
    def changeName(cls,name):
        cls.name=name

# p1=person()
# p1.changeName("subhan")      #ap pr ha k ap object bnana chahty ho ya nhi
# print(p1.name)     
person.changeName("tuba")
print(person.name)


# Method 2
# class person:
#     name="anonymous"
#     def changeName(self,name):
#         person.name=name
# p1=person()
# p1.changeName("subhan")
# print(p1.name)     
# print(person.name)   


#  Method 3
# class person:
#     name="anonymous"
#     def changeName(self,name):
#         self.__class__.name=name
# p1=person()
# p1.changeName("subhan")
# print(p1.name)     
# print(person.name)  
