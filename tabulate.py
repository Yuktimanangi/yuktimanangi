headers=["name", "age", "department"]

data=[
    ["yukk", 20, "IS"],
    ["yukti", 21, "CS"],
    ["srushti", 22, "eee"],
    ["siri", 20, "IS"]   
]

print(f"{headers[0]:<12} {headers[1]:<5} {headers[2]:<15}")
print("*" *30)

for row in data:
    print(f"{row[0]:<12} {row[1]:<5} {row[2]:<15}")
    print("-" *30)


