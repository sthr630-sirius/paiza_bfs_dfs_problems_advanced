from collections import deque

n, m, x, y, =map(int, input().split())
x -= 1
y -= 1
field = [list(input()) for _ in range(n)]
is_visited = [[False]*m for _ in range(n)]
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

#for fi in field:
#    print(fi)

nxt_grids = deque()

nxt_x = x
nxt_y = y
nxt_grids.append([nxt_x, nxt_y])
is_visited[nxt_x][nxt_y] = True
field[nxt_x][nxt_y] = "+"

while nxt_grids:
    now_grid = nxt_grids.popleft()
    now_x = now_grid[0]
    now_y = now_grid[1]
    for dx, dy in delta:
        nxt_x = now_x + dx
        nxt_y = now_y + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < m and field[nxt_x][nxt_y] != "#" and not is_visited[nxt_x][nxt_y]:
            nxt_grids.append([nxt_x, nxt_y])
            is_visited[nxt_x][nxt_y] = True
            field[nxt_x][nxt_y] = "+"

for fi in field:
    print("".join(fi))