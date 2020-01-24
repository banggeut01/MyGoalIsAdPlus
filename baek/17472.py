# 17472 다리 만들기 2

def updateMap(x, y, n):
    visit[x][y] = True
    board[x][y] = n
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < M and board[nx][ny] == 1 and not visit[nx][ny]:
            updateMap(nx, ny, n )

def getBridge(x, y, s):
    initX, initY = x, y
    for dx, dy in dir:
        cnt = 0
        x, y = initX, initY
        while -1 < x + dx < N and -1 < y + dy < M and not board[x + dx][y + dy]:
            x, y, cnt = x + dx, y + dy, cnt + 1
        if -1 < x + dx < N and -1 < y + dy < M and cnt >= 2:
            e = board[x + dx][y + dy]
            ns, ne = min(s, e), max(s, e)
            if bridge.get((ns, ne)):
                bridge[(ns, ne)] = min(bridge[(ns, ne)], cnt)
            else:
                bridge[(ns, ne)] = cnt

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
sumCnt = 0
bridge = dict()
dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
blist = []
MIN = -1

# 섬체크
visit = [[False] * M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 1 and not visit[i][j]:
            updateMap(i, j, sumCnt + 1)
            sumCnt += 1
# 다리길이
for i in range(N):
    for j in range(M):
        if board[i][j]:
            getBridge(i, j, board[i][j])
# 다리정렬
for s, e in bridge.keys():
    blist.append((bridge[(s, e)], s, e))
blist = sorted(blist)
# 다리 고르기
if len(blist) >= sumCnt - 1:
    total = 0
    selected = [False] * (sumCnt + 1)
    w, s, e = blist[0]
    selected[s] = selected[e] = True
    total += w
    picked = 1
    # print(w)
    if sumCnt > 2:
        for idx in range(1, len(blist)):
            w, s, e = blist[idx]
            if (selected[s] == True and selected[e] == False) or (selected[s] == False and selected[e] == True):
                selected[s] = selected[e] = True
                total += w
                picked += 1
                # print(w)
            if picked == sumCnt: break
    MIN = total
print(MIN)