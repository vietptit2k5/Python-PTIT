def check(s,ss) :
    for i in range(1,len(s)) :
        if abs(ord(s[i])-ord(s[i-1])) != abs(ord(ss[i])-ord(ss[i-1])) : return False
    return True
for _ in range(int(input())):
    s = str(input())
    ss = ''.join(reversed(s))
    print("YES" if check(s,ss) else "NO")
