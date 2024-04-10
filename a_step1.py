from collections import deque

n, x, y = map(int, input().split())

x -= 1
y -= 1

g = [[] for _ in range(n)]
for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

nxt_vertices = deque()
is_visited = [False]*n
time = [0]*n
cnt_child = 0

nxt_v = x
nxt_vertices.append(x)
is_visited[x] = True

if len(g[x]) >= 2:
    time[x] = 10
else:
    time[x] = 0

while nxt_vertices:
    now_v = nxt_vertices.popleft()

    for nxt_v in g[now_v]:
        if not is_visited[nxt_v]:
            nxt_vertices.append(nxt_v)
            is_visited[nxt_v] = True
            time[nxt_v] = time[now_v] + 5

print(time[y])