from collections import deque

n, m, x, y, z = map(int, input().split())
x -= 1

facility = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)


nxt_vertices = deque()
is_visited = [False]*n
distance = [0]*n

nxt_v = x
nxt_vertices.append(nxt_v)
is_visited[nxt_v] = True
distance[nxt_v] = 0

while nxt_vertices:
    now_v = nxt_vertices.popleft()
    for nxt_v in g[now_v]:
        if not is_visited[nxt_v]:
            nxt_vertices.append(nxt_v)
            is_visited[nxt_v] = True
            distance[nxt_v] = distance[now_v] + 5

cnt = 0
ans = []

for i in range(n):
    if distance[i] <= y and facility[i] == z:
        cnt += 1
        ans.append(i+1)

print(cnt)
for i in range(len(ans)):
    print(ans[i])