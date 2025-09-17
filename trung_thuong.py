for t in range(int(input())) :
    arr = [0]*1001
    n = int(input())
    tmp=-1
    valua = 1001
    for i in range(n) :
        m = int(input())
        arr[m] +=1
        if arr[m] > tmp :
            tmp=arr[m]
            valua = m
        elif arr[m] == tmp :
            if m < valua :
                valua = m
    print(valua)