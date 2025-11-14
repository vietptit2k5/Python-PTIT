from collections import deque
t = int(input())
arr = list(map(int,input().split()))
st = deque()
for x in arr :
    if len(st)==0 : st.append(x)
    else :
        y = st[-1]
        if (x+y)%2==0 :
            st.pop()
        else : st.append(x)
print(len(st))
    
        
