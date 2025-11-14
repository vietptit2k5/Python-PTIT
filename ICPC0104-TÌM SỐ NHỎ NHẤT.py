t = int(input())
for _ in range(t):
    s = input()
    num = ''
    res = float('inf')
    for c in s:
        if c.isdigit():
            num += c
        else:
            if num:
                res = min(res, int(num))
                num = ''
    if num:
        res = min(res, int(num))
    print(res)
