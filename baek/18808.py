# 스티커 붙이기 18808.py
import copy
def isPossible(i, j):
    for x in range(H):
        for y in range(W):
            if board[x + i][y + j] and smap[x][y]:
                return False
    return True

def check(i, j):
    for x in range(H):
        for y in range(W):
            if smap[x][y]:
                board[x + i][y + j] = 1

def rotation():
    global H, W, smap
    H, W = W, H
    copied = copy.deepcopy(smap)
    smap = [[0] * W for _ in range(H)]
    for i in range(W): # 행
        for j in range(H): # 열
            smap[j][W - i - 1] = copied[i][j]

def solution(cnt):
    for i in range(N):
        for j in range(M):
            if i + H - 1 < N and j + W - 1 < M:
                if isPossible(i, j):
                    check(i, j)
                    return
    if cnt == 3: return
    rotation()
    solution(cnt + 1)


N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
for _ in range(K):
    H, W = map(int, input().split())
    smap = [list(map(int, input().split())) for _ in range(H)]
    solution(0)
ANS = 0
for i in range(N):
    for j in range(M):
        if board[i][j]:
            ANS += 1
print(ANS)
# print(board)