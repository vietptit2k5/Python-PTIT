t=int(input())
for i in range(t) :
    n=input()
    ok=1
    for ch in n :
        if ch != "4" and ch != "7" :
            print('NO')
            ok=0
            break
    if ok==1 :
        print('YES')        