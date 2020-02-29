# 5653.py 줄기세포 배양
import collections
import sys
sys.stdin = open('5653input.txt', 'r')
def duplicate():
    T = 0
    while T < K and queue:
        tmp = dict()
        for key, val in queue.items():
            x, y = key
            l, s, e = val  # l:수명, s:활성화시간, e:죽는시간
            if e > T and s <= T:  # 번식
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nx, ny = x + dx, y + dy
                    if not queue.get((nx, ny)):
                        if tmp.get((nx, ny)):
                            originL, t1, t2 = tmp[(nx, ny)]
                            if originL < l: tmp[(nx, ny)] = (l, T + 1 + l, T + 1 + l * 2)
                        else:
                            tmp[(nx, ny)] = (l, T + 1 + l, T + 1 + l * 2)
        # tmp --> queue에 추가
        for key, val in tmp.items():
            queue[key] = val
        T += 1
    cnt = 0
    for key, val in queue.items():
        l, s, e = val
        if e > T: cnt += 1
    return cnt


for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    queue = dict()
    for i in range(N):
        li = list(map(int, input().split()))
        for j in range(len(li)):
            if li[j]: queue[(i, j)] = (li[j], li[j], li[j] * 2)
    print('#{} {}'.format(tc, duplicate()))