# 17140.py 이차원 배열과 연산
# R : 행 정렬 / 행개수 >= 열개수
# C : 열 정렬 / 행개수 < 열개수
import copy
def R():
    MAX = 0
    for i in range(len(board)):
        tmp = []
        board[i] = sorted(board[i])
        prev, cnt, j = 0, 0, 0
        while not board[i][j]:
            j += 1
        while j < len(board[i]):
            if board[i][j] != prev:
                if prev != 0:
                    tmp.append((cnt, prev))
                prev, cnt = board[i][j], 1
            else:
                cnt += 1
            j += 1
        tmp.append((cnt, prev))
        tmp = sorted(tmp)
        board[i] = []
        for cnt, num in tmp:
            board[i].append(num)
            board[i].append(cnt)
        MAX = max(MAX, len(board[i]))
    for i in range(len(board)):
        for _ in range(MAX - len(board[i])):
            board[i].append(0)

def transfer():
    tmp = [[0] * len(board) for _ in range(len(board[0]))]
    for i in range(len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j] = board[j][i]
    return copy.deepcopy(tmp)

def solution():
    global board
    if r < len(board) and c < len(board[0]) and board[r][c] == k:
        return 0

    time = 0
    while time < 100:
        if len(board) >= len(board[0]):
            R()
        else:
            # 행 <-> 열
            board = transfer()
            R()
            # 행 <-> 열
            board = transfer()
        time += 1
        if r < len(board) and c < len(board[0]) and board[r][c] == k:
            return time
    return -1

r, c, k = map(int, input().split())
r, c = r - 1, c - 1
board = [list(map(int, input().split())) for _ in range(3)]
print(solution())
