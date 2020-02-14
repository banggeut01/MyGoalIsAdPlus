# 5656.py 벽돌 깨기
import sys
sys.stdin = open('5656input.txt', 'r')
import copy, collections
def breakBrick(B): # B:보드
    global MIN
    for j in seq:
        dq = collections.deque()
        i = 0
        while i < H and not B[i][j]:
            i += 1
        if i == H: continue
        if B[i][j] > 1:
            dq.append((i, j, B[i][j]))
        B[i][j] = 0
        while dq:
            x, y, val = dq.popleft()
            for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                idx = 1
                while idx < val:
                    nx, ny = x + dx, y + dy
                    if -1 < nx < H and -1 < ny < W:
                        if B[nx][ny]:
                            if B[nx][ny] > 1: dq.append((nx, ny, B[nx][ny]))
                            B[nx][ny] = 0
                    else: break
                    idx += 1
        # 보드 업데이트
        for j in range(W):
            tmp = []
            for i in range(H):
                if B[i][j]:
                    tmp.append(B[i][j])
                B[i][j] = 0
            for i in range(H - 1, -1, -1):
                B[i][j] = tmp.pop()
                if not tmp: break
    cnt = 0
    print(B)
    for i in range(H):
        for j in range(W):
            if B[i][j]: cnt += 1
    MIN = min(MIN, cnt)
        # for j in range(W):
        #     i = H - 1
        #     while B[i][j] and i > -1:
        #         i += 1
        #     if i > 0:
        #         ni = i - 1
        #         while ni > -1 and not B[ni][j]:
        #             ni -= 1
        #         if ni > -1 and B[ni][j]:
        #             B[ni][j], B[i][j] = B[i][j], B[ni][j]
        #         i = i + 1


def comb(k, s):
    if k == N:
        copied = copy.deepcopy(board)
        breakBrick(copied)
        return

    for idx in range(s, W):
        seq.append(idx)
        comb(k + 1, idx + 1)
        seq.pop()

for tc in range(1, int(input()) + 1):
    N, W, H = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(H)]
    MIN = W * H # 남은 벽돌
    # 조합
    seq = []
    comb(0, 0)
    print('#{} {}'.format(tc, MIN))