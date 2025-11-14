class KhachHang :
    def __init__(self,ma,ten,chiso_cu,chiso_moi):
        self.ma = "KH" + str(ma).zfill(2)
        self.ten = ten
        self.chiso_cu = chiso_cu
        self.chiso_moi = chiso_moi
        self.tien = self.tinh_tien()
    def tinh_tien(self) :
        so = self.chiso_moi - self.chiso_cu
        if so <= 50 : 
            tong = so*102
        elif so <=100 :
            tong = 50*100+(so-50)*150
            tong += tong*0.03
        else :
            tong = 50*100+50*150+(so-100)*200
            tong+=tong*0.05
        return round(tong)

n = int(input())
ds = []
for i in range(1,n+1) :
    ten = input().strip()
    chiso_cu = int(input())
    chiso_moi = int(input())
    ds.append(KhachHang(i,ten,chiso_cu,chiso_moi))
ds.sort(key=lambda x : -x.tien)
for kh in ds :
    print(f"{kh.ma} {kh.ten} {kh.tien}")
