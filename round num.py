n=int(input("enter any no:"))
l=[]
while(n not in l):
    l.append(n)
    n=sum([int(i) * int(i) for i in str(n)])
if(n==1):
    print("round no")
else:
    print("not a round no")