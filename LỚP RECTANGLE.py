class Rectangle:
    def __init__(self, length, width, color):
        self.length = length
        self.width = width
        self._color = color
    
    def perimeter(self):
        if self.length <= 0 or self.width <= 0:
            return None
        return 2 * (self.length + self.width)
    
    def area(self):
        if self.length <= 0 or self.width <= 0:
            return None
        return self.length * self.width
    
    def color(self):
        return self._color.capitalize()

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), arr[2])
    if r.perimeter() is None or r.area() is None:
        print("INVALID")
    else:
        print(f"{r.perimeter()} {r.area()} {r.color()}")
