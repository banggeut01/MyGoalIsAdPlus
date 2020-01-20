# 1824.py 혁진이의 프로그램 검증

# '?'에서만 백트래킹
def hyeokming(x, y, char, d):
    while True:
        s = board[x][y] # state
        if s.isdigit(): char = int(s)
        elif s == '<': d = 2
        elif s == '>': d = 3
        elif s == '^': d = 0
        elif s == 'v': d = 1
        elif s == '_':
            if char == 0: d = 3
            else: d = 0
        elif s == '|':
            if char == 0: d = 1
            else: d = 0
        elif s == '@':
            global result
            result = "YES"
            return True
        elif s == '+':
            if char == 15: char = 0
            else: char += 1
        elif s == '-':
            if char == 0: char = 15
            else: char -= 1
        elif s == '?':
            for dx, dy in dir:
                nx, ny = x + dx, y + dy

        if visit[d][char][x][y]: return
        else: visit[d][char][x][y] = True
    return

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 위, 아, 왼, 오
for tc in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    # i < 0 => i += R
    # i >= R => i -= R
    # j < 0 => j += C
    # j >= C => j -= C
    result = "NO"
    visit = [[[[False] * C for _ in range(R)] for _ in range(16)] for _ in range(4)]
    hyeokming(0, 0, 0, 3)
    print('#{} {}'.format(tc, result))