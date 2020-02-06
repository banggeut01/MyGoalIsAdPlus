# 2382.py 미생물 격리

def simul():
    for i in range(1, K + 1):
        if not die(i):


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split()) # 보드크기, 시간, 미생수
    pos = dict()
    D = [0]
    die = [False] * (K + 1)
    board = [[[] for _ in range(N)] for _ in range(N)]
    for i in range(1, K + 1):
        x, y, micro, di = map(int, input().split())
        D.append(di)
        pos[i] = (x, y)
        board[x][y].append(i)
    print('#{} {}'.format(tc, simul()))

