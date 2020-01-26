# 2105_2.py 디저트 카페 - 2)다른 방법
import sys
sys.stdin = open('2105input.txt', 'r')
dir = [(-1, 1), (1, 1), (1, -1), (-1, -1)]
for tc in range(1, int(input()) + 1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    visit = [False] * 101
    MAX = -1

    for i in range(1, N):
        for j in range(N - 2):
            back(i, j, -1, 0, 0, 0) # x, y, d, total, up, down
    print('#{} {}'.format(tc, MAX))