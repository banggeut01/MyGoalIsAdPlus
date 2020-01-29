# 16197.py 두 동전 
# 순열로 다시!



'''
동전이 붙어있는 상황
가로로 붙어있으면 c1이 왼쪽, c2가 오른쪽
세로로 붙어있으면 c1이 위쪽, c2가 아래쪽
'''
def coin(visit):
    global MIN
    for idx in range(10):
        if idx + 1 == MIN: return
        dx, dy = dir[order[idx]]
        s, e, d = 0, 1, 1
        f = 0
        if idx == 0 or idx == 3:
            e, s, d = 0, 1, -1
        for i in range(s, e + d, d):
            x, y = loc[i][0], loc[i][1]
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M:
                if board[nx][ny] == '.':
                    board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
            else:
                board[x][y], f = '.', f + 1
        if f == 1:
            MIN = idx + 1
        elif f == 2:
            return

def perm(k):
    global MIN
    if MIN == 10 and k >= MIN: return
    if k == 10:
        visit = [[[[False] * M for _ in range(N)] for _ in range(M) for _ in range(N)]
        visit[loc[0][0]][loc[0][1]][1][0]][loc[1][1]] = True
        coin(visit)
        return
    for idx in range(4):
        order[k] = idx
        perm(k + 1)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
loc = [[-1, -1], [-1, -1]]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            if loc[0][0] == -1:
                loc[0][0], loc[0][1] = i, j
            else:
                loc[1][0], loc[1][1] = i, j
if abs(loc[0][0] - loc[1][0]) + abs(loc[0][1] - loc[1][1]) == 1: # 인접
    if loc[0][0] > loc[1][0] or loc[0][1] > loc[1][1]: # loc[1]가 위 or 왼쪽
        loc[0], loc[1] = loc[1], loc[0]
MIN = 0xffffff
order = [-1] * 10
perm(0)
if MIN > 10: MIN = -1
print(MIN)