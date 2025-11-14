from functools import reduce
from decimal import Decimal, ROUND_HALF_UP

class HocSinh:
    def __init__(self, i, ten, diem):
        self.code = f'HS{str(i).zfill(2)}'
        self.name = ten
        self.tbc = (Decimal(diem[0])*2 + Decimal(diem[1])*2 + reduce(lambda x, y: x + y, map(Decimal, diem[2:]))) / Decimal(12)
        self.tbc = self.tbc.quantize(Decimal('0.1'), ROUND_HALF_UP)
        if self.tbc >= 9:
            self.loai = 'XUAT SAC'
        elif self.tbc >= 8:
            self.loai = 'GIOI'
        elif self.tbc >= 7:
            self.loai = 'KHA'
        elif self.tbc >= 5:
            self.loai = 'TB'
        else:
            self.loai = 'YEU'

n = int(input())
ds = []
for i in range(1, n+1):
    ten = input().strip()
    diem = input().split()
    ds.append(HocSinh(i, ten, diem))

ds.sort(key=lambda x: (-x.tbc, x.code))

for hs in ds:
    print(hs.code, hs.name, hs.tbc, hs.loai)
