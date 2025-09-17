arr = []
while len(arr) < 10:
    arr.extend(map(int, input().split()))
arr = arr[:10]
myset = set()
for i in range(10) :
    myset.add(arr[i] % 42)
print(len(myset))
