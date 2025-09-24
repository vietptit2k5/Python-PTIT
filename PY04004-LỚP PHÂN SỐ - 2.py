import math
class PhanSo :
    def __init__(self,tu,mau):
        self.tu=tu
        self.mau=mau
    def rutgon(self) :
        g = math.gcd(self.tu,self.mau)
        self.tu //= g
        self.mau //=g
        return self
    def __add__(self,other) :
        tu_moi = self.tu*other.mau+self.mau*other.tu
        mau_moi = self.mau*other.mau
        return PhanSo(tu_moi,mau_moi).rutgon()
    def __str__(self):
        return f"{self.tu}/{self.mau}"
if __name__ == '__main__' :
    a,b,c,d = map(int,input().split())
    p = PhanSo(a,b)
    q = PhanSo(c,d)
    t = p+q
    print(t)

        