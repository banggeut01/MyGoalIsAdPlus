# 5658.py 보물상자 비밀번호
import collections
def rotation():
    l = N // 4 # 비밀번호길이
    for i in range(l):
        # 리스트 넣기
        for s in range(0, N, l):
            ANS.append(list(seq)[s:s + l])
        if i == l - 1:
            break
        # 회전
        seq.appendleft(seq.pop())

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split()) # N:길이, K:번째
    seq = collections.deque(input())
    ANS = []
    rotation()
    for idx in range(len(ANS)):
        ANS[idx] = int('0x' + ''.join(ANS[idx]), 16)
    ANS = list(reversed(sorted(list(set(ANS)))))
    print('#{} {}'.format(tc, ANS[K - 1]))
