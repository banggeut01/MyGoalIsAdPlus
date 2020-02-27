# 17136.py 색종이 붙이기
def isPossible(i, j, x):
    for r in range(i, i + x + 1):
        for c in range(j, j + x + 1):
            if not board[r][c]: return False
    return True

def updateBoard(i, j, x, val):
    for r in range(i, i + x + 1):
        for c in range(j, j + x + 1):
            board[r][c] = val

def paper(i, j, cnt, cur):
    global MIN
    if cnt == MIN:
        return

    if cur == 0:
        MIN = min(MIN, cnt)
        return

    if i == 10 and j == 0:
        return

    if not board[i][j]:
        if j == 9:
            paper(i + 1, 0, cnt, cur)
        else:
            paper(i, j + 1, cnt, cur)
    else:
        for x in range(4, -1, -1):
            if NUM[x] and i + x < 10 and j + x < 10:
                if isPossible(i, j, x):
                    updateBoard(i, j, x, 0)
                    NUM[x] -= 1
                    if j + x == 9:
                        paper(i + 1, 0, cnt + 1, cur - (x + 1) ** 2)
                    else:
                        paper(i, j + x, cnt + 1, cur - (x + 1) ** 2)
                    updateBoard(i, j, x, 1)
                    NUM[x] += 1

board = [list(map(int, input().split())) for _ in range(10)]
MIN = 100
visit = [[False] * 10 for _ in range(10)]
NUM = [5, 5, 5, 5, 5]
oneCnt = 0
for i in range(10):
    for j in range(10):
        if board[i][j]: oneCnt += 1
paper(0, 0, 0, oneCnt)
if MIN == 100: MIN = -1
print(MIN)