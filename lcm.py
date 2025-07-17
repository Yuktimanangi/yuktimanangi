a = int(input("Enter num 1: "))
b = int(input("Enter num 2: "))

if a > b:
    big = a
else:
    big = b

while True:
    if big % a == 0 and big % b == 0:
        print("The LCM is", big)
        break
    big += 1  # Just increment by 1 instead of step
