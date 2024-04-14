from collections import  deque

def bfs(screen, connect, color):
    is_visited = [[False] * m for _ in range(n)]
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    cnt = 0

    nxt_grids = deque()

    for i in range(n):
        for j in range(m):
            nxt_x = i
            nxt_y = j

            if screen[nxt_x][nxt_y] != color or is_visited[nxt_x][nxt_y]:
                continue

            nxt_grids.append([nxt_x, nxt_y])
            is_visited[nxt_x][nxt_y] = True
            connect[nxt_x][nxt_y] = color + str(cnt)

            while nxt_grids:
                now_grid = nxt_grids.popleft()
                now_x = now_grid[0]
                now_y = now_grid[1]
                for dx, dy in delta:
                    nxt_x = now_x + dx
                    nxt_y = now_y + dy
                    if 0 <= nxt_x < n and 0 <= nxt_y < m and not is_visited[nxt_x][nxt_y]:
                        if screen[nxt_x][nxt_y] == color:
                            nxt_grids.append([nxt_x, nxt_y])
                            is_visited[nxt_x][nxt_y] = True
                            connect[nxt_x][nxt_y] = color+str(cnt)

            cnt += 1

n, m, k = map(int, input().split())
screen = [list(input()) for _ in range(n)]
connect = [[""]*m for _ in range(n)]

# Rの連結成分
bfs(screen, connect, "R")
# Gの連結成分
bfs(screen, connect, "G")
# Bの連結成分
bfs(screen, connect, "B")

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    if connect[x1-1][y1-1] == connect[x2-1][y2-1]:
        print("Yes")
    else:
        print("No")
