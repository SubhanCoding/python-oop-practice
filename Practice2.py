class order:
    def __init__(self,items,price):
        self.items=items
        self.price=price

    def __gt__(self,o2):
        return self.price>o2.price

o1=order("chips",20)
o2=order("tea",15)
print(o1>o2)    