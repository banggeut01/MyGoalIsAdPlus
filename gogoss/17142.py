# 17142.py 연구소 3
import copy
import collections

def bfs():
    global ANS
    dq = collections.deque()
    B = copy.deepcopy(board)
    for x, y in selected:
        B[x][y] = 3
        dq.append((x, y))

    time, zero = 0, 0
    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < N and B[nx][ny] != 1 and B[nx][ny] != 3:
                    if B[nx][ny] == 0: zero += 1
                    B[nx][ny] = 3
                    dq.append((nx, ny))

        time += 1
        if total == zero:
            if ANS == -1:
                ANS = time
            else:
                ANS = min(ANS, time)
            return

def comp(k, s):
    if k == M:
        bfs()
        return

    for i in range(s, len(virus)):
        selected.append(virus[i])
        comp(k + 1, i + 1)
        selected.pop()

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
virus, selected = [], []
ANS = -1
total = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            total += 1
if total == 0:
    ANS = 0
else:
    comp(0, 0)
print(ANS)