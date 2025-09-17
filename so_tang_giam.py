def check(s):
    if len(s) < 3 : return False
    for i in range(1,len(s)) :
        ok_tang = all(s[j] < s[j+1] for j in range(i))
        ok_giam = all(s[j] > s[j+1] for j in range(i,len(s)-1))
        if ok_tang and ok_giam : return True
    return False
for _ in range(int(input())) :
    s = input()
    print("YES") if check(s) else print("NO")