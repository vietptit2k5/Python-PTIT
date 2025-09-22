def check(n):
    return all(int(ch) % 2 == 0 for ch in str(n))

arr = []
for i in range(10, 100, 2):
    if check(i) and str(i) == str(i)[::-1]:
        arr.append(i)
for i in range(2, 1000, 2):
    if check(i):
        s = str(i)
        ss = s[::-1]
        tmp = int(s + ss)
        arr.append(tmp)
arr.sort()

for _ in range(int(input())):
    n = int(input())
    pos = []
    idx = 0
    while arr[idx] < n and idx <= len(arr)-1 :
        pos.append(arr[idx])
        idx+=1
    print(*pos)
