def solve(n) :
    cnt=0
    if n%7==0 : return n
    while cnt <= 1000 :
        s = "".join(reversed(str(n)))
        m = int(s)
        n+=m
        cnt+=1
        if n%7==0 :
            return n
            break
    if cnt > 1000 : return -1
if __name__ == "__main__" :
    for _ in range(int(input())) :
        n = int(input())
        print(solve(n))