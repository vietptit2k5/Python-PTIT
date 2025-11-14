def convert(X, b):
    group = {2: 1, 4: 2, 8: 3, 16: 4}[b]
    while len(X) % group != 0:
        X = '0' + X  
    res = ''
    for i in range(0, len(X), group):
        val = int(X[i:i+group], 2)
        if b == 16:
            if val < 10:
                res += str(val)
            else:
                res += chr(ord('A') + val - 10)
        else:
            res += str(val)
    return res.lstrip('0') or '0'


with open("DATA.in", "r") as f:
    lines = [line.strip() for line in f if line.strip() != ""]

T = int(lines[0])
idx = 1
for _ in range(T):
    b = int(lines[idx]); idx += 1
    X = lines[idx]; idx += 1
    print(convert(X, b))
