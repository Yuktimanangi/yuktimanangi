def prime(n):
    if n <= 1:
        return False
    for j in range(2, int(n**0.5) + 1):
        if n % j == 0:
            return False
    return True

def sod(i):
    # sum of digits is prime
    digit_sum = sum(int(d) for d in str(i))
    return prime(digit_sum)

def dig(i):
    # all digits should be non-prime
    while i > 0:
        d = i % 10
        if prime(d):
            return False
        i = i // 10
    return True

for i in range(100, 1000):
    if prime(i) and sod(i) and dig(i):
        print(i, end=" ")
