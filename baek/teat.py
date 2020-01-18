import collections
def rotation(i, j): # 반시계 방향 회전, board[i]에 추가
    tmp = [[0] * 5 for _ in range(5)]
    # 바깥
    tmp[4][0], tmp[3][0], tmp[2][0], tmp[1][0] = board[i][j][0][0], board[i][j][0][1], board[i][j][0][2], board[i][j][0][3]
    tmp[0][0], tmp[0][1], tmp[0][2], tmp[0][3] = board[i][j][0][4], board[i][j][1][4], board[i][j][2][4], board[i][j][3][4]
    tmp[0][4], tmp[1][4], tmp[2][4], tmp[3][4] = board[i][j][4][4], board[i][j][4][3], board[i][j][4][2], board[i][j][4][1]
    tmp[4][4], tmp[4][3], tmp[4][2], tmp[4][1] = board[i][j][4][0], board[i][j][3][0], board[i][j][2][0], board[i][j][1][0]
    # 안쪽
    tmp[3][1], tmp[2][1] = board[i][j][1][1], board[i][j][1][2]
    tmp[1][1], tmp[1][2] = board[i][j][1][3], board[i][j][2][3]
    tmp[1][3], tmp[2][3] = board[i][j][3][3], board[i][j][3][2]
    tmp[3][3], tmp[3][2] = board[i][j][3][1], board[i][j][2][1]
    # 가운데
    tmp[2][2] = board[i][j][2][2]
    for a in board[i]:
        if a == tmp:
            return False
    board[i].append(tmp)
    return True

def bfs(sr, sc, er, ec):
    dq = collections.deque()
    visit = [[[False] * 5 for _ in range(5)] for _ in range(5)]
    dq.append((0, sr, sc))
    visit[0][sr][sc] = True
    ret = 0
    tmp = len(dq)
    while dq:
        for _ in range(tmp):
            x, y, z = dq.popleft()
            for dx, dy, dz in (-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1):
                nx, ny, nz = x + dx, y + dy, z + dz
                if -1 < nx < 5 and -1 < ny < 5 and -1 < nz < 5 and not visit[nx][ny][nz] and miro[nx][ny][nz]:
                    if nx == 4 and ny == er and nz == ec:
                    visit[nx][ny][nz] = True
                    dq.append((nx, ny, nz))
        ret += 1
        tmp = len(dq)
    return -1

def perm(k):
    if k == 5:
        global MIN
        for idx in range(4):
            sr, sc = S[idx]
            if not miro[0][sr][sc]: continue
            er, ec = E[idx]
            ret = bfs(sr, sc, er, ec)
            if ret != -1:
                if MIN == -1: MIN = ret
                else: MIN = min(MIN, ret)
        return

    for i in range(5):
        if not visit[i]:
            brng = len(board[i])
            for j in range(brng):
                if k == 0 and not board[i][j][0][0] and not board[i][j][0][4] \
                        and not board[i][j][4][0] and not board[i][j][4][4] : continue
                visit[i] = True
                miro.append(board[i][j])
                perm(k + 1)
                visit[i] = False
                miro.pop()

board = [[] for _ in range(5)]
for i in range(5):
    board[i].append([list(map(int, input().split())) for _ in range(5)])
    for j in range(3):
        if not rotation(i, j):
            break
visit = [False] * 5 # 판 순서
miro = []
S = [(0, 0), (0, 4), (4, 0), (4, 4)]
E = [(4, 4), (4, 0), (0, 4), (0, 0)]
MIN = -1
perm(0)
print(MIN)