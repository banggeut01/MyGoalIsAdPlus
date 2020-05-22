# 2468.py 안전 영역
import sys
sys.setrecursionlimit(10000)
def dfs(x, y, h):
    visit[x][y] = True
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N and not visit[nx][ny] and board[nx][ny] > h:
            dfs(nx, ny, h)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ANS = 1
max_h = 1
for i in range(N):
    for j in range(N):
        if board[i][j] > max_h:
            max_h = board[i][j]

for h in range(1, max_h):
    visit = [[False] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] > h and not visit[i][j]:
                dfs(i, j, h)
                cnt += 1
    ANS = max(ANS, cnt)
print(ANS)
