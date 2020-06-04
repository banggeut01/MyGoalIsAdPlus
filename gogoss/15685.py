# 15685.py 드래곤 커브
def is_square(x, y):
    if not board[x][y]: return False
    if not board[x][y + 1]: return False
    if not board[x + 1][y]: return False
    if not board[x + 1][y + 1]: return False
    return True

board = [[0] * 101 for _ in range(101)]
N = int(input())
xy = [(0, 1), (-1, 0), (0, -1), (1, 0)]
new_d = {0: 1, 1: 2, 2: 3, 3: 0}
for _ in range(N):
    y, x, d, g = map(int, input().split())
    nx, ny = x + xy[d][0], y + xy[d][1]
    board[x][y], board[nx][ny] = 1, 1
    memo = [d]
    for _ in range(g):
        tmp = []
        for i in range(len(memo) - 1, -1 , -1):
            new = new_d[memo[i]]
            tmp.append(new)
            nx, ny = nx + xy[new][0], ny + xy[new][1]
            board[nx][ny] = 1
        memo += tmp
cnt = 0
for i in range(100):
    for j in range(100):
       if is_square(i, j):
           cnt += 1
print(cnt)