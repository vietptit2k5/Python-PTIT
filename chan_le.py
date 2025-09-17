def check(n) :
    tong = sum(int(digit) for digit in str(n))
    if tong % 10 != 0 : return False
    for i in range(len(n)-1) :
        if abs(int(n[i])-int(n[i+1])) != 2 : return False
    return True

for _ in range(int(input())) :
    n = input()
    print("YES") if check(n) else print("NO")