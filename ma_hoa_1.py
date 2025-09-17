for t in range(int(input())) :
    ss = input()
    s=""
    cnt=1
    for i in range(0,len(ss)-1,1) :
        if ss[i]==ss[i+1] :
            cnt+=1
        else :
            s+=str(cnt)+ss[i]
            cnt=1
    if ss[len(ss)-1] == ss[len(ss)-2] :
        s+=str(cnt)+ss[len(ss)-1]
    else : s+='1'+ss[len(ss)-1]
    print(s)