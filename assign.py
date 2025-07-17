input_str = "1234"
result = 0
for c in input_str:
    result = result * 10 + (ord(c) - ord('2'))
print("Output:", result)