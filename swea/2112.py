# 2112.py 보호 필름
import sys
sys.stdin = open('2112input.txt', 'r')
def isPass():
    for y in range(W):
        prev, cnt = 2, 0
        for x in range(D):
            if prev == board[x][y]: cnt += 1
            else: cnt = 1; prev = board[x][y]
            if cnt == K: break
        if cnt < K:
            return False
    return True

def back(k, s):
    global MIN
    A, B = [0] * W, [1] * W
    if k >= MIN: return
    if isPass():
        MIN = min(MIN, k)
        return
    if k == D: return

    for idx in range(s, D):
        board[idx], A = A, board[idx]
        back(k + 1, idx + 1)
        board[idx], A = A, board[idx]
        board[idx], B = B, board[idx]
        back(k + 1, idx + 1)
        board[idx], B = B, board[idx]

for tc in range(1, int(input()) + 1):
    D, W, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(D)]
    MIN = D
    back(0, 0)
    print('#{} {}'.format(tc, MIN))
