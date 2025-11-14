s1 = set(input().lower().split())
s2 = set(input().lower().split())

union = sorted(s1 | s2)
intersection = sorted(s1 & s2)

print(' '.join(union))
print(' '.join(intersection))
