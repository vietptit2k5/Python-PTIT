m = input()
n=''.join(reversed(m))
cnt=0
s=""
for i in range(len(n)) :
    cnt+=1
    s=str(n[i])+s
    if cnt==3 and i !=len(n)-1 :
        s=","+s
        cnt=0
print(s)

