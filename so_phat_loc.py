def check(s) :
    if s[len(s)-2]=='8' and s[len(s)-1]=='6' :
        return True
    return False
for _ in range(int(input())) :
    s = input() 
    print("YES") if check(s) else print("NO")
    