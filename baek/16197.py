# 16197.py 두 동전


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]
'''
동전이 붙어있는 상황
가로로 붙어있으면 c1이 왼쪽, c2가 오른쪽
세로로 붙어있으면 c1이 위쪽, c2가 아래쪽
'''
def back(k):
    global MIN
    if MIN > 0: return

    for idx in range(4): # 0, 3이면 n1부터 아니면 n2부터
        # 두동전 모두 떨어지면 return
        # 두동전 모두 안떨어지면 다음 back()
        # 한동전만 떨어지면 답갱신 후 return
        
        # loc[0]이 무조건 위, 왼쪽
        dx, dy = dir[idx]
        s, e, d = 0, 1, 1
        f = 0
        if idx == 0 or idx == 3:
            e, s, d = 0, 1, -1
        for i in range(s, e + d, d):
            nx, ny = loc[i][0], loc[i][1]
            if -1 < nx < N and -1 < ny < M:
                if
            else:
                board[nx][ny], board[x][y] = '.'
                f += 1
        

    if k == 10: return

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
loc = [-1, -1], [-1, -1]
for i in range(N):
    for j in range(M):
        if board[i][j] == 'o':
            if loc[0][0] == -1:
                loc[0][0], loc[0][1] = i, j
            else:
                loc[1][0], loc[1][1] = i, j
if abs(loc[0][0] - loc[1][0]) + abs(loc[0][1] - loc[1][1]) == 1: # 인접
    if loc[0][0] > loc[1][0] or loc[0][1] > [1][1]: # loc[1]가 위 or 왼쪽
        loc[0], loc[1] = loc[1], loc[0]
MIN = 0
back(0)
if MIN == 0: MIN = -1
print(MIN)