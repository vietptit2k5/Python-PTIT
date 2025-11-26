from itertools import combinations


N, K = map(int, input().split())
names = input().split()

unique_names = sorted(set(names))

all_combinations = combinations(unique_names, K)

for combo in all_combinations:
    print(' '.join(combo))