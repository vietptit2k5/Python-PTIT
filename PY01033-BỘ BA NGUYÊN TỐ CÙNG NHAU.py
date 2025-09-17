import math
a,b=map(int,input().split())
arr=[]
for i in range(a,b-1) :
    for j in range(i+1,b) :
        for f in range(j+1,b+1) :
            if math.gcd(i,j)==1 and math.gcd(j,f)==1 and math.gcd(f,i)==1 :
                arr.append(i)
                arr.append(j)
                arr.append(f)
                print("(" + ", ".join(str(x) for x in arr) + ")")
                arr=[]