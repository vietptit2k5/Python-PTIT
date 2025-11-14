for _ in range(int(input())) :
    s = input()
    ds = []
    cnt = 0
    for i in range(len(s)) :
        if s[i].isdigit() :
            cnt += int(s[i])
        else : ds.append(s[i])
    ds.sort()
    res = ""
    for i in range(len(ds)) :
        res += ds[i]
    print(f"{res}{cnt}")