names=["a","b","c","d"]
marks=[10,20,30,40]
res=list(zip(names,marks))
q=sorted(res,key=lambda x:x[1])
print(q)