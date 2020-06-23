# 16236.py 아기 상어
import collections
def bfs(tmp, x, y, z):
    ret = 0
    dq = collections.deque()
    visit = [[False] * N for _ in range(N)]
    dq.append((x, y))
    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < N and not visit[nx][ny]:
                    if not board[nx][ny]:
                        dq.append((nx, ny))
                        visit[nx][ny] = True
                    elif board[nx][ny] < z: # 먹이가능
                        tmp.append((nx, ny))
                        visit[nx][ny] = True
                    elif board[nx][ny] == z:
                        visit[nx][ny] = True
                        dq.append((nx, ny))
        ret += 1
        if len(tmp) > 0:
            return ret
    return 0

def solution():
    global _x, _y
    z, zcnt, cnt = 2, 0, 0
    while True:
        tmp = []
        cnt += bfs(tmp, _x, _y, z)
        if len(tmp) == 0:
            return cnt
        else:
            tmp = sorted(tmp)
            _x, _y = tmp[0][0], tmp[0][1]
            board[_x][_y] = 0
            zcnt += 1
            if zcnt == z:
                z += 1
                zcnt = 0

def getPos():
    for i in range(N):
        for j in range(N):
            if board[i][j] == 9:
                board[i][j] = 0
                return (i, j)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
_x, _y = getPos()
print(solution())