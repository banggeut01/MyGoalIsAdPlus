# 17144.py 미세먼지 안녕!

def getPos():
    global cleaner
    for i in range(R):
        if board[i][0] == -1:
            return (i, 0)

def clean_up():
    CR, CC = cleaner
    for x in range(CR - 1, 0, -1):
        board[x][0], board[x - 1][0] = board[x - 1][0], board[x][0]
    for y in range(C - 1):
        board[0][y], board[0][y + 1] = board[0][y + 1], board[0][y]
    for x in range(CR):
        board[x][C - 1], board[x + 1][C - 1] = board[x + 1][C - 1], board[x][C - 1]
    for y in range(C - 1, CC + 1, -1):
        board[CR][y], board[CR][y - 1] = board[CR][y - 1], board[CR][y]
    board[CR][CC + 1] = 0

def clean_down():
    CR, CC = cleaner[0] + 1, cleaner[1]
    for x in range(CR + 1, R - 1):
        board[x][0], board[x + 1][0] = board[x + 1][0], board[x][0]
    for y in range(C - 1):
        board[R - 1][y], board[R - 1][y + 1] = board[R - 1][y + 1], board[R - 1][y]
    for x in range(R - 1, CR, -1):
        board[x][C - 1], board[x - 1][C - 1] = board[x - 1][C - 1], board[x][C - 1]
    for y in range(C - 1, CC + 1, -1):
        board[CR][y], board[CR][y - 1] = board[CR][y - 1], board[CR][y]
    board[CR][CC + 1] = 0

def solution():
    time = 0
    while time < T:
        move = [[0] * C for _ in range(R)]
        for x in range(R):
            for y in range(C):
                if board[x][y] >= 5:
                    tmp = board[x][y] // 5
                    cnt = 0
                    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                        nx, ny = x + dx, y + dy
                        if -1 < nx < R and -1 < ny < C and board[nx][ny] != -1:
                            move[nx][ny] += tmp
                            cnt += 1
                    board[x][y] -= tmp * cnt

        for x in range(R):
            for y in range(C):
                board[x][y] += move[x][y]

        clean_up()
        clean_down()

        time += 1

    total = 0
    for i in range(R):
        for j in range(C):
            if board[i][j] > 0:
                total += board[i][j]
    return total

R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
cleaner = getPos()
print(solution())
