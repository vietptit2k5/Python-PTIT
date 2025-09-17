for t in range(int(input())) :
    n = int(input())
    arrA=list(map(int,input().split()))
    arrB=list(map(int,input().split()))
    arrA.sort()
    arrB.sort()
    ok=1
    for i in range(n) :
        if arrA[i] > arrB[i] :
            ok=0
            break
    if ok==1 : print("YES")
    else : print("NO")