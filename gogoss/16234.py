# 16234.py 인구 이동
import collections
def bfs(i, j, visit):
    dq = collections.deque()
    visit[i][j] = True
    dq.append((i, j))
    cnt, total, tmp = 1, board[i][j], [(i, j)]
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and not visit[nx][ny] and L <= abs(board[x][y] - board[nx][ny]) <= R:
                cnt, total = cnt + 1, total + board[nx][ny]
                tmp.append((nx, ny))
                dq.append((nx, ny))
                visit[nx][ny] = True
    return (cnt, total, tmp)


def is_end():
    flag = False
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                cnt, total, tmp = bfs(i, j, visit)
                if cnt > 1:
                    for x, y in tmp:
                        board[x][y] = total // cnt
                    flag = True
    if not flag: return True
    else: return False

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
ANS = 0
while True:
    if is_end():
        break
    ANS += 1
print(ANS)