from collections import deque

def bfs(g, n, root, step):
    nxt_vertices = deque()
    is_visited = [False]*n

    nxt_v = root
    nxt_vertices.append(nxt_v)
    is_visited[nxt_v] = True
    step[nxt_v] = 0

    while nxt_vertices:
        now_v = nxt_vertices.popleft()
        for nxt_v in g[now_v]:
            if not is_visited[nxt_v]:
                nxt_vertices.append(nxt_v)
                is_visited[nxt_v] = True
                step[nxt_v] = step[now_v] + 1


    """
    for i in range(n):
        print(f"v:{i+1} step:{step[i]}")
    """

n, m, x, y = map(int, input().split())
g = [[] for _ in range(n)]
x_step = [0]*n
y_step = [0]*n
x -= 1
y -= 1

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

bfs(g, n, x, x_step)
bfs(g, n, y, y_step)

for d_x, d_y in zip(x_step, y_step):
    if d_x < d_y:
         print("X is closer")
    elif d_x == d_y:
        print("Same")
    elif d_x > d_y:
        print("Y is closer")