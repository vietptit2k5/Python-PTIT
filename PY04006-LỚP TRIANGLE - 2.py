import math
class Point :
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def khoang_cach(self,other) :
        return math.sqrt((self.a-other.a)**2+(self.b-other.b)**2)

class Triangle :
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def check(self) :
        AB = self.A.khoang_cach(self.B)
         