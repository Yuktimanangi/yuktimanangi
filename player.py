import random

# Input player names
name1 = input("Enter player 1 name: ")
name2 = input("Enter player 2 name: ")

print("Computer has fixed 5 numbers between 1 and 10.")
print("You guys have to guess them. Ready???")

# Generate 5 unique random numbers between 1 and 10
nums = []
while len(nums) != 5:
    d = random.randint(1, 10)
    if d not in nums:
        nums.append(d)

print("----------------")

# Initialize scores and guess history
s1 = 0
s2 = 0
player1 = []
player2 = []

# 3 rounds
for i in range(3):
    print("-------- ROUND {} --------".format(i + 1))

    # Player 1 guess
    print("Dear {}, guess your choice:".format(name1))
    ch = int(input())
    while ch in player1 or ch in player2:
        ch = int(input("It is already taken. Choose another: "))
    player1.append(ch)
    if ch in nums:
        print("----->> CORRECT")
        s1 += 1
    else:
        print("---------- WRONG")

    # Player 2 guess
    print("Dear {}, guess your choice:".format(name2))  # Fixed: name2, not name1
    ch = int(input())
    while ch in player1 or ch in player2:
        ch = int(input("It is already taken. Choose another: "))
    player2.append(ch)
    if ch in nums:
        print("----->> CORRECT")
        s2 += 1
    else:
        print("---------- WRONG")

# Summary
print("-------------------")
print("Let's have a summary:")
print("Computer had fixed:", nums)
print("{} guessed: {}".format(name1, player1))
print("{} guessed: {}".format(name2, player2))
print("{}'s Score: {}".format(name1, s1))
print("{}'s Score: {}".format(name2, s2))

# Result
if s1 > s2:
    print(" {} wins!".format(name1))
elif s2 > s1:
    print(" {} wins!".format(name2))
else:
    print(" It's a draw!")
