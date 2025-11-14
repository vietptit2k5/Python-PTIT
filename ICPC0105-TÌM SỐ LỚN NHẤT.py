for _ in range(int(input())) :
    s = input()
    num = 0
    res = ''
    for c in s :
        if c.isdigit() :
            res += c
        else :
            if res :
                num = max(num,int(res))
                res = ''
    if res : num = max(num,int(res))
    print(num)