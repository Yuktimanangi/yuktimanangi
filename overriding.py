class A:
    def show(self):
        print("hello")
class B(A):
    def show(self):
         print("today is wed")

s=A()
s1=B()
s.show()
s1.show()
