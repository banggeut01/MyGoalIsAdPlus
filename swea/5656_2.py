# 5656_2.py 벽돌 깨기
import copy
def break_box(B):
    ret, t = TOTAL, 0
    dq = []
    while t < N and ret:
        for i in range(H):
            if B[i][selected[t]]:
                if B[i][selected[t]] > 1: dq.append((i, selected[t], B[i][selected[t]]))
                B[i][selected[t]] = 0
                ret -= 1
                break

        while dq and ret:
            x, y, val = dq.pop(0)
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                nx, ny, nval = x + dx, y + dy, val
                while -1 < nx < H and -1 < ny < W and nval > 1:
                    if B[nx][ny]:
                        if B[nx][ny] > 1: dq.append((nx, ny, B[nx][ny]))
                        B[nx][ny] = 0; ret -= 1
                    nval -= 1
                    nx, ny = nx + dx, ny + dy

        for j in range(W):
            tmp = []
            for i in range(H):
                if B[i][j]: tmp.append(B[i][j]); B[i][j] = 0
            for i in range(H - 1, -1, -1):
                if tmp: B[i][j] = tmp.pop()
                else: break
        t += 1
    return ret

def select_col(k):
    if k == N:
        global MIN
        copied = copy.deepcopy(board)
        MIN = min(MIN, break_box(copied))
        return

    for idx in range(W):
        selected[k] = idx
        select_col(k + 1)

for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    selected = [-1] * N
    TOTAL = 0
    for i in range(H):
        for j in range(W):
            if board[i][j]: TOTAL += 1
    MIN = TOTAL
    select_col(0)
    print('#{} {}'.format(tc, MIN))