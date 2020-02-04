# 2117.py 홈 방범 서비스
import sys
sys.stdin = open('2117input.txt', 'r')
import collections
def bfs(x, y): # K - 1 만큼 bfs
    global ANS
    visit = [[False] * N for _ in range(N)]
    dq = collections.deque()
    dq.append((x, y))
    visit[x][y] = True
    if board[x][y]: cnt = 1
    else: cnt = 0
    t = 1
    while dq and t < K:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < N and not visit[nx][ny]:
                    if board[nx][ny]: cnt += 1
                    dq.append((nx, ny))
                    visit[nx][ny] = True
        if cnt * M >= t * t + (t + 1) * (t + 1):
            ANS = max(ANS, cnt)
        t += 1

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split()) #도시크기, 비용
    board = [list(map(int, input().split())) for _ in range(N)]
    ANS = 1 # 서비스 집 개수
    # 서비스 영역은 bfs k-1만큼 했을때
    # bfs 시작 점을 board내 범위로 하면 된다. 벗어나면 손해이니까?
    # k 범위 : 운영비용 k * k + (k - 1) * (k - 1) 이 보드내 전체 집 개수*M보다 작을때 이득이다.
    H = 0 # 전체 집 개수
    for i in range(N):
        for j in range(N):
            if board[i][j]: H += 1

    K = 1
    while H * M >= K * K + (K + 1) * (K + 1):
        K += 1
    # print(K)
    for i in range(N):
        for j in range(N):
            bfs(i, j)
    # bfs(3, 3)
    print('#{} {}'.format(tc, ANS))

