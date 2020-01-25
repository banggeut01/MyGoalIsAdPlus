# 2105.py 디저트 카페
# 0 -> 0, 1
# 1 -> 1, 2
# 2 -> 0 만큼
# 3 -> 1 만큼
def back(x, y, d, total, up, down):
    if d == 0:
        nx, ny = x + dir[d][0], y + dir[d][1]
        if -1 < nx < N and -1 < ny < N and not visit[board[nx][ny]]:
            visit[board[nx][ny]] = True
            back(nx, ny, d, total + 1, up + 1, down)
            visit[board[nx][ny]] = False
        nx, ny = x + dir[d + 1][0], y + dir[d + 1][1]
        if -1 < nx < N and -1 < ny < N and not visit[board[nx][ny]]:
            visit[board[nx][ny]] = True
            back(nx, ny, d + 1, total + 1, up, down + 1)
            visit[board[nx][ny]] = False
    elif d == 1:
        nx, ny = x + dir[d][0], y + dir[d][1]
        if -1 < nx < N and -1 < ny < N and not visit[board[nx][ny]]:
            visit[board[nx][ny]] = True
            back(nx, ny, d, total + 1, up, down + 1)
            visit[board[nx][ny]] = False
        nx, ny = x + dir[d + 1][0], y + dir[d + 1][1]
        d, nup = d + 1, up
        tmp = []
        while nup > 0:
            nx, ny = x + dir[d][0], y + dir[d][1]
            if -1 < nx < N and -1 < ny < N and not visit[board[nx][ny]]:
                tmp.append(board[nx][ny])
                visit[board[nx][ny]] = True
                x, y, total, nup = nx, ny, total + 1, nup - 1
            else:
                while tmp:
                    visit[tmp.pop()] = False
                return
        else:
            back(nx, ny, d, total, up, down)
            while tmp:
                visit[tmp.pop()] = False
    elif d == 2:
        ndown, d = down, d + 1
        tmp = []
        while ndown > 1:
            nx, ny = x + dir[d][0], y + dir[d][1]
            if -1 < nx < N and -1 < ny < N and not visit[board[nx][ny]]:
                x, y, total, ndown = nx, ny, total + 1, ndown - 1
            else:
                while tmp:
                    visit[tmp.pop()] = False
                return
        else:
            global MAX
            MAX = max(MAX, total)
            while tmp:
                visit[tmp.pop()] = False

dir = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * 100
    MAX = -1

    for i in range(1, N):
        for j in range(N - 2):
            visit[board[i][j]] = True
            back(i, j, 0, 1, 0, 0) # x, y, d, total, up, down
            visit[board[i][j]] = False
    print('#{} {}'.format(tc, MAX))