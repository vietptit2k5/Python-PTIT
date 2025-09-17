n = int(input().strip())
students = []

for _ in range(n):
    name = input().strip()
    c, t = map(int, input().split())
    students.append((name, c, t))

students.sort(key=lambda x: (-x[1], x[2], x[0]))

for s in students:
    print(s[0], s[1], s[2])
