# 1953.py 탈주범 검거
import sys
sys.stdin = open('1953input.txt', 'r')
import collections
def bfs(x, y, t):
    ret = 1
    visit = [[False] * M for _ in range(N)]
    dq = collections.deque()
    dq.append((x, y))
    visit[x][y] = True
    while t > 1:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            s = board[x][y]
            for el in dir[s]:
                dx, dy = d[el]
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < M and board[nx][ny] and \
                        not visit[nx][ny] and cod[el] in dir[board[nx][ny]]:
                    visit[nx][ny] = True
                    ret += 1
                    dq.append((nx, ny))
                    # print(nx, ny)
        t -= 1
    return ret

d = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 0123:상하좌우
dir = [[], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
cod = {0: 1, 1: 0, 2: 3, 3: 2}

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, bfs(R, C, L)))