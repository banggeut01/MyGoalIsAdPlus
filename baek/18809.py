# 18809.py Gaaaaaaaaaarden
import copy
def solution(gxy, rxy):
    global ANS
    B = copy.deepcopy(board)
    for x, y in gxy:
        B[x][y] = -1
    for x, y in rxy:
        B[x][y] = -1
    cnt = 0
    while gxy and rxy:
        # 초록 배양
        tmp = dict()
        for _ in range(len(gxy)):
            x, y = gxy.pop(0)
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < M and 0 < B[nx][ny]:
                    tmp[(nx, ny)] = 'G'

        # 빨간 배양
        for _ in range(len(rxy)):
            x, y = rxy.pop(0)
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < M and 0 < B[nx][ny]:
                    t = tmp.get((nx, ny))
                    if not t:
                        tmp[(nx, ny)] = 'R'
                    else:
                        if t == 'G':
                            cnt += 1
                            B[nx][ny] = -1
                            tmp[(nx, ny)] = 'F'

        ANS = max(ANS, cnt)
        # if not tmp: return
        # 보드 업데이트
        for key, val in tmp.items():
            x, y = key
            if val == 'R':
                gxy.append(key)
                B[x][y] = -1
            elif val == 'G':
                rxy.append(key)
                B[x][y] = -1

def select_g(k, s, g, r):
    if k == G:
        r = list(set(gr) - set(g))
        gxy, rxy = copy.deepcopy(g), copy.deepcopy(r)
        solution(gxy, rxy)
        return

    for idx in range(s, G + R):
        g.append(gr[idx])
        select_g(k + 1, idx + 1, g, r)
        g.pop()

def select_gr(k, s):
    if k == G + R:
        # g + r 개 중 g 개 뽑기
        g, r = [], []
        select_g(0, 0, g, r)
        return

    for idx in range(s, len(Y)):
        gr.append(Y[idx])
        select_gr(k + 1, idx + 1)
        gr.pop()

ANS = 0
N, M, G, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
Y = [] # 황토땅
for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            Y.append((i, j))
# len(Y) 중 G + R개 뽑기
gr = []
select_gr(0, 0)
print(ANS)