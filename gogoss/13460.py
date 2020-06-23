# 13460.py 구슬 탈출 2
def back():
    global R, B
    x, y = R
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy















        if -1 < nx < N and -1 < ny < M and board[nx][ny] != '#':
            if board[nx][ny] == 'O':


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
R, B, O = (-1, -1), (-1, -1), (-1, -1)
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            R = (i, j)
        elif board[i][j] == 'B':
            B = (i, j)
        elif board[i][j] == 'O':
            O = (i, j)
visit = [[False] * M for i in range(N)]
ANS = -1
back()
print(ANS)