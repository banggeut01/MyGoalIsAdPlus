# 4131.py 활주로 건설
import sys
sys.stdin = open('4131input.txt', 'r')

def isPossible(x, y, d, prev):
    dx, dy = d
    visit[x][y] = True
    for _ in range(X - 1):
        x, y = x + dx, y + dy
        if -1 < x < N and -1 < y < N and board[x][y] == prev and not visit[x][y]:
            visit[x][y] = True
        else: return False
    return True

xy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 상하좌우
for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    ANS = 0
    # 행
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        prev = board[i][0]
        j = 1
        while j < N:
            if board[i][j] != prev:
                if board[i][j] == prev + 1:
                    if not isPossible(i, j - 1, xy[2], prev): break
                    else: prev = board[i][j]; j += 1
                elif board[i][j] == prev - 1:
                    if not isPossible(i, j, xy[3], board[i][j]): break
                    else: prev = board[i][j]; j += X
                else: break
            else: j += 1
        else: ANS += 1
            # print('ANS + 1: {}행'.format(i))


    # 열
    visit = [[False] * N for _ in range(N)]
    for j in range(N):
        prev = board[0][j]
        i = 1
        while i < N:
            if board[i][j] != prev:
                if board[i][j] == prev + 1:
                    if not isPossible(i - 1, j, xy[0], prev): break
                    else: prev = board[i][j]; i += 1
                elif board[i][j] == prev - 1:
                    if not isPossible(i, j, xy[1], board[i][j]): break
                    else: prev = board[i][j]; i += X
                else: break
            else: i += 1
        else: ANS += 1
            # print('ANS + 1: {}열'.format(j))
    print('#{} {}'.format(tc, ANS))