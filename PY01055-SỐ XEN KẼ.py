def is_xen_ke(number: str) -> str:
    if len(number) % 2 == 0:
        return "NO"
    if number[0] == number[1]:
        return "NO"
    odd_positions = number[::2]
    if all(ch == odd_positions[0] for ch in odd_positions):
        return "YES"
    else:
        return "NO"

t = int(input())
for _ in range(t):
    num = input().strip()
    print(is_xen_ke(num))