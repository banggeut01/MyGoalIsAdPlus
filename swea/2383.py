# 2383. 점심 식사시간

def getDist(isFirstStep, rc):
    r, c = rc
    if isFirstStep: return abs(x1 - r) + abs(y1 - c)
    else: return abs(x2 - r) + abs(y2 - c)

def go(seq, t):
    for i in range(len(seq)):
        if i < 3: seq[i] += t
        else:
            if seq[i - 3] > seq[i]: seq[i] += (t + seq[i - 3] - seq[i])
            else: seq[i] += t
    if len(seq):
        return seq[-1]
    return 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    P = [] # 학생 위치
    x1, y1, x2, y2 = -1, -1, -1, -1
    MIN = 0xffffff
    for i in range(N):
        for j in range(N):
            if board[i][j] > 1:
                if x1 == -1: x1, y1 = i, j
                else: x2, y2 = i, j
            elif board[i][j] == 1:
                P.append((i, j))
    for i in range(1 << len(P)):
        g1, g2 = [], []
        for j in range(len(P)):
            if i & 1 << j: g1.append(getDist(1, P[j]) + 1)
            else: g2.append(getDist(0, P[j]) + 1)
        g1, g2 = sorted(g1), sorted(g2)
        MIN = min(MIN, max(go(g1, board[x1][y1]), go(g2, board[x2][y2])))
    print('#{} {}'.format(tc, MIN))