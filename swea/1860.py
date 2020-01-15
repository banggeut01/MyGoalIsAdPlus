# 1860.py 진기의 최고급 붕어빵

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split()) # N:사람수, M초에 K개
    li = list(map(int, input().split())) # N명 도착시간 초단위
    li = sorted(li)
    T, cnt, idx = 0, 0, 0
    result = 'Possible'
    while idx < N:
        if T + M < li[idx]:
            T += M
            cnt += K
        elif T + M > li[idx]:
            cnt -= 1
            idx += 1
        else:
            T += M
            cnt += K
            cnt -= 1
            idx += 1
        if cnt < 0:
            result = 'Impossible'
            break
    print('#{} {}'.format(tc, result))