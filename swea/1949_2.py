# 1949_2.py 등산로 조성
import sys
sys.stdin = open('1949input.txt', 'r')
def back(k, flag, x, y):
    global ANS
    ANS = max(ANS, k)
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N and not visit[nx][ny]:
            if board[nx][ny] < board[x][y]:
                visit[nx][ny] = True
                back(k + 1, flag, nx, ny)
                visit[nx][ny] = False
            elif flag and board[nx][ny] - board[x][y] + 1 <= K:
                tmp, board[nx][ny] = board[nx][ny], board[x][y] - 1
                visit[nx][ny] = True
                back(k + 1, 0, nx, ny)
                board[nx][ny] = tmp
                visit[nx][ny] = False

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    MAX_H = 0
    ANS = 0
    for i in range(N):
        for j in range(N):
            MAX_H = max(MAX_H, board[i][j])
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] == MAX_H:
                visit[i][j] = True
                back(1, 1, i, j)
                visit[i][j] = False
    print('#{} {}'.format(tc, ANS))