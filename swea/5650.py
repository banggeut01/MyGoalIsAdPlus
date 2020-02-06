# 5650.py 핀볼 게임
import sys
sys.stdin = open('5650input.txt', 'r')
def go(initX, initY, d):
    global MAX
    x, y, cnt = initX, initY, 0
    while True:
        nx, ny = x + xy[d][0], y + xy[d][1]
        if -1 < nx < N and -1 < ny < N:
            num = board[nx][ny]
            if not num:
                if nx == initX and ny == initY:
                    MAX = max(MAX, cnt)
                    return
                else:
                    x, y = nx, ny
            elif 5 < num:
                x, y = hall[(num, nx, ny)]
            elif 0 < num:
                x, y, d = nx, ny, dirDict[(d, num)]
                cnt += 1
            else:
                MAX = max(MAX, cnt)
                return
        else:
            MAX = max(MAX, cnt * 2 + 1)
            return

xy = [(-1, 0), (1, 0), (0, -1), (0, 1)] #0123 상하좌우
dirDict = { (0, 1): 1, (1, 1): 3, (2, 1): 0, (3, 1): 2,
            (0, 2): 3, (1, 2): 0, (2, 2): 1, (3, 2): 2,
            (0, 3): 2, (1, 3): 0, (2, 3): 3, (3, 3): 1,
            (0, 4): 1, (1, 4): 2, (2, 4): 3, (3, 4): 0,
            (0, 5): 1, (1, 5): 0, (2, 5): 3, (3, 5): 2}

for tc in range(1, int(input()) + 1):
    hall = dict()
    MAX = 0
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if 5 < board[i][j] < 11:
                hallNum = board[i][j]
                if not hall.get(hallNum):
                    hall[hallNum] = (i, j)
                else:
                    x, y = hall[hallNum]
                    hall[(hallNum, x, y)] = (i, j)
                    hall[(hallNum, i, j)] = (x, y)

    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                for d in range(4):
                    if -1 < i + xy[d][0] < N and -1 < j + xy[d][1] < N:
                        go(i, j, d)
    print('#{} {}'.format(tc, MAX))