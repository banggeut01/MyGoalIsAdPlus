# 6087.py 레이저 통신
import collections
def is_end(x, y):
    if x == ex and y == ey: return True
    return False

def bfs(x, y):
    global MIN
    dq = collections.deque()
    dist = [[[-1] * 4 for _ in range(M)] for _ in range(N)]
    # 처음 이동
    for d in range(4):
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if -1 < nx < N and -1 < ny < M:
            if is_end(nx, ny): MIN = 1; return
            elif board[nx][ny] == '.':
                dq.append((nx, ny, d))
                dist[nx][ny][d] = 0
    while dq:
        x, y, d = dq.popleft()
        # 직진
        nx, ny = x + dxy[d][0], y + dxy[d][1]
        if -1 < nx < N and -1 < ny < M:
            if is_end(nx, ny): MIN = min(MIN, dist[x][y][d])
            elif board[nx][ny] == '.' and (dist[nx][ny][d] == -1 or dist[nx][ny][d] > dist[x][y][d]):
                dq.append((nx, ny, d))
                dist[nx][ny][d] = dist[x][y][d]
        # 반사
        for rd in ref_d[d]:
            nx, ny = x + dxy[rd][0], y + dxy[rd][1]
            if -1 < nx < N and -1 < ny < M:
                if is_end(nx, ny): MIN = min(MIN, dist[x][y][d] + 1)
                elif board[nx][ny] == '.' and (dist[nx][ny][rd] == -1 or dist[nx][ny][rd] > dist[x][y][d] + 1):
                    dq.append((nx, ny, rd))
                    dist[nx][ny][rd] = dist[x][y][d] + 1


dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
ref_d = {0: [2, 3], 1: [2, 3], 2: [0, 1], 3: [0, 1]}
M, N = map(int, input().split())
board = [list(input()) for _ in range(N)]
sx, sy, ex, ey = -1, -1, -1, -1
MIN = 0xffffff
for i in range(N):
    for j in range(M):
        if board[i][j] == 'C':
            if sx == -1:
                sx, sy = i, j
            else:
                ex, ey = i, j

bfs(sx, sy)
print(MIN)