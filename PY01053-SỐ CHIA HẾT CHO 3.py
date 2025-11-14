for _ in range(int(input())) :
    n = str(input())
    cnt = 0
    for i in range(len(n)) :
        cnt += int(n[i])
    print("YES") if cnt % 3 ==0 else print("NO")