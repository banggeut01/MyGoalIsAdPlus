# 17779.py 게리맨더링 2

def getAns(x, y, d1, d2):
    global total
    sum1, sum2, sum3, sum4, sum5 = 0, 0, 0, 0, 0
    for i in range(x):
        for j in range(y + 1):
            sum1 += board[i][j]
    tmp = 0
    for i in range(x, x + d1):
        for j in range(y - tmp):
            sum1 += board[i][j]
        tmp += 1

    for i in range(x):
        for j in range(y + 1, N):
            sum2 += board[i][j]

    tmp = 0
    for i in range(x, x + d2 + 1):
        for j in range(y + 1 + tmp, N):
            sum2 += board[i][j]
        tmp += 1

    for i in range(N - 1, x + d1 + d2, -1):
        for j in range(y - d1 + d2):
            sum3 += board[i][j]
        for j in range(y - d1 + d2, N):
            sum4 += board[i][j]

    tmp = 0
    for i in range(x + d1, x + d1 + d2 + 1):
        for j in range(y - d1 + tmp):
            sum3 += board[i][j]
        tmp += 1

    tmp = 1
    for i in range(x + d1 + d2, x + d2, -1):
        for j in range(y - d1 + d2 + tmp, N):
            sum4 += board[i][j]
        tmp += 1
    sum5 = total - (sum1 + sum2 + sum3 + sum4)
    return max(sum1, sum2, sum3, sum4, sum5) - min(sum1, sum2, sum3, sum4, sum5)

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
ANS = 0xffffff
total = 0
for x in range(N):
    for y in range(N):
        total += board[x][y]

for x in range(0, N - 2):
    for y in range(1, N - 1):
        for d1 in range(1, N - 1):
            for d2 in range(1, N - 1):
                if x + d1 + d2 < N and -1 < y - d1 and y + d2 < N:
                    ANS = min(ANS, getAns(x, y, d1, d2))

print(ANS)