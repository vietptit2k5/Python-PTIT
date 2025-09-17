from collections import deque

N, M, X = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

visited = [False] * (N + 1)

q = deque([X])
visited[X] = True
while q:
    u = q.popleft()
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            q.append(v)

res = [i for i in range(1, N + 1) if not visited[i]]

if res:
    for v in sorted(res):
        print(v)
else:
    print(0)
