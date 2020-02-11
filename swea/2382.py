# 2382.py 미생물 격리
import sys
sys.stdin = open('2382input.txt', 'r')
def simul():
    global liveCnt
    t = 0
    while t < M and liveCnt > 0:
        for i in range(1, K + 1):
            if not die[i]:
                x, y = pos[i]
                d = D[i]
                dx, dy = xy[d][0], xy[d][1]
                board[x][y].remove(i)
                nx, ny = x + dx, y + dy
                if nx == 0 or nx == N - 1 or ny == 0 or ny == N - 1:
                    micro[i] //= 2
                    if micro[i] == 0:
                        die[i] = True
                        liveCnt -= 1
                    else:
                        D[i] = rev[d]
                        pos[i] = (nx, ny)
                        board[nx][ny].append(i)
                else:
                    pos[i] = (nx, ny)
                    board[nx][ny].append(i)
        for x in range(N):
            for y in range(N):
                if len(board[x][y]) > 1:
                    maxM, tmp = 0, 0
                    for i in board[x][y]:
                        tmp += micro[i]
                        maxM = max(maxM, micro[i])
                    dieTmp = []
                    for i in board[x][y]:
                        if maxM != micro[i]:
                            die[i] = True
                            liveCnt -= 1
                            dieTmp.append(i)
                        else:
                            micro[i] = tmp
                    for i in dieTmp:
                        board[x][y].remove(i)
        t += 1
    cnt = 0
    # import pprint
    # pprint.pprint(board)
    # print(micro)
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                cnt += micro[board[x][y][0]]
    return cnt


xy = [0, (-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
rev = { 1: 2, 2: 1, 3: 4, 4: 3}
for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split()) # 보드크기, 시간, 미생수
    pos = dict()
    D = [0] * (K + 1)
    micro = [0] * (K + 1)
    die = [False] * (K + 1)
    liveCnt = K
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(1, K + 1):
        x, y, m, di = map(int, input().split())
        D[i] = di
        micro[i] = m
        pos[i] = (x, y)
        board[x][y].append(i)
    print('#{} {}'.format(tc, simul()))

