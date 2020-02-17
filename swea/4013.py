# 4013.py 특이한 자석
import sys
sys.stdin = open('4013input.txt', 'r')
import collections
def rotRight(n):
    board[n].appendleft(board[n].pop())

def rotLeft(n):
    board[n].append(board[n].popleft())


right = [0, 2, 3, 4, 0]
left = [0, 0, 1, 2, 3]
for tc in range(1, int(input()) + 1):
    board = [[0]]
    K = int(input())
    for _ in range(4):
        board.append(collections.deque(map(int, (input().split()))))
    # li = [list(map(int, input().split())) for _ in range(K)]

    for _ in range(K):
        n, d = map(int, input().split())
        visit = [False] * 5
        visit[n] = True
        seq = [(n, d)]
        rot = [(n, d)]
        while seq:
            # 오른쪽
            n, d = seq.pop(0)
            L, R = left[n], right[n]
            if R and not visit[R]:
                if board[n][2] != board[R][6]:
                    visit[R] = True
                    seq.append((R, d * (-1)))
                    rot.append((R, d * (-1)))
            # 왼쪽
            if L and not visit[L]:
                if board[n][6] != board[L][2]:
                    visit[L] = True
                    seq.append((L, d * (-1)))
                    rot.append((L, d * (-1)))
        for n, d in rot:
            if d == 1: # 오른쪽
                rotRight(n)
            else: # 왼쪽
                rotLeft(n)
    ANS = 0
    for idx in range(4):
        if board[idx + 1][0]:
            ANS += 2 ** idx

    print('#{} {}'.format(tc, ANS))