def match(num, pattern):
    num = str(num)
    if len(num) != len(pattern):
        return False
    for i in range(len(num)):
        if pattern[i] != '?' and pattern[i] != num[i]:
            return False
    return True

ops = ['+', '-', '*', '/']

def solve(expr):
    parts = expr.split()
    a_pat, op_pat, b_pat, _, c_pat = parts
    for op in (ops if op_pat == '?' else [op_pat]):
        for a in range(10, 100):
            if not match(a, a_pat):
                continue
            for b in range(10, 100):
                if not match(b, b_pat):
                    continue
                if op == '+':
                    c = a + b
                elif op == '-':
                    c = a - b
                elif op == '*':
                    c = a * b
                else:  # '/'
                    if b == 0 or a % b != 0:
                        continue
                    c = a // b
                if 10 <= c <= 99 and match(c, c_pat):
                    return f"{a} {op} {b} = {c}"
    return "WRONG PROBLEM!"

for _ in range(int(input())):
    print(solve(input().strip()))
