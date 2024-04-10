from collections import deque

def OutField(field, screen):
    #print(f"screen:{screen}")
    for fi in field:
        print("".join(fi))

    #print("-------------")

n, m, x, y, k = map(int, input().split())
field = [list(input()) for _ in range(n)]
x -= 1
y -= 1

is_visited = [[False]*m for _ in range(n)]
step = [[0]*m for _ in range(n)]

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
nxt_grids = deque()

nxt_x = x
nxt_y = y
nxt_grids.append([nxt_x, nxt_y])
is_visited[nxt_x][nxt_y] = True
step[nxt_x][nxt_y] = 0
screen = 0
field[nxt_x][nxt_y] = "+"
#field[nxt_x][nxt_y] = str(step[nxt_x][nxt_y])


while nxt_grids:
    now_x, now_y = nxt_grids.popleft()
    for dx, dy in delta:
        nxt_x = now_x + dx
        nxt_y = now_y + dy
        if 0 <= nxt_x < n and 0 <= nxt_y < m and field[nxt_x][nxt_y] != "#" and not is_visited[nxt_x][nxt_y]:
            nxt_grids.append([nxt_x, nxt_y])
            is_visited[nxt_x][nxt_y] = True
            step[nxt_x][nxt_y] = step[now_x][now_y] + 1

            if step[nxt_x][nxt_y] == screen + 1:
                OutField(field, screen)
                screen += 1

            field[nxt_x][nxt_y] = "+"
            #field[nxt_x][nxt_y] = str(step[nxt_x][nxt_y])

    if screen >= k:
        break

for _ in range(screen, k):
    OutField(field, screen)