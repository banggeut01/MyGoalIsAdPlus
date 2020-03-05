# 5658_2.py 보물상자 비밀번호
def rotation(k):
    for idx in range(0, N, L):
        ANS.add(''.join(char[idx : idx + L]))
    if k == L: return
    char.append(char.pop(0))
    rotation(k + 1)

for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    L = N // 4
    char = list(input())
    ANS = set()
    rotation(0)
    ANS_list = []
    for hex_num in ANS:
        ANS_list.append(int(hex_num, 16))
    ANS_list = list(reversed(sorted(ANS_list)))
    print('#{} {}'.format(tc, ANS_list[K - 1]))