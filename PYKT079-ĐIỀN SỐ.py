for _ in range(int(input())) :
    n = int(input())
    ds = list(map(int,input().split()))
    nums = []
    for x in ds :
        if x not in nums :
            nums.append(x)
    valua_max = max(x for x in nums)
    valua_min = min(x for x in nums)
    ans = valua_max-valua_min-len(nums)+1
    print(ans)
