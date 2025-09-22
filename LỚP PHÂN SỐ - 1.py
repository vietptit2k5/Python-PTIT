import math

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    
    def rutgon(self):
        g = math.gcd(self.tu, self.mau)
        self.tu //= g
        self.mau //= g
    
    def __str__(self):
        return f"{self.tu}/{self.mau}"

if __name__ == '__main__':
    tu, mau = map(int, input().split())
    ps = PhanSo(tu, mau)
    ps.rutgon()
    print(ps)
