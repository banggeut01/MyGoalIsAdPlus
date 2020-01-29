# 11559.py Puyo Puyo

def dfs(x, y, c):
    visit[x][y] = True
    tmp.append((x, y))
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < 12 and -1 < ny < 6 and not visit[nx][ny] and board[nx][ny] == c:
            dfs(nx, ny, c)

board = [list(input()) for _ in range(12)]
flag = True
ans = 0
while flag:
    flag = False
    # 연쇄칸 삭제
    visit = [[False] * 6 for _ in range(12)]
    for i in range(11, -1, -1):
        for j in range(6):
            if not visit[i][j] and board[i][j] != '.':
                tmp = []
                dfs(i, j, board[i][j])
                if len(tmp) >= 4:
                    flag = True
                    for idx in range(len(tmp)):
                        x, y = tmp[idx]
                        board[x][y] = '.'
    # 뿌요 하강
    if flag:
        ans += 1
        for j in range(6):
            i = 11
            while i > -1:
                if board[i][j] == '.':
                    ni = i - 1
                    while ni > -1 and board[ni][j] == '.':
                        ni -= 1
                    if ni > -1:
                        board[i][j], board[ni][j] = board[ni][j], board[i][j]
                i -= 1
print(ans)

