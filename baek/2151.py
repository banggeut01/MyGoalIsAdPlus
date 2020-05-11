# 거울 설치 2151.py

import collections
def bfs():
    global MIN
    def is_goal(x2, y2):
        if x2 == door_x2 and y2 == door_y2: return True
        else: return False
    dq = collections.deque()
    dist = [[[0] * 4 for _ in range(N)] for _ in range(N)]
    visit = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    for d in range(4):
        nx, ny = door_x1 + dxy[d][0], door_y1 + dxy[d][1]
        if -1 < nx < N and -1 < ny < N and (board[nx][ny] == "!" or board[nx][ny] == "."):
            visit[nx][ny][d] = True
            dq.append((nx, ny, d))
    while dq:
        x, y, d = dq.popleft()
        # 직진 - '!', '.'에서
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if -1 < nx < N and -1 < ny < N and (not visit[nx][ny][d] or dist[nx][ny][d] > dist[x][y][d]):
            if board[nx][ny] == '#':
                if is_goal(nx, ny):
                    MIN = min(MIN, dist[x][y][d])
            elif board[nx][ny] != '*':
                visit[nx][ny][d] = True
                dist[nx][ny][d] = dist[x][y][d]
                dq.append((nx, ny, d))
        # 반사
        if board[x][y] == '!':
            for i in reflect[d]:
                nx, ny = x + dxy[i][0], y + dxy[i][1]
                if -1 < nx < N and -1 < ny < N and (not visit[nx][ny][i] or dist[nx][ny][i] > dist[x][y][d] + 1):
                    if board[nx][ny] == '#':
                        if is_goal(nx, ny):
                            MIN = min(MIN, dist[x][y][d] + 1)
                    elif board[nx][ny] != '*':
                        visit[nx][ny][i] = True
                        dist[nx][ny][i] = dist[x][y][d] + 1
                        dq.append((nx, ny, i))
    return False

N = int(input())
board = [list(input()) for _ in range(N)]
dxy = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
reflect = { 0: [2, 3], 1: [2, 3], 2: [0, 1], 3: [0, 1]}
door_x1, door_y1, door_x2, door_y2 = -1, -1, -1, -1
MIN = 0xffffff
for i in range(N):
    for j in range(N):
        if board[i][j] == '#':
            if door_x1 == -1:
                door_x1, door_y1 = i, j
            else:
                door_x2, door_y2 = i, j
if abs(door_x1 - door_x2) + abs(door_y1 - door_y2) == 1:MIN = 0
else: bfs()
print(MIN)