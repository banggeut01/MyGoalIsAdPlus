# 3987.py 보이저 1호
def go(sx, sy, initd):
    global MAX, ANS
    visit = [[[False] * M for _ in range(N)] for _ in range(4)]
    x, y, d, cnt = sx, sy, initd, 1
    while True:
        if not visit[d][x][y]:
            visit[d][x][y] = True
            if board[x][y] == '\\':
                d = dirDict[(1, d)]
            elif board[x][y] == "/":
                d = dirDict[(2, d)]
            nx,  ny = x + xy[d][0], y + xy[d][1]
            if -1 < nx < N and -1 < ny < M:
                if board[nx][ny] == 'C':
                    if MAX < cnt:
                        ANS = alpha[initd]
                        MAX = max(MAX, cnt)
                    return
                else:
                    x, y = nx, ny
                    cnt += 1
            else:
                if MAX < cnt:
                    ANS = alpha[initd]
                    MAX = max(MAX, cnt)
                return
        else:
            MAX = 'Voyager'
            return


# /, \, C
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상우하좌
alpha = {0: 'U', 1: 'R', 2: 'D', 3: 'L'}
N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dirDict = {(1, 0): 3, (1, 3): 0, (1, 1): 2, (1, 2): 1,
           (2, 3): 2, (2, 1): 0, (2, 0): 1, (2, 2): 3}
sx, sy = map(int, input().split())
sx, sy = sx - 1, sy - 1
MAX = 0
ANS = ''
for idx in range(4):
    go(sx, sy, idx)
    if MAX == 'Voyager': ANS = alpha[idx]; break
print(ANS)
print(MAX)