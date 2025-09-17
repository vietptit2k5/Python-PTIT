s=input()
cnt_th=0
cnt_hoa=0
for i in range(0,len(s),1) :
    n=ord(s[i])
    if n>=97 and n<=122 :
        cnt_th+=1
    else :
        cnt_hoa+=1
ss=""
if cnt_th >= cnt_hoa :
    for i in range(0,len(s),1) :
        x=ord(s[i])
        if x>=65 and x<=90 :
            x+=32
        ss+=chr(x)
    print(ss)
else :
    for i in range(0,len(s),1) :
        x=ord(s[i])
        if x>=97 and x<=122 :
            x-=32
        ss+=chr(x)
    print(ss)   