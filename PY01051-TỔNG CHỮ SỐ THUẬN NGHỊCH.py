def check(s) :
    n = len(s)
    if n < 2 : return False
    else :
        for i in range(int(n/2)) :
            if s[i] != s[n-1-i] : return False
        return True
    
for _ in range(int(input())) :
    s = str(input())
    tmp = 0
    for i in range(len(s)) : tmp += int(s[i])

    print("YES") if check(str(tmp)) else print("NO")