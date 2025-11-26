from collections import Counter
s = str(input())
ds = []
for i in range(0,len(s),2) :
    if i < len(s)-1 :
        n = int(str(s[i]+s[i+1]))
        ds.append(n)
couter_ds = [0]*100
num = []
for i in ds :
    couter_ds[i]+=1
    if i not in num :
        num.append(i)
for i in num :
    print(f"{i} {couter_ds[i]}")