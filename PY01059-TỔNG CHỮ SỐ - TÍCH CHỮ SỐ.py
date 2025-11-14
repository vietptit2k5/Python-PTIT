import sys

def solve():
    try:
        N = sys.stdin.readline().strip()
    except EOFError:
        return
    
    if not N:
        return

    tong_chan = 0
    tich_le = 1
    
    co_chu_so_le_khac_khong = False
    
    length = len(N)
    
    for i in range(length):
        chu_so = int(N[i])
        
        if i % 2 == 0:
            tong_chan += chu_so
        else:
            if chu_so != 0:
                tich_le *= chu_so
                co_chu_so_le_khac_khong = True

    if not co_chu_so_le_khac_khong:
        tich_le = 0
        
    print(f"{tong_chan} {tich_le}")

def main():
    try:
        T = int(sys.stdin.readline().strip())
    except:
        return
        
    for _ in range(T):
        solve()

if __name__ == "__main__":
    main()