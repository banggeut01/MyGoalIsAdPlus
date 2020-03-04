# 2819.py 격자판의 숫자 이어 붙이기
def dfs(k, x, y):
    if k == 7:
        SET.add(int(''.join(map(str, num))))
        return
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = x + dx, y + dy
        if -1 < nx < 4 and -1 < ny < 4:
            num[k] = board[nx][ny]
            dfs(k + 1, nx, ny)

for tc in range(1, int(input()) + 1):
    board = [list(map(int, input().split())) for _ in range(4)]
    num = [-1] * 7
    SET = set()
    for i in range(4):
        for j in range(4):
            num[0] = board[i][j]
            dfs(1, i, j)
    print('#{} {}'.format(tc, len(SET)))