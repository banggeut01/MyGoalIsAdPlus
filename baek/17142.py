# 17142.py 연구소 3
# 활성 인접 비활성 => 활성
import copy, collections
def bfs(B):
    dq = collections.deque()
    D = [[0] * N for _ in range(N)]
    for x, y in valid:
        dq.append((x, y))
        B[x][y] = 3
    ret = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N:
                if B[nx][ny] == 0:
                    B[nx][ny] = 3
                    dq.append((nx, ny))
                    D[nx][ny] = D[x][y] + 1
                    ret = max(ret, D[nx][ny])
                elif B[nx][ny] == 2:
                    B[nx][ny] = 3
                    D[nx][ny] = D[x][y] + 1
                    dq.append((nx, ny))
    for i in range(N):
        for j in range(N):
            if not B[i][j]:
                return 0
    return ret

def comp(k, s):
    if k == M:
        copied = copy.deepcopy(board)
        result = bfs(copied)
        if result:
            global MIN
            if MIN == -1: MIN = result
            else: MIN = min(MIN, result) 
        return

    for idx in range(s, len(virus)):
        valid.append(virus[idx])
        comp(k + 1, idx + 1)
        valid.pop()

N, M = map(int, input().split())
# 1벽, 0빈칸, 2비활성바이러스, 3활성바이러스
# 1이 아니고, 3이 아니면
# (0이면 큐에 넣기 바이러스로 바꾸기)
# (2이면 큐에 넣기)

board = [list(map(int, input().split())) for _ in range(N)]
MIN = -1
virus = []
zero = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == 2: virus.append((i, j))
        elif board[i][j] == 0: zero += 1
if zero:
    valid = [] # 활성
    comp(0, 0)
else: MIN = 0
print(MIN)