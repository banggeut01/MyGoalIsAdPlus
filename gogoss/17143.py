# 17143.py 낚시왕
def move():
    global shark
    tmp = {} # (x, y): num, s, d, z
    for key, val in shark.items():
        x, y, s, d, z = val
        board[x][y] = 0
        idx = 0
        nx, ny = x, y
        while idx < s:
            if -1 < nx + xy[d][0] < R and -1 < ny + xy[d][1] < C:
                nx, ny = nx + xy[d][0], ny + xy[d][1]
            else:
                d = reverse_d[d]
                nx, ny = nx + xy[d][0], ny + xy[d][1]
            idx += 1
        if tmp.get((nx, ny)):
            if tmp[(nx, ny)][3] < z:
                tmp[(nx, ny)] = (key, s, d, z)
        else:
            tmp[(nx, ny)] = (key, s, d, z)
    shark = {}
    for key, val in tmp.items():
        x, y = key
        num, s, d, z = val
        shark[num] = (x, y, s, d, z)
        board[x][y] = num

def solution():
    global shark
    ret = 0
    for j in range(C):
        for i in range(R):
            if board[i][j]:
                r, c, s, d, z = shark.pop(board[i][j])
                ret += z
                board[i][j] = 0
                break
        move()
    return ret

R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
shark = {}
xy = [(0, 0), (-1, 0), (1, 0), (0, 1), (0, -1)]
reverse_d = {1: 2, 2: 1, 3: 4, 4: 3}
for  i in range(1, M + 1):
    # (r, c)좌표, s속력, d이동방향, z크기
    r, c, s, d, z = map(int, input().split())
    r, c = r - 1, c - 1
    shark[i] = (r, c, s, d, z)
    board [r][c] = i
print(solution())