class rect:
    def set_dim(self,a,b):
        self.a=a
        self.b=b
        

    def area(self,a,b):
       return(self.a*self.b)

nums=[]
d=int(input("enter num of rect:"))
for i in range(d):
    R=rect()
    a=int(input("enter len of rect:"))
    b=int(input("enter breadth of rect:"))
    R.set_dim(a,b)
    nums.append(R)

iii=1
for i in nums:
    print("area of rect {} : is {}".format(iii,i.area()))
iii=iii+1
    


