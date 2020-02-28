# 5653.py 줄기세포 배양
import collections
import sys
# sys.stdin = open('5653input.txt', 'r')
def duplicate():
    T = 0
    # die = dict()
    while T < K and queue:
        tmp = dict()
        for key, val in queue.items():
            x, y = key
            l, s, e = val # l:수명, s:활성화시간, e:죽는시간
            # if e == T: # 죽음
            #     die[(x, y)] = True
            if e > T + 1 and s <= T + 1: # 번식
            # elif s <= T:
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nx, ny = x + dx, y + dy
                    if not queue.get((nx, ny)):
                        if tmp.get((nx, ny)):
                             originL, t1, t2 = tmp[(nx, ny)]
                             if originL < l: tmp[(nx, ny)] = (l, T + 1 + l, T + 1 + l * 2)
                        else:
                            tmp[(nx, ny)] = (l, T + 1 + l, T + 1 + l * 2)
        # # die --> queue에서 삭제
        # for key in die:
        #     if queue.get(key):
        #         queue.pop(key)
        # tmp --> queue에 추가
        for key, val in tmp.items():
            queue[key] = val
        print('{} {} {}'.format(T + 1, len(queue), queue))
        T += 1
    print(queue)
    return len(queue)

for tc in range(1, int(input()) + 1):
    N, M, K = map(int, input().split())
    # dq = collections.deque()
    queue = dict()
    for i in range(N):
        li = list(map(int, input().split()))
        for j in range(len(li)):
            # if li[j]: dq.append((i, j, 0, li[j], li[j] + li[j]))
            if li[j]: queue[(i, j)] = (li[j], li[j], li[j] * 2)
    print(queue)
    print('#{} {}'.format(tc, duplicate()))
