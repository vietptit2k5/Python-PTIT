from collections import Counter
n,m = map(int,input().split())
votes = list(map(int,input().split()))
cnt_votes = Counter(votes)
sort_cnt_votes = sorted(cnt_votes.items(),key = lambda x : (-x[-1],x[0]))
if len(sort_cnt_votes) < 2 : print("NONE")
else :
    valua = sort_cnt_votes[0][1]
    for a,b in sort_cnt_votes[1:] :
        if b < valua :
            print(a)
            break
    else : print("NONE")