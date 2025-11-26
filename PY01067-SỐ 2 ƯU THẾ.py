def is_dominant_two(tri_str):
    count_2 = tri_str.count('2')
    return count_2 > len(tri_str) / 2

def generate_dominant_trinary(n):
    result = []
    i = 0
    while len(result) < n:
        tri = ''
        num = i
        if num == 0:
            tri = '0'
        else:
            while num > 0:
                tri = str(num % 3) + tri
                num //= 3
        if is_dominant_two(tri):
            result.append(tri)
        i += 1
    return result

t = int(input())
for _ in range(t):
    n = int(input())
    res = generate_dominant_trinary(n)
    print(' '.join(res))