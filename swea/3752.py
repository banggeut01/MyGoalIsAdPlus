# 3752.py 가능한 시험 점수

for tc in range(1, int(input()) + 1):
    N = int(input())
    score = list(map(int, input().split()))
    ANS = {0}
    for s in score:
        tmp = set()
        for x in ANS:
            tmp.add(x + s)
        ANS = ANS.union(tmp)
    print('#{} {}'.format(tc, len(ANS)))