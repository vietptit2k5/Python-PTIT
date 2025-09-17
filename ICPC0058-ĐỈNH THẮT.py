from collections import deque

def bfs(u, v, adj, banned, N):
    if u == banned or v == banned:
        return False
    visited = [False] * (N + 1)
    q = deque([u])
    visited[u] = True
    while q:
        node = q.popleft()
        if node == v:
            return True
        for nxt in adj[node]:
            if nxt != banned and not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)
    return False

t = int(input())
for _ in range(t):
    N, M, u, v = map(int, input().split())
    adj = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
    if not bfs(u, v, adj, -1, N):
        print(0)
        continue
    count = 0
    for x in range(1, N + 1):
        if not bfs(u, v, adj, x, N):
            count += 1
    print(count)
