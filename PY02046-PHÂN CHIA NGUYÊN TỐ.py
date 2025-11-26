def check(n) :
    if n<2 : return False
    if n%2==0 : return n==2
    for i in range(3,int(n**0.5)+1,2) :
        if n%i==0 : return False
    return True

n = int(input())
ds = list(map(int,input().split()))[:n]
num = []
for x in ds :
    if x not in num :
        num.append(x)

if len(num) < 2:
    print("NOT FOUND")
else:
    for i in range(len(num)-1):
        if check(sum(num[:i+1])) and check(sum(num[i+1:])):
            print(i)
            break
    else:
        print("NOT FOUND")