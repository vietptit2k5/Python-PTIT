for t in range(int(input())) :
    ss = input()
    s=""
    for i in range(len(ss)) :
        if i % 2 ==0 :
            a = (ss[i])
        else :
            n = int(ss[i])
            while n>0 :
                s+=a
                n-=1
    print(s)
