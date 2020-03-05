# 1953_2.py 탈주범 검거
import collections
def bfs(x, y):
    dq = collections.deque()
    dq.append((x, y))
    visit = [[False] * M for _ in range(N)]
    visit[x][y] = True
    ret = 1
    T = 1
    while T < L and dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dir in D[board[x][y]]:
                nx, ny = x + xy[dir][0], y + xy[dir][1]
                if -1 < nx < N and -1 < ny < M and not visit[nx][ny] and rev[dir] in D[board[nx][ny]]:
                    ret += 1
                    dq.append((nx, ny))
                    visit[nx][ny] = True
        T += 1
    return ret

xy = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 0상, 1하, 2좌, 3우
D = [[-1], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]
rev = { 0: 1, 1: 0, 2: 3, 3: 2}
for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split()) # NM:행열, RC:맨홀뚜껑, L:소요시간
    board = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, bfs(R, C)))