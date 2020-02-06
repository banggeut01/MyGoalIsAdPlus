# 2174.py 로봇 시뮬레이션
def test():
    global ANS
    for idx in range(M): # 한명령어에 대해
        r, t, i = cmd[idx]
        initx, inity, d = pos[r]
        x, y = initx, inity
        if t == 'L':
            for _ in range(i % 4):
                d = (d + 3) % 4
            pos[r][2] = d
        elif t == 'R':
            for _ in range(i % 4):
                d = (d + 1) % 4
            pos[r][2] = d
        else:
            dx, dy = dir[d]
            for _ in range(i):
                nx, ny = x + dx, y + dy
                if -1 < nx < B and -1 < ny < A:
                    if board[nx][ny]:
                        ANS = 'Robot ' + str(r) + ' crashes into robot ' + str(board[nx][ny])
                        return
                    x, y = nx, ny
                else:
                    ANS = 'Robot ' + str(r) + ' crashes into the wall'
                    return
            board[initx][inity], board[nx][ny] = 0, r
            pos[r] = [nx, ny, d]

A, B = map(int, input().split()) # 가로, 세로
N, M = map(int, input().split()) # N개로봇, M개 명령
pos = [0]
# 0상 1우 2하 3좌
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 왼쪽은 -1(+3), 오른쪽은 -3(+1)
makeDir = {'N': 0, 'E': 1, 'S': 2, 'W': 3}
ANS = 'OK'
board = [[0] * A for _ in range(B)]
for idx in range(1, N + 1):
    y, x, direct = input().split()
    x, y = B - int(x), int(y) - 1
    pos.append([x, y, makeDir[direct]])
    board[x][y] = idx
cmd = []
for idx in range(M):
    r, t, i = input().split()
    cmd.append([int(r), t, int(i)])
test()
print(ANS)


