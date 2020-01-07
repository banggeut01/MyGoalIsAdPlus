# 17822.py 원판 돌리기
import collections
def bfs(r, c, num):
    ret = 1
    visit[r][c] = True
    dq = collections.deque()
    dq.append((r, c))
    board[r][c] = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < M and not visit[nx][ny] and board[nx][ny] == num:
                visit[nx][ny] = True
                dq.append((nx, ny))
                board[nx][ny] = 0
                ret += 1
        if y == 0:
            if not visit[x][M - 1] and board[x][M - 1] == num:
                visit[x][M - 1] = True
                dq.append((x, M - 1))
                board[x][M - 1] = 0
                ret += 1
        elif y == M - 1:
            if not visit[x][0] and board[x][0] == num:
                visit[x][0] = True
                dq.append((x, 0))
                board[x][0] = 0
                ret += 1
    if ret == 1:
        visit[r][c] = False
        board[r][c] = num
        return 0
    else: return ret

N, M, T = map(int, input().split()) # 행, 열, 회전횟수
board = [collections.deque(map(int, input().split())) for _ in range(N)]
tlist = [list(map(int, input().split())) for _ in range(T)]
for x, d, k in tlist: # x배수, d방향, k칸 회전
    for i in range(x - 1, N, x):
        if d: # 반시계
            for _ in range(k):
                board[i].append(board[i].popleft())
        else: # 시계
            for _ in range(k):
                board[i].appendleft(board[i].pop())
    # 인접 개수 찾기
    visit = [[False] * M for _ in range(N)]
    adjNum = 0
    for i in range(N):
        for j in range(M):
            if not visit[i][j] and board[i][j]:
                adjNum += bfs(i, j, board[i][j])
    if not adjNum:
        total, cnt = 0, 0
        for i in range(N):
            for j in range(M):
                if board[i][j]:
                    total += board[i][j]
                    cnt += 1
        if cnt:
            avg = total / cnt
            for i in range(N):
                for j in range(M):
                    if board[i][j]:
                        if board[i][j] > avg:
                            board[i][j] -= 1
                        elif board[i][j] < avg:
                            board[i][j] += 1
        else:
            break
result = 0
for i in range(N): result += sum(board[i])
print(result)