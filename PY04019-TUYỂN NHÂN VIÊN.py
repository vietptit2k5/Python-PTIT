class NhanVien :
    def __init__(self,ma,ten,diem_lt,diem_th):
        self.ma = "TS" + str(ma).zfill(2)
        self.ten = ten
        self.diem_lt = diem_lt
        self.diem_th = diem_th
        self.diem_tb = self.tinh_diem()
        self.loai = self.xep_loai()
    def tinh_diem(self) :
        if self.diem_lt > 10 : self.diem_lt /= 10
        if self.diem_th > 10 : self.diem_th /= 10
        diem_tb = (self.diem_lt+self.diem_th)/2
        return round(diem_tb,2)
    def xep_loai(self) :
        if self.diem_tb < 5 :
            rank = "TRUOT"
        elif self.diem_tb < 8 :
            rank = "CAN NHAC"
        elif self.diem_tb <= 9.5 :
            rank = "DAT"
        else : rank = "XUAT SAC"
        return rank
n = int(input())
ds = []
for i in range(1,n+1) :
    ten = input().strip()
    diem_lt = float(input())
    diem_th = float(input())
    ds.append(NhanVien(i,ten,diem_lt,diem_th))
ds.sort(key=lambda x : -x.diem_tb)
for nv in ds :
    print(f"{nv.ma} {nv.ten} {nv.diem_tb}.2f {nv.loai}")
    

        