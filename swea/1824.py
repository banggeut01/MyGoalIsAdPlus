# 1824.py 혁진이의 프로그램 검증
def hyeokming():
    visit = [[[False] * C for _ in range(R)] for _ in range(16)]
    x, y, char = 0, 0, 0
    while True:
        
        if visit[char][x][y]: return False
        else: visit[char][x][y] = True
    return False

for tc in range(1, int(input()) + 1):
    R, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(R)]
    # i < 0 => i += R
    # i >= R => i -= R
    # j < 0 => j += C
    # j >= C => j -= C
    result = "NO"
    if hyeokming(): result = "YES"
    print('#{} {}'.format(tc, result))