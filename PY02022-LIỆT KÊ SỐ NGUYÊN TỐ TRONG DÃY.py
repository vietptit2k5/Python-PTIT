import math
def check(n) :
    if n<2 : return False
    if n%2==0 : return n==2
    for i in range(3,(int)(math.sqrt(n))+1,2) :
        if n%i==0 : return False
    return True

n = int(input())
arr = list(map(int,input().split()))
pos = [0]*1000000
for i in range(n) :
    if check(arr[i]) :
        pos[arr[i]]+=1
for i in range(n) :
    if pos[arr[i]] > 0 :
        print(arr[i],pos[arr[i]])
        pos[arr[i]]=0