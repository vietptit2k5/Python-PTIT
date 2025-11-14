import sys

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()
it = iter(data)
t = int(next(it))
out = []
for _ in range(t):
    b = int(next(it))
    s = next(it)
    if b == 2:
        out.append(s)
        continue
    group = {4:2,8:3,16:4}[b]
    pad = (-len(s)) % group
    s = '0'*pad + s
    res_chars = []
    for i in range(0, len(s), group):
        val = int(s[i:i+group], 2)
        if val < 10:
            res_chars.append(str(val))
        else:
            res_chars.append(chr(ord('A') + val - 10))
    out.append(''.join(res_chars))
sys.stdout.write('\n'.join(out))
