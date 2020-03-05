# 4012.py 요리사
def get_synergy(g):
    total = 0
    for x in range(len(g) - 1):
        for y in range(x + 1, len(g)):
            total += board[g[x]][g[y]] + board[g[y]][g[x]]
    return total

for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    MIN = 0xffffff
    for i in range(1 << N):
        g1, g2 = [], []
        for j in range(N):
            if i & 1 << j: g1.append(j)
            else: g2.append(j)
        if len(g1) == N // 2:
            MIN = min(MIN, abs(get_synergy(g1) - get_synergy(g2)))
    print('#{} {}'.format(tc, MIN))
