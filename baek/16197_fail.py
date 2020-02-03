# 16197_fail.py 두 동전
# 백트래킹 시도
# 문제를 계속 잘못읽엇다

'''
동전이 붙어있는 상황
가로로 붙어있으면 c1이 왼쪽, c2가 오른쪽
세로로 붙어있으면 c1이 위쪽, c2가 아래쪽
'''
def go(xy, d):
    dx, dy = d
    nx, ny = xy[0] + dx, xy[1] + dy
    if -1 < nx < N and -1 < ny < M:
        if board[nx][ny] == '.':
            board[xy[0]][xy[1]], board[nx][ny] = '.', 'o'
            return (nx, ny)
        else: return (xy[0], xy[1])
    else:
        board[ny[0]][xy[1]] = '.'
        return (-1, -1)

def coin(k, n1, n2):
    global MIN
    if k + 1 >= MIN: return
    ox1, oy1, ox2, oy2 = n1[0], n1[1], n2[0], n2[1]

    for idx in range(4):
        cnt = 0
        if idx == 0 or idx == 3:
            x1, y1 = go(n1, dir[idx])
            if x1 == -1: cnt += 1
            x2, y2 = go(n2, dir[idx])
            if x2 == -1: cnt += 1
        else:
            x2, y2 = go(n2, dir[idx])
            if x2 == -1: cnt += 1
            x1, y1 = go(n1, dir[idx])
            if x1 == -1: cnt += 1
        if cnt == 1:
            MIN = k + 1
            board[ox1][oy1], board[ox2][oy2] = 'o', 'o'
            return
        elif cnt == 0:
            if not visit[x1][y1][x2][y2]:
                n1, n2 = [x1, y1], [x2, y2]
                visit[x1][y1][x2][y2] = True
                val1, val2 = board[x1][y1], board[x2][y2]
                coin(k + 1, n1, n2)
                n1, n2 = [ox1, oy1], [ox2, oy2]
                board[ox1][oy1], board[ox2][oy2] = 'o', 'o'
                board[x1][y1], board[x2][y2] = val1, val2
            else: return

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n1, n2 = [-1, -1], [-1, -1]
flag = False
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            if n1[0] == -1: n1 = [i, j]
            else: n2 = [i, j]; flag = True; break
    if flag: break
visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
visit[n1[0]][n1[1]][n2[0]][n2[1]] = True
MIN = 0xffffff
coin(0, n1, n2)
if MIN > 10: MIN = -1
print(MIN)


'''동전 업데이트 문제
떨어졌을 때 다시 원래대로 돌려야함
'''

def go(xy, direct, num):
    global n1, n2
    dx, dy = direct
    nx, ny = xy[0] + dx, xy[1] + dy
    if -1 < nx < N and -1 < ny < M:
        if board[nx][ny] == '.':
            board[xy[0]][xy[1]], board[nx][ny] = '.', 'o'
            if num == 1: n1 = [nx, ny]
            else: n2 = [nx, ny]
            return False
        else: return False
    else: return True

def coin(visit):
    global MIN
    for idx in range(min(len(seq), MIN)):
        if dtn.get(seq[:MIN]): return
        d = seq[idx]
        cnt = 0
        if d == 0 or d == 3:
            if go(n1, dir[d], 1): cnt += 1
            if go(n2, dir[d], 2): cnt += 1
        else:
            if go(n2, dir[d], 2): cnt += 1
            if go(n1, dir[d], 1): cnt += 1
        if cnt == 2:
            return
        elif cnt == 1:
            MIN = idx + 1
            dtn[:idx + 1] = True
            return
        else:
            if not visit[n1[0]][n1[1]][n2[0]][n2[1]]:
                visit[n1[0]][n1[1]][n2[0]][n2[1]] = True
            else:
                return



def perm(k):
    if k == 10:
        n1, n2 = on1, on2
        visit = [[[[False] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]
        visit[n1[0]][n1[1]][n2[0]][n2[1]] = True
        coin(visit)
        return

    for idx in range(4):
        seq[k] = idx
        perm(k + 1)

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dtn = dict()
n1, n2 = [-1, -1], [-1, -1]
flag = False
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            if n1[0] == -1: n1 = [i, j]
            else: n2 = [i, j]; flag = True; break
    if flag: break
on1, on2 = n1, n2
MIN = 0xffffff
seq = [-1] * 10
perm(0)
if MIN > 10: MIN = -1
print(MIN)

''' 완탐도 안되었다. BFS로 풀어보자 '''