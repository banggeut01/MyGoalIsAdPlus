# 15685.py 사다리 조작
def is_left(x, y):
    if 0 > y - 1: return False
    if not board[x][y - 1]: return False
    return True

def is_right(x, y):
    if y >= N - 1: return False
    if not board[x][y]: return False
    return True

def is_possible(x, y):
    if y + 1 < N - 1 and not board[x][y + 1] or y == N - 2:
        return True
    else:
        return False

def is_answer():
    flag = False
    for j in range(N - 1):
        x, y, s = 0, j, j
        while x < H:
            if is_left(x, y):
                x, y = x + 1, y - 1
            elif is_right(x, y):
                x, y = x + 1, y + 1
            else:
                x, y = x + 1, y
        if y != s:
            flag = True
        if flag:
            return False
    return True

def back(x, y, cur):
    global ANS
    if ANS != -1 and ANS <= cur: return
    if cur > 3: return
    if is_answer():
        if ANS == -1:
            ANS = cur
        else:
            ANS = min(cur, ANS)
        return

    nx, ny = x, y
    while nx < H:
        while ny < N - 1:
            if board[nx][ny]:
                ny += 2
            else:
                if is_possible(nx, ny):
                    board[nx][ny] = 1
                    back(nx, ny + 2, cur + 1)
                    board[nx][ny] = 0
                ny += 1
        nx, ny = nx + 1, 0

N, M, H = map(int, input().split())
board = [[0] * (N - 1) for _ in range(H)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1
ANS = -1
back(0, 0, 0)
print(ANS)