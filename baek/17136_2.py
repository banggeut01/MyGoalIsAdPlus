# 17136_2.py 색종이 붙이기 (옛 방법으로 다시 짜봄)
def isPossible(i, j, x):
    for r in range(i, i + x + 1):
        for c in range(j, j + x + 1):
            if not board[r][c]: return False
    return True

def updateBoard(i, j, x, val):
    for r in range(i, i + x + 1):
        for c in range(j, j + x + 1):
            board[r][c] = val

def paper(r, cnt, cur):
    global MIN
    if cnt == MIN:
        return

    if cur == 0:
        MIN = min(MIN, cnt)
        return

    # 한 자리에 색종이 1 ~ 5 크기를 두고 난 후, for문을 계속 돌리면 안된다.
    # 바로 return 시켜야함!
    flag = False
    for i in range(r, 10):
        for j in range(10):
            if board[i][j]:
                for x in range(4, -1, -1):
                    if NUM[x] and i + x < 10 and j + x < 10:
                        if isPossible(i, j, x):
                            updateBoard(i, j, x, 0)
                            NUM[x] -= 1
                            flag = True
                            paper(i, cnt + 1, cur - (x + 1) ** 2)
                            updateBoard(i, j, x, 1)
                            NUM[x] += 1
            if flag: return

board = [list(map(int, input().split())) for _ in range(10)]
MIN = 100
visit = [[False] * 10 for _ in range(10)]
NUM = [5, 5, 5, 5, 5]
oneCnt = 0
for i in range(10):
    for j in range(10):
        if board[i][j]: oneCnt += 1
paper(0, 0, oneCnt)
if MIN == 100: MIN = -1
print(MIN)