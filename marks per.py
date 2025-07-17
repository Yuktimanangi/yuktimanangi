import time

names = []
marks = []

for i in range(5):
    n = input("Enter your name: ")
    names.append(n)
    student = []
    for j in range(3):
        m = int(input("Enter your mark {}: ".format(j + 1)))  # Convert input to int
        student.append(m)
    marks.append(student)

per = []
for i in marks:
    res = sum(i) / 3  # Use float division for accurate percentage
    per.append(res)

time.sleep(3)
print("-----------------------------")

for i in range(5):  # Print for all 5 students
    print("{}. {} : {:.2f}%".format(i + 1, names[i], per[i]))
