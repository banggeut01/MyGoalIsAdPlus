# 3055_2.py
# 탈출
# 3055.py 탈출
import collections

# 비어있는 곳은 '.'
# 물이 차있는 지역은 '*' => .
# 돌 'X'
# 비버의 굴은 'D'
# 고슴도치의 위치는 'S' => .

# 고슴도치 이동 *
# 물 이동 *
# 돌을 통과할 수 없음
# 물이 찰 에정인 칸으로 고슘도치 이동 x
# 물에 빠지기 때문에
def bfs():
    # 1-비버visit, 0-물visit
    t = 0
    while dq:
        flag = False
        for _ in range(len(dq)):
            x, y, w = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny = x + dx, y + dy
                if -1 < nx < R and -1 < ny < C:
                    if not w: # 비버
                        if not visit[nx][ny]:
                            if board[nx][ny] == '.':
                                visit[nx][ny] = True
                                dq.append((nx, ny, 0))
                                flag = True
                            elif board[nx][ny] == 'D':
                                return t + 1
                    elif w: # 물
                        # 비버가 이미 간곳은 가지 않아도 된다.
                        if board[nx][ny] == '.' and not visit[nx][ny]:
                            board[nx][ny] = '*'
                            dq.append((nx, ny, 1))
        if not flag: return "KAKTUS"
        t += 1
    return "KAKTUS"

R, C  = map(int, input().split())
board = [list(input()) for _ in range(R)]
biber = [-1, -1]
dq = collections.deque()
# 비버의 visit
visit = [[False] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if board[i][j] == '*':
            dq.append((i, j, 1))
        elif board[i][j] == 'S':
            biber = [i, j]
            board[i][j] = '.'
            visit[i][j] = True
dq.append((biber[0], biber[1], 0))
print(bfs())
