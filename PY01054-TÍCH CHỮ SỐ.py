def solve(s) :
    cnt = 1
    for i in range(len(s)) :
        if int(s[i]) > 0 : cnt*=int(s[i])
    return cnt
for _ in range(int(input())) :
    s = str(input())
    print(solve(s)) 