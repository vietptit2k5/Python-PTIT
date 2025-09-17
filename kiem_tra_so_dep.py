def check(n) :
    if n[0] == n[1] : return False
    for i in range(len(n)-2) :
        if n[i] != n[i+2] : return False
    return True
if __name__=="__main__" :
    for _ in range(int(input())) :
        n = input()
        print("YES") if check(n) else print("NO")

