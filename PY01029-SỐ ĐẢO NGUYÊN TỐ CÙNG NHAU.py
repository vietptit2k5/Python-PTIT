import math
def check(n) :
    s = ''.join(reversed(str(n)))
    m = int(s)
    if math.gcd(n,m) == 1 : return True
    else : return False
for _ in range(int(input())) :
    n = int(input())
    print("YES") if check(n) else print("NO")
