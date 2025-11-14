class ThiSinh:
    def __init__(self, ho_ten, ngay_sinh, diem1, diem2, diem3):
        self.ho_ten = ho_ten
        self.ngay_sinh = ngay_sinh
        self.tong_diem = diem1 + diem2 + diem3

ho_ten = input().strip()
ngay_sinh = input().strip()
diem1 = float(input().strip())
diem2 = float(input().strip())
diem3 = float(input().strip())

thi_sinh = ThiSinh(ho_ten, ngay_sinh, diem1, diem2, diem3)

print(f"{thi_sinh.ho_ten} {thi_sinh.ngay_sinh} {thi_sinh.tong_diem:.1f}")
