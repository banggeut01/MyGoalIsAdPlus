# 1861_teacher.py
def dfs(x, y):
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N and board[nx][ny] - board[x][y] == 1 \
                and not visit[board[nx][ny]]:
            visit[board[nx][ny]] = 1
            dfs(nx, ny)

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [0] * (N * N + 1)
    for i in range(N):
        for j in range(N):
            if not visit[board[i][j]]:
                dfs(i, j)
    max_cnt, min_num = 0, N * N
    cnt = 1
    # print(visit)
    for i in range(N * N, -1 , -1):
        if visit[i]:
            cnt += 1
            if cnt >= max_cnt: max_cnt, min_num = cnt, i
        else:
            cnt = 1
    print('#{} {} {}'.format(tc, min_num - 1, max_cnt))