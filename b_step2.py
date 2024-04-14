from collections import  deque

def bfs(x, y, color):
    is_visited = [[False] * m for _ in range(n)]
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    nxt_grids = deque()

    nxt_x = x
    nxt_y = y

    nxt_grids.append([nxt_x, nxt_y])
    is_visited[nxt_x][nxt_y] = True

    while nxt_grids:
        now_grid = nxt_grids.popleft()
        now_x = now_grid[0]
        now_y = now_grid[1]
        for dx, dy in delta:
            nxt_x = now_x + dx
            nxt_y = now_y + dy
            if 0 <= nxt_x < n and 0 <= now_y < m and not is_visited[nxt_x][nxt_y]:
                # -----------check--------
                if screen[nxt_x][nxt_y] == "R""G""B":
                    nxt_grids.append([nxt_x, nxt_y])
                    screen[nxt_x][nxt_y] == color
                #-------------check---------


n, m = map(int, input().split())
screen = [list(input()) for _ in range(n)]

#R --> G
#R --> B
#G --> R
#G --> B
#B --> R
#B --> G



for scri in screen:
    print(scri)