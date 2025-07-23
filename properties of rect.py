class rect:
    prop1="sum of all angles is 360"
    prop2="each angle is 90"
    def get_info(self):
        a=int(input("enter the len of rect:"))
        b=int(input("enter the breadth of rect:"))
        self.len=a
        self.breadth=b

    def area(self):
        print(self.len*self.breadth)
print("the rectangle properties")
print(rect.prop1)
print(rect.prop2)
a1=rect()
a2=rect()
a1.get_info()
a2.get_info()
a1.area()
a2.area()