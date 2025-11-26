def check(a,b) :
    if len(a) != len(b) :
        return len(a) - len(b)
    else : return (a>b) - (b>a)


while True:
    N_line = input().strip()
    if N_line == '':
        continue
    n = int(N_line)
    if n == 0:
        break
    ds = []
    for _ in range(n) :
        nums = input().strip().lstrip('0')
        if nums == '' : nums = '0'
        ds.append(nums)
    num_max = ds[0]
    num_min = ds[0]
    ok = True
    for num in ds[1:] :
        if check(num,num_max) > 0 : num_max = num
        if check(num,num_min) < 0 : num_min = num
        if num != ds[0] : ok = False
    if ok : print("BANG NHAU")
    else : print(f"{num_min} {num_max}")
