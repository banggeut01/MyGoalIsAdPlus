# 2589.py 보물섬
import collections
def bfs(x, y):
    dq = collections.deque()
    dq.append((x, y))
    D = [[0] * M for _ in range(N)]
    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True
    ret = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and not visit[nx][ny] and board[nx][ny] == 'L':
                dq.append((nx, ny))
                D[nx][ny] = D[x][y] + 1
                ret = D[nx][ny]
                visit[nx][ny] = True
    return ret

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
MAX = 0
for i in range(N):
    for j in range(M):
        if board[i][j] == 'L':
            MAX = max(MAX, bfs(i, j))
print(MAX)