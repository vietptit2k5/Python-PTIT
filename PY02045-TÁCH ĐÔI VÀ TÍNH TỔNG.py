s = input().strip()
while len(s) > 1 :
    n = int(len(s)/2)
    a = int(s[:n])
    b = int(s[n:])
    print(a+b)
    s = str(a+b)