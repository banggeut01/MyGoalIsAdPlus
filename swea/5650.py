# 5650.py 핀볼 게임
import sys
sys.stdin = open('5650input.txt', 'r')
def go(initX, initY, initD):
    global MAX
    x, y, cnt, d = initX, initY, 0, initD
    visit = [[[False] * N for _ in range(N)] for _ in range(4)]
    while True:
        if visit[d][x][y]: return
        visit[d][x][y] = True
        # print(cnt)
        nx, ny = x + xy[d][0], y + xy[d][1]
        if -1 < nx < N and -1 < ny < N:
            num = board[nx][ny]
            if not num:
                if nx == initX and ny == initY:
                    # if MAX < cnt: print(initX, initY, initD)
                    MAX = max(MAX, cnt)
                    return
                else:
                    x, y = nx, ny
            elif 5 < num < 11:
                x, y = hall[(num, nx, ny)]
            elif 0 < num < 6:
                x, y, d = nx, ny, dirDict[(d, num)]
                cnt += 1
            else:
                MAX = max(MAX, cnt)
                return
        # else:
        #     d = dirDict[(d, 5)]
        #     cnt += 1

xy = [(-1, 0), (1, 0), (0, -1), (0, 1)] #0123 상하좌우
dirDict = { (0, 1): 1, (1, 1): 3, (2, 1): 0, (3, 1): 2,
            (0, 2): 3, (1, 2): 0, (2, 2): 1, (3, 2): 2,
            (0, 3): 2, (1, 3): 0, (2, 3): 3, (3, 3): 1,
            (0, 4): 1, (1, 4): 2, (2, 4): 3, (3, 4): 0,
            (0, 5): 1, (1, 5): 0, (2, 5): 3, (3, 5): 2}
hall = dict()
for tc in range(1, int(input()) + 1):
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
            elif not board[i][j] and (i == 0 or i == N - 1 or j == 0 or j == N - 1):
                board[i][j] = 5
    print(board)

    # print(hall)
    # print(board)
    for i in range(N):
        for j in range(N):
            if not board[i][j]:
                for d in range(4):
                    if -1 < i + xy[d][0] < N and -1 < j + xy[d][1] < N:

                        # go(5, 9, 2)
                        # go(2, 3, 3)
                        # go(4, 0, 2)
                        go(i, j, d)
    print('#{} {}'.format(tc, MAX))