import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def area(self):
     
        x1, y1 = self.p1.x, self.p1.y
        x2, y2 = self.p2.x, self.p2.y
        x3, y3 = self.p3.x, self.p3.y
        if (x2 - x1)*(y3 - y1) == (x3 - x1)*(y2 - y1):
            return None  

        a = self.p1.distance(self.p2)
        b = self.p2.distance(self.p3)
        c = self.p3.distance(self.p1)
        s = (a + b + c) / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area


T = int(input())
for _ in range(T):
    nums = list(map(float, input().split()))
    if len(nums) != 6:
        print("INVALID")
        continue
    p1 = Point(nums[0], nums[1])
    p2 = Point(nums[2], nums[3])
    p3 = Point(nums[4], nums[5])
    triangle = Triangle(p1, p2, p3)
    area = triangle.area()
    if area is None or area == 0:
        print("INVALID")
    else:
        print(f"{area:.2f}")
