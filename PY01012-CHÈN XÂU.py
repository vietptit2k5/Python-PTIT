S1 = input()
S2 = input()
p = int(input())

index = p - 1
result = S1[:index] + S2 + S1[index:]

print(result)
