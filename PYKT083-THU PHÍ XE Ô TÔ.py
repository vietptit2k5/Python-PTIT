class Xe:
    def __init__(self, bien, loai, ghe, huong, ngay):
        self.bien = bien
        self.loai = loai
        self.ghe = int(ghe)
        self.huong = huong
        self.ngay = ngay

def get_price(loai, ghe):
    if loai == 'Xe_con' and ghe == 5: return 10000
    if loai == 'Xe_con' and ghe == 7: return 15000
    if loai == 'Xe_tai': return 20000
    if loai == 'Xe_khach' and ghe == 29: return 50000
    if loai == 'Xe_khach' and ghe == 45: return 70000
    return 0

n = int(input())
money = {}
order = []
for _ in range(n):
    bien, loai, ghe, huong, ngay = input().split()
    x = Xe(bien, loai, ghe, huong, ngay)
    if x.huong == 'IN':
        if ngay not in money:
            money[ngay] = 0
            order.append(ngay)
        money[ngay] += get_price(x.loai, x.ghe)

for d in order:
    print(f'{d}: {money[d]}')
