arr = [0] * 94

def fibo():
    arr[0] = 0
    arr[1] = 1
    for i in range(2, 94):
        arr[i] = arr[i-1] + arr[i-2]

fibo()

for t in range(int(input())):
    a, b = map(int, input().split())
    for n in range(a, b+1):
        print(arr[n], end=" ")
    print()
