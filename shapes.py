def circle():
     r=int(input("enter radius of circle"))
     print("area of circle is:",3.14*r*r)

def square(a):
      print("area of square is:",a*a)

def triangle():
      b=int(input("enter base:"))
      h=int(input("enter height:"))
      return 0.5*b*h

def rect(a,b):
      return a*b
           

while(True):
    print("1.CIRCLE")
    print("2.SQUARE")
    print("3.TRIANGLE")
    print("4.RECTANGLE")
    print("5.EXIT")

    ch=int(input("enter your choice:"))
    match ch:
        case 1:
                circle()
        case 2:
             a=int(input("enter side of square"))
             square(a)
        case 3: 
            res=triangle()
            print("area of triangle",res)
        case 4:
             a=int(input("enter length of rect"))
             b=int(input("enter the breadth of rect"))
             res=rect(a,b)
             print("area of rect",res)    
        case 5:
              exit(0)
        case _:print("invalid option")

    