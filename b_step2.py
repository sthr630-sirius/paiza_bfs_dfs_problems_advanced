from collections import  deque

def bfs_mono(screen, color):
    # colorの連結成分
    is_visited = [[False] * m for _ in range(n)]
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    cnt_connect = 0

    nxt_grids = deque()

    for i in range(n):
        for j in range(m):
            nxt_x = i
            nxt_y = j

            if screen[nxt_x][nxt_y] != color or is_visited[nxt_x][nxt_y]:
                continue

            nxt_grids.append([nxt_x, nxt_y])
            is_visited[nxt_x][nxt_y] = True

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

            cnt_connect += 1

    return cnt_connect

def bfs_bi(screen, color):
    #color以外の連結成分
    is_visited = [[False] * m for _ in range(n)]
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    cnt_connect = 0

    nxt_grids = deque()

    for i in range(n):
        for j in range(m):
            nxt_x = i
            nxt_y = j

            if screen[nxt_x][nxt_y] == color or is_visited[nxt_x][nxt_y]:
                continue

            nxt_grids.append([nxt_x, nxt_y])
            is_visited[nxt_x][nxt_y] = True

            while nxt_grids:
                now_grid = nxt_grids.popleft()
                now_x = now_grid[0]
                now_y = now_grid[1]
                for dx, dy in delta:
                    nxt_x = now_x + dx
                    nxt_y = now_y + dy
                    if 0 <= nxt_x < n and 0 <= nxt_y < m and not is_visited[nxt_x][nxt_y]:
                        if screen[nxt_x][nxt_y] != color:
                            nxt_grids.append([nxt_x, nxt_y])
                            is_visited[nxt_x][nxt_y] = True

            cnt_connect += 1

    return cnt_connect



n, m = map(int, input().split())
screen = [list(input()) for _ in range(n)]

ans = 100100100100100

# Rの連結成分
mono_connect_cnt = bfs_mono(screen, "R")
# GBの連結成分
bi_connect_cnt = bfs_bi(screen, "R")
ans = min(ans, mono_connect_cnt+bi_connect_cnt)

# Gの連結成分
mono_connect_cnt = bfs_mono(screen, "G")
# RBの連結成分
bi_connect_cnt = bfs_bi(screen, "G")
ans = min(ans, mono_connect_cnt+bi_connect_cnt)

# Bの連結成分
mono_connect_cnt = bfs_mono(screen, "B")
# RGの連結成分
bi_connect_cnt = bfs_bi(screen, "B")
ans = min(ans, mono_connect_cnt+bi_connect_cnt)

print(ans)






#for scri in screen:
#    print(scri)