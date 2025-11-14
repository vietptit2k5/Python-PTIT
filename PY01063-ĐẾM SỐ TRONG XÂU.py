for _ in range(int(input())) :
    s = str(input())
    n = int(input())
    id = len(str(n))
    idx = 0
    cnt = 0
    while idx <= len(s)-id :
        m = int(s[idx:idx+id])
        if m==n :
            cnt+=1
            idx+=id
        else : idx+=1
    print(cnt)
