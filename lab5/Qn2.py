class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __mul__(self, scalar):
        return Point(self.x * scalar, self.y * scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(3, 4)
print(p * 2)  # Output: (6, 8)
