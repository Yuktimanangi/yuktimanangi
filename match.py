import random
n=int(input("Enter no of teams:"))
teams=[]
for i in range(n):
    a=input(("Enter team name:"))
    teams.append(a)

meet=int(input("Enter no of meeting bw one pair:"))
match=[]
for i in range(n-1):
    for j in range(i-1,n):
        for k in range(meet):
            match.append([teams[i],teams[j]])
            
random.shuffle(match)
print("-----------------------------")
index=1
for i in match:
    print("match {}: {} vs {}".format(index,i[0],i[1]))
    index=index+1
    

