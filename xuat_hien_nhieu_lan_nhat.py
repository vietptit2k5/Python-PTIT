for t in range(int(input())) :
    index = [0]*1000000
    n = int(input())
    arr = list(map(int,input().split()))
    idx = (int)(n/2)
    valua = 1000001
    for i in range(n) :
        index[arr[i]]+=1
        if index[arr[i]] > idx :
            idx=index[arr[i]]
            valua=arr[i]
        elif index[arr[i]]==idx and valua!=1000001 and arr[i] < valua :
            valua = arr[i]
    if valua != 1000001 : print(valua)
    else : print("NO")