# 1949.py 등산로 조성
# dfs
def back(x, y, state, cnt):
    global MAX
    # if MAX < cnt:
    #     print(tmp)
    #     print(board)
    MAX = max(MAX, cnt)
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N and not visit[nx][ny]:
            if board[nx][ny] < board[x][y]:
                visit[nx][ny] = True
                # tmp.append((nx, ny))
                back(nx, ny, state, cnt + 1)
                visit[nx][ny] = False
                # tmp.pop()
            elif not state:
                diff = board[nx][ny] - board[x][y] + 1
                if diff <= K:
                    state = 1
                    visit[nx][ny] = True
                    rem = board[nx][ny]
                    board[nx][ny] -= diff
                    # tmp.append((nx, ny))
                    back(nx, ny, state, cnt + 1)
                    state = 0
                    visit[nx][ny] = False
                    board[nx][ny] = rem
                    # tmp.pop()

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    MAX = 0
    H = 0
    # tmp = []
    for i in range(N):
        for j in range(N):
            if H < board[i][j]: H = board[i][j]
    for i in range(N):
        for j in range(N):
            if board[i][j] == H:
                visit = [[False] * N for _ in range(N)]
                visit[i][j] = True
                # print((i, j))
                back(i, j, 0, 1)
    print('#{} {}'.format(tc, MAX))