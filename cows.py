legs = int(input("Enter total number of legs: "))
heads = int(input("Enter total number of heads: "))
flag = False  # Initialize the flag

for hen in range(heads + 1):  # Include 'heads' in the range
    cow = heads - hen
    if (cow * 4 + hen * 2 == legs):
        print("Cows:", cow)
        print("Hens:", hen)
        flag = True
        break

if not flag:
    print("No solution")
