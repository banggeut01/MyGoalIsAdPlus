# 2105.py 디저트 카페
# 0 -> 0, 1
# 1 -> 1, 2
# 2 -> 0 만큼
# 3 -> 1 만큼
import sys
sys.stdin = open('2105input.txt', 'r')
def isPossible(nx, ny):
    if -1 < nx < N and -1 < ny < N and not visit[board[nx][ny]]: return True
    else: return False

def back(x, y, d, total, up, down):
    if d == -1: # 초기 상태 -> 0
        d = 0
        nx, ny = x + dir[d][0], y + dir[d][1]
        if isPossible(nx, ny):
            visit[board[nx][ny]] = True
            back(nx, ny, d, total + 1, up + 1, down)
            visit[board[nx][ny]] = False
    elif d == 0: # 우상
        nx, ny = x + dir[d][0], y + dir[d][1]
        if isPossible(nx, ny):
            visit[board[nx][ny]] = True
            back(nx, ny, d, total + 1, up + 1, down)
            visit[board[nx][ny]] = False
        nx, ny = x + dir[d + 1][0], y + dir[d + 1][1]
        if isPossible(nx, ny):
            visit[board[nx][ny]] = True
            back(nx, ny, d + 1, total + 1, up, down + 1)
            visit[board[nx][ny]] = False
    elif d == 1: # 우하
        nx, ny = x + dir[d][0], y + dir[d][1]
        if isPossible(nx, ny):
            visit[board[nx][ny]] = True
            back(nx, ny, d, total + 1, up, down + 1)
            visit[board[nx][ny]] = False
        d, nup = d + 1, up
        tmp = []
        while nup > 0:
            nx, ny = x + dir[d][0], y + dir[d][1]
            if isPossible(nx, ny):
                tmp.append(board[nx][ny])
                visit[board[nx][ny]] = True
                x, y, total, nup = nx, ny, total + 1, nup - 1
            else:
                while tmp: visit[tmp.pop()] = False
                break
        else:
            back(nx, ny, d, total, up, down)
            while tmp: visit[tmp.pop()] = False
    elif d == 2: # 좌하
        ndown, d = down, d + 1
        tmp = []
        while ndown > 0:
            nx, ny = x + dir[d][0], y + dir[d][1]
            if isPossible(nx, ny):
                tmp.append(board[nx][ny])
                visit[board[nx][ny]] = True
                x, y, total, ndown = nx, ny, total + 1, ndown - 1
            else:
                while tmp: visit[tmp.pop()] = False
                break
        else:
            global MAX
            # if total == 32:
            #     print(total, end=" ; ")
            #     for idx in range(len(visit)):
            #         if visit[idx]: print(idx, end=' ')
            #     print('=========================')
            MAX = max(MAX, total)
            while tmp: visit[tmp.pop()] = False

dir = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * 101
    MAX = -1

    for i in range(1, N):
        for j in range(N - 2):
            back(i, j, -1, 0, 0, 0) # x, y, d, total, up, down
    print('#{} {}'.format(tc, MAX))