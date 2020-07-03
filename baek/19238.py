# 19238.py 스타트 택시
import collections
def sbfs():
    cnt = 0
    if board[D[0]][D[1]] > 1:
        return (board[D[0]][D[1]], cnt)
    visit = [[False] * N for _ in range(N)]
    dq = collections.deque()
    dq.append((D[0], D[1]))
    ansList = []
    while dq:
        flag = False
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < N and not visit[nx][ny] and board[nx][ny] != 1:
                    if board[nx][ny] > 1:
                        flag = True
                        ansList.append((nx, ny, board[nx][ny]))
                    else:
                        dq.append((nx, ny))
                        visit[nx][ny] = True
        if flag:
            ansList = sorted(ansList)
            return (ansList[0][2], cnt + 1)
        cnt += 1
    return (-1, -1)

def edfs(sr, sc, er, ec):
    visit = [[False] * N for _ in range(N)]
    dq = collections.deque()
    dq.append((sr, sc))
    cnt = 0
    while dq:
        for _ in range(len(dq)):
            x, y = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < N and not visit[nx][ny] and board[nx][ny] != 1:
                    if nx == er and ny == ec:
                        return cnt + 1
                    dq.append((nx, ny))
                    visit[nx][ny] = True
        cnt += 1
    return -1

N, M, G = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dest = dict()
D = list(map(int, input().split()))
D[0], D[1] = D[0] - 1, D[1] - 1
for i in range(2, M + 2):
    sx, sy, ex, ey = map(int, input().split())
    board[sx - 1][sy - 1] = i
    dest[i] = (sx - 1, sy - 1, ex - 1, ey - 1)
cnt = 0
ANS = -1
for _ in range(M):
    num, dist1 = sbfs()
    if num == -1: break
    dist2 = edfs(dest[num][0], dest[num][1], dest[num][2], dest[num][3])
    dist = dist1 + dist2
    if dist2 == -1 or dist > G: break
    board[dest[num][0]][dest[num][1]] = 0
    D[0], D[1] = dest[num][2], dest[num][3]
    G = G - dist + dist2 * 2
    # print(num, dest[num], dist1, dist2, G)
else:
    ANS = G
print(ANS)
