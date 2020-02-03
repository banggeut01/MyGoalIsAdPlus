# 16197.py 두 동전
import collections
def bfs():
    visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    visit[tmp1[0]][tmp1[1]][tmp2[0]][tmp2[1]] = True
    dq.append((tmp1[0], tmp1[1], tmp2[0], tmp2[1]))
    t = 0
    while dq and t < 10:
        for _ in range(len(dq)):
            x1, y1, x2, y2 = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                cnt = 0
                nx1, ny1, nx2, ny2 = x1 + dx, y1 + dy, x2 + dx, y2 + dy
                if -1 < nx1 < N and -1 < ny1 < M:
                    if board[nx1][ny1] == '#': nx1, ny1 = x1, y1
                else: cnt += 1
                if -1 < nx2 < N and -1 < ny2 < M:
                    if board[nx2][ny2] == '#': nx2, ny2 = x2, y2
                else: cnt += 1
                if cnt == 1:
                    global MIN
                    MIN = t + 1
                    return
                elif cnt == 0:
                    if not visit[nx1][ny1][nx2][ny2]:
                        dq.append((nx1, ny1, nx2, ny2))
                        visit[nx1][ny1][nx2][ny2] = True
        t += 1



N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
# dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dq = collections.deque()
tmp1, tmp2 = [-1, -1], [-1, -1]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            if tmp1[0] == -1: tmp1 = [i, j]
            else: tmp2 = [i, j]

MIN = 0xffffff
bfs()
if MIN > 10: MIN = -1
print(MIN)