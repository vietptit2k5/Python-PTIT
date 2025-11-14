class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        r = self.real * other.real - self.imag * other.imag
        i = self.real * other.imag + self.imag * other.real
        return Complex(r, i)

    def __str__(self):
        if self.imag >= 0:
            return f"{self.real} + {self.imag}i"
        else:
            return f"{self.real} - {abs(self.imag)}i"

T = int(input())
for _ in range(T):
    a, b, c, d = map(int, input().split())
    A = Complex(a, b)
    B = Complex(c, d)
    C = (A + B) * A
    D = (A + B) * (A + B)
    print(f"{C}, {D}")
