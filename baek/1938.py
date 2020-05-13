# 1938.py 통나무 옮기기
import collections
def is_dochack(x, y, is_garo):
    if x == exy[1][0] and y == exy[1][1] and is_garo == e_is_garo:
        return True
    else:
        return False

def move_possible(x, y, is_garo):
    if is_garo == 1:
        for idx in range(-1, 2):
            if 0 > x or x >= N or 0 > y + idx or y + idx >= N or board[x][y + idx] == '1': return False
    else:
        for idx in range(-1, 2):
            if 0 > x + idx or x + idx >= N or 0 > y or y >= N or board[x + idx][y] == '1': return False
    return True

def rot_possible(x, y):
    for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
        nx, ny = x + dx, y + dy
        if 0 > nx or nx >= N or 0 > ny or ny >= N or board[nx][ny] == '1': return False
    return True

def bfs(x, y, is_garo):
    global MIN
    dq = collections.deque()
    dq.append((x, y, is_garo))
    while dq:
        x, y, is_garo = dq.popleft()
        if is_garo == 1: d = 1; rot_d = 0
        else: d = 0; rot_d = 1
        # 이동
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and dist[nx][ny][d] == -1 and move_possible(nx, ny, is_garo):
                if is_dochack(nx, ny, is_garo): return dist[x][y][d] + 1
                dist[nx][ny][d] = dist[x][y][d] + 1
                dq.append((nx, ny, is_garo))
        # 회전
        if dist[x][y][rot_d] == -1 and rot_possible(x, y):
            if is_dochack(x, y, is_garo*(-1)): return dist[x][y][d] + 1
            dist[x][y][rot_d] = dist[x][y][d] + 1
            dq.append((x, y, is_garo*(-1)))
    return 0

N = int(input())
board = [list(input()) for _ in range(N)]
bxy, exy, b_is_garo, e_is_garo = [], [], -1, -1
# 좌표
for i in range(N):
    for j in range(N):
        if board[i][j] == 'B':
            if j + 1 < N and board[i][j + 1] == 'B':
                bxy = [[i, j], [i, j + 1], [i, j + 2]]
                b_is_garo = 1
            else:
                bxy = [[i, j], [i + 1, j], [i + 2, j]]
            for x, y in bxy:
                board[x][y] = '0'
        elif board[i][j] == 'E':
            if j + 1 < N and board[i][j + 1] == 'E':
                exy = [[i, j], [i, j + 1], [i, j + 2]]
                e_is_garo = 1
            else:
                exy = [[i, j], [i + 1, j], [i + 2, j]]
            for x, y in exy:
                board[x][y] = '0'

dist = [[[-1] * 2 for _ in range(N)] for _ in range(N)]
if b_is_garo == 1:
    dist[bxy[1][0]][bxy[1][1]][1] = 0
else:
    dist[bxy[1][0]][bxy[1][1]][0] = 0
print(bfs(bxy[1][0], bxy[1][1], b_is_garo))