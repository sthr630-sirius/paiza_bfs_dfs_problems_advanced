from collections import deque

n, m = map(int, input().split())
road_time = list(map(int, input().split()))
g = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

nxt_vertices = deque()
is_visited = [False]*n
high_way_time = [0]*n


nxt_v = 0
nxt_vertices.append(nxt_v)
is_visited[nxt_v] = True

while nxt_vertices:
    now_v = nxt_vertices.popleft()
    for nxt_v in g[now_v]:
        if not is_visited[nxt_v]:
            nxt_vertices.append(nxt_v)
            is_visited[nxt_v] = True
            high_way_time[nxt_v] = high_way_time[now_v] + 5

ans = 0

for i in range(n):
    if high_way_time[i] < road_time[i]:
        ans += 1

print(ans)
#print(road_time)
#print(high_way_time)