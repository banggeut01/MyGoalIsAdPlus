# 4131.py 활주로 건설

for tc in range(1, int(input()) + 1):
    N, X = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    # 열
    visit = [[False] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            