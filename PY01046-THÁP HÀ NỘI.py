def in_check(n,a,b) :
    print(a,'->',b)
def quaylui(n,a,b,c) :
    if(n==1) : in_check(n,a,c)
    else :
        quaylui(n-1,a,c,b)
        in_check(n,a,c)
        quaylui(n-1,b,a,c)

n = int(input())
a="A"
b="B"
c="C"
quaylui(n,a,b,c)
