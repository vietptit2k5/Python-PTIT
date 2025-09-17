def check(n) :
    for i in range(len(n)) :
        if n[i]!='1' and n[i]!='2' and n[i]!='0' : return False
    return True
for _ in range(int(input())) :
    n = input()
    print("YES") if check(n) else print("NO")