# 5644.py 무선 충전
import sys
sys.stdin = open('5644input.txt', 'r')
import collections
def bfs(x, y, val, c):
    dq = collections.deque()
    dq.append((x, y))
    visit = [[False] * 10 for _ in range(10)]
    visit[x][y] = True
    board[x][y].append(val)
    t = 0
    while dq and t < c:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < 10 and -1 < ny < 10 and not visit[nx][ny]:
                    visit[nx][ny] = True
                    dq.append((nx, ny))
                    board[nx][ny].append(val)
        t += 1

def go(k, total, ax, ay, bx, by):
    tmp = 0
    if len(board[ax][ay]) and len(board[bx][by]):
        for a in board[ax][ay]:
            for b in board[bx][by]:
                if a == b:
                    tmp = max(tmp, P[a])
                else:
                    tmp = max(tmp, P[a] + P[b])
    else:
        if len(board[ax][ay]):
            for a in board[ax][ay]:
                tmp = max(tmp, P[a])
        if len(board[bx][by]):
            for b in board[bx][by]:
                tmp = max(tmp, P[b])
    total += tmp
    if k == M:
        global MAX
        MAX = total
        return

    go(k + 1, total, ax + D[ad[k]][0], ay + D[ad[k]][1], bx + D[bd[k]][0], by + D[bd[k]][1])


D = [(0, 0), (-1, 0), (0, 1), (1, 0), (0, -1)]
for tc in range(1, int(input()) + 1):
    M, A = map(int, input().split()) # 총이동시간, BC개수
    ad = list(map(int, input().split()))
    bd = list(map(int, input().split()))
    board = [[[] for _ in range(10)] for _ in range(10)]
    P = [0] * A # C충전범위, P처리량
    for idx in range(A):
        j, i, c, p = map(int, input().split())
        P[idx] = p
        bfs(i - 1, j - 1, idx, c)
    MAX = 0
    go(0, 0, 0, 0, 9, 9)
    print('#{} {}'.format(tc, MAX))