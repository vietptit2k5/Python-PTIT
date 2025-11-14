def time_to_minutes(t):
    h, m = map(int, t.split(':'))
    return h*60 + m

n = int(input())
stations = {}
order = []
for _ in range(n):
    name = input().strip()
    start = input().strip()
    end = input().strip()
    rain = float(input().strip())
    duration = time_to_minutes(end) - time_to_minutes(start)
    if name not in stations:
        stations[name] = {'total_rain': 0.0, 'total_time': 0}
        order.append(name)
    stations[name]['total_rain'] += rain
    stations[name]['total_time'] += duration

for idx, name in enumerate(order, 1):
    total_rain = stations[name]['total_rain']
    total_time = stations[name]['total_time']
    avg_per_hour = total_rain / total_time * 60
    print(f"T{idx:02d} {name} {avg_per_hour:.2f}")
