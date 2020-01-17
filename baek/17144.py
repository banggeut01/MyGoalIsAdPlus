# 17144.py 미세먼지 안녕!
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
for i in range(2, R):
    if board[i][0] == -1:
        cleaner = i
        break

for _ in range(T):
    # 확산
    move = [[0] * C for _ in range(R)]
    for x in range(R):
        for y in range(C):
            if board[x][y] >= 5:
                tmp = board[x][y] // 5
                cnt = 0
                for dx, dy in (-1, 0), (1, 0), (0, 1), (0, -1):
                    nx, ny = x + dx, y + dy
                    if -1 < nx < R and -1 < ny < C and board[nx][ny] != -1:
                        move[nx][ny] += tmp
                        cnt += 1
                board[x][y] -= tmp * cnt
    for x in range(R):
        for y in range(C):
            board[x][y] += move[x][y]

    # 순환
    x, y = cleaner - 1, 0
    while x > 0:
        board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
        x -= 1
    while y < C - 1:
        board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
        y += 1
    while x < cleaner:
        board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
        x += 1
    while y > 1:
        board[x][y], board[x][y - 1] = board[x][y - 1], board[x][y]
        y -= 1
    board[x][1] = 0
    x, y = cleaner + 2, 0
    while x < R - 1:
        board[x][y], board[x + 1][y] = board[x + 1][y], board[x][y]
        x += 1
    while y < C - 1:
        board[x][y], board[x][y + 1] = board[x][y + 1], board[x][y]
        y += 1
    while x > cleaner + 1:
        board[x][y], board[x - 1][y] = board[x - 1][y], board[x][y]
        x -= 1
    while y > 1:
        board[x][y], board[x][y - 1] = board[x][y - 1], board[x][y]
        y -= 1
    board[x][1] = 0

total = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            total += board[i][j]
print(total)