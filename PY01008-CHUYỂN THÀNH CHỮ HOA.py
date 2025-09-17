s=input()
ss=""
for i  in range(0,len(s),1) :
    n=ord(s[i])
    if n>=97 and n<=122 :
        ss+=chr(n-32)
    else :
        ss+=chr(n)
print(ss)
    
