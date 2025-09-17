P = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
pos = {v : i for i,v in enumerate(P)}
ok=1
while ok==1 :
    arr = list(map(str,input().split()))
    K = (int)(arr[0])
    if K == 0 : ok=0
    else :
        s = arr[1]
        ss = ""
        for i in range(len(s)) :
            n = pos[s[i]]
            ss+=P[(n+K)%28]
        ss_rev = ''.join(reversed(ss))
        print(ss_rev)

             