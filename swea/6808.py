# 6808.py 규영이와 인영이의 카드게임

def perm(n, ksum, ysum):
    if n == 9:
        global W, L
        if ksum > ysum: W += 1
        elif ksum < ysum: L += 1
        return

    for i in range(9):
        if not visit[i]:
            visit[i] = True
            if K[n] > Y[i]: perm(n + 1, ksum + K[n] + Y[i], ysum)
            else: perm(n + 1, ksum, ysum + K[n] + Y[i])
            visit[i] = False

for tc in range(1, int(input()) + 1):
    K = list(map(int, input().split())) # 규영
    Y = list(set([x for x in range(1, 19)]) - set(K)) # 인영
    W, L = 0, 0
    visit = [False] * 9
    perm(0, 0, 0)
    print('#{} {} {}'.format(tc, W, L))