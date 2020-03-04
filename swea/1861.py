# 1861.py 정사각형 방
def back(x, y, k):
    D[initX][initY] = max(D[initX][initY], k)
    if k == N * N: return

    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N and not visit[nx][ny] and board[nx][ny] == board[x][y] + 1:
            if not D[nx][ny]:
                visit[x][y] = True
                back(nx, ny, k + 1)
                visit[x][y] = False
            else:
                D[initX][initY] = D[initX][initY] + D[nx][ny]


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    MAX, ANS = 0, N * N
    D = [[0] * N for _ in range(N)]
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            visit[i][j] = True
            initX, initY = i, j
            back(i, j, 1)
            visit[i][j] = False
    for i in range(N):
        for j in range(N):
            if D[i][j] > MAX:
                MAX, ANS = D[i][j], board[i][j]
            elif D[i][j] == MAX:
                ANS = min(board[i][j], ANS)
    print('#{} {} {}'.format(tc, ANS, MAX))