s = str(input())
ds = []
for i in range(0,len(s),2) :
    if i<len(s)-1 :
        n = int(s[i]+s[i+1])
        if n not in ds :
            ds.append(n)
print(*ds)