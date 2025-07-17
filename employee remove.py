names = ["A", "B", "C", "D", "F", "G", "H", "J"]
memo = [0, 1, 1, 1, 2, 2, 1, 2]
salary = [1000, 2000, 3000, 4500, 2000, 5000, 1500, 2300]

data = list(zip(names, memo, salary))

removed1 = []
removed2 = []

# Remove people with salary > 4000
for i in data:
    if i[2] > 4000:
        removed1.append(i)

# Keep remaining people
remaining = [i for i in data if i[2] <= 4000]

# Sort remaining by name in reverse (Z-A)
a = sorted(remaining, key=lambda x: x[0], reverse=True)

# Remove up to 4 with memo >= 2
for i in a:
    if i[1] >= 2 and len(removed2) < 4:
        removed2.append(i)

# Final list of removed
final = removed1 + removed2

# Print results
for idx, i in enumerate(final, 1):
    print("{}. {} : Memo{} : Salary{} ".format(idx, i[0], i[1], i[2]))
