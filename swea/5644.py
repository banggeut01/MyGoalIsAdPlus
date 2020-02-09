# 5644.py 무선 충전
import collections
def bfs(x, y, val, c):
    dq = collections.deque()
    dq.append((x, y))
    visit = [[False] * 10 for _ in range(10)]
    visit[x][y] = True
    t = 0
    while dq and t < c:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < 10 and -1 < ny < 10 and not visit[nx][ny]:
                    board[nx][ny] += val
        t += 1

D = [0, (-1, 0), (0, 1), (1, 0), (0, -1)]
for tc in range(1, int(input()) + 1):
    M, A = map(int, input().split()) # 총이동시간, BC개수
    am = list(map(int, input().split()))
    bm = list(map(int, input().split()))
    board = [[0] * 10 for _ in range(10)]
    P = [0] * A # C충전범위, P처리량
    for idx in range(A):
        c, r, c, p = map(int, input().split())
        P[idx] = p
        # board[x - 1][y - 1] += 1 << idx
        bfs(r - 1, c - 1, 1 << idx, c)
    print(board)