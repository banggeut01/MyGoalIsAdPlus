# 17837.py 새로운 게임 2
def getTmp(x, y, nx, ny, tmp, i):
    idx = len(horse[x][y]) - 1
    while idx >= 0:
        pos[horse[x][y][idx]][0], pos[horse[x][y][idx]][1] = nx, ny
        tmp.append(horse[x][y].pop())
        if tmp[-1] == i:
            return
        idx -= 1

def solution():
    turn = 0
    while turn < 1000:
        for i in range(1, K + 1):
            x, y, d = pos[i]
            nx, ny = x + xy[d][0], y + xy[d][1]
            if -1 < nx < N and -1 < ny < N:
                if board[nx][ny] == 0:
                    tmp = []
                    getTmp(x, y, nx, ny, tmp, i)
                    for _ in range(len(tmp)):
                        horse[nx][ny].append(tmp.pop())
                    if len(horse[nx][ny]) >= 4: return turn + 1
                elif board[nx][ny] == 1:
                    tmp = []
                    getTmp(x, y, nx, ny, tmp, i)
                    for _ in range(len(tmp)):
                        horse[nx][ny].append(tmp.pop(0))
                    if len(horse[nx][ny]) >= 4: return turn + 1
                else:
                    new_d = reverse_xy[d]
                    pos[i][2] = new_d
                    nx, ny = x + xy[new_d][0], y + xy[new_d][1]
                    if -1 < nx < N and -1 < ny < N:
                        if board[nx][ny] == 0:
                            tmp = []
                            getTmp(x, y, nx, ny, tmp, i)
                            for _ in range(len(tmp)):
                                horse[nx][ny].append(tmp.pop())
                            if len(horse[nx][ny]) >= 4: return turn + 1
                        elif board[nx][ny] == 1:
                            tmp = []
                            getTmp(x, y, nx, ny, tmp, i)
                            for _ in range(len(tmp)):
                                horse[nx][ny].append(tmp.pop(0))
                            if len(horse[nx][ny]) >= 4: return turn + 1
            else:
                new_d = reverse_xy[d]
                pos[i][2] = new_d
                nx, ny = x + xy[new_d][0], y + xy[new_d][1]
                if -1 < nx < N and -1 < ny < N:
                    if board[nx][ny] == 0:
                        tmp = []
                        getTmp(x, y, nx, ny, tmp, i)
                        for _ in range(len(tmp)):
                            horse[nx][ny].append(tmp.pop())
                        if len(horse[nx][ny]) >= 4: return turn + 1
                    elif board[nx][ny] == 1:
                        tmp = []
                        getTmp(x, y, nx, ny, tmp, i)
                        for _ in range(len(tmp)):
                            horse[nx][ny].append(tmp.pop(0))
                        if len(horse[nx][ny]) >= 4: return turn + 1
        turn += 1
    return -1
N, K = map(int, input().split()) # 체스크기, 말개수
# 0흰, 1빨, 2파
board = [list(map(int, input().split())) for _ in range(N)]
horse = [[[] for _ in range(N)] for _ in range(N)]
xy = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)] # 우좌상하
reverse_xy = {1: 2, 2: 1, 3: 4, 4: 3}
pos = {}
for i in range(1, K + 1):
    x, y, d = map(int, input().split())
    horse[x - 1][y - 1].append(i)
    pos[i] = [x - 1, y - 1, d]
print(solution())