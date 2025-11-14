ok=0
cnt=0
ds = []
res =  ""
for _ in range(int(input())) :
    tmp = input()
    if tmp != "":
        if ok == 0 :
            res = tmp
            ok = 1
        else :
            cnt+=1
    else : 
        ds.append(f"{res}: {cnt}")
        cnt=0
        ok=0
if ok==1 : 
    ds.append(f"{res}: {cnt}")
for x in ds :
    print(x)

