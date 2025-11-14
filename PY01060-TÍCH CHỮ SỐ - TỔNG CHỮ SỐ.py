for _ in range(int(input())) :
    s = str(input())
    tich = 1 
    tong = 0
    for i in range(len(s)) :
        if i%2==0 : 
            if int(s[i]) > 0 : tich *= int(s[i])
        else : tong += int(s[i])
    ds = []
    ds.append(tich)
    ds.append(tong)
    print(*ds)