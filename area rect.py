class rect:
    def set_dim(self, a, b):
        self.a = a
        self.b = b

    def area(self):  # Removed a, b from here
        return self.a * self.b

nums = []
d = int(input("Enter number of rectangles: "))

for i in range(d):
    R = rect()
    a = int(input(f"Enter length of rectangle {i+1}: "))
    b = int(input(f"Enter breadth of rectangle {i+1}: "))
    R.set_dim(a, b)
    nums.append(R)

for idx, i in enumerate(nums, start=1):
    print(f"Area of rectangle {idx}: {i.area()}")
