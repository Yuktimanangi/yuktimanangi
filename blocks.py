b = int(input("Enter the number of blocks: "))
l = int(input("Enter the number of lines per block: "))
s = int(input("Enter the number of stars per line: "))
total = 0

print("------------------------")

for i in range(b):
    print(f"------- Block {i+1} --------")
    count = 0
    for j in range(l):
        for k in range(s):
            print("*", end=" ")
            count += 1
        print()
    print(f"Stars in block {i+1}: {count}")
    total += count

print(f"Total stars printed: {total}")
