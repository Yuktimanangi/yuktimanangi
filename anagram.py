str1=input("enter string 1:" )
str2=input("enter string 2:" )
a=str1.upper()
b=str2.upper()
a1="".join( i for i in a if i!=" ")
b1="".join( i for i in b if i!=" ")
a2=sorted(a1)
b2=sorted(b1)
if(a2==b2):
    print("it is anagram")
else:
    print("it is not anagram")