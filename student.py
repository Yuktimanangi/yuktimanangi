class college:
    col="NITTE"
    def student(self,name,mark):
        self.name=name
        self.mark=mark

    def passfail(self):
        if(self.mark>40):
            print("clear")
        else:
            print("fail")
    def modify(self,grade):
        self.mark=self.mark+grade
    def display(self):
        print("name:",self.name)
        print("college:",self.col)
        print("marks:",self.mark)
        
        self.passfail()

s1=college()
s2=college()
s1.student("yukk", 30)
s2.student("yukti", 90)
s1.display()
print("---------------")
s2.display()



        