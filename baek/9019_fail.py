# 9019_fail.py
import collections
def solution(k, cmd, num):
    global MIN, ANS
    if MIN <= k:
        return

    cur = int(''.join(num))
    if cur == tobe:
        MIN = min(MIN, k)
        ANS = cmd
        return

    tmp = cur * 2 % 10000
    if not visit[tmp] or visit[tmp] > k + 1:
        tmp_deq = collections.deque(str(tmp))
        for _ in range(4 - len(tmp_deq)):
            tmp_deq.appendleft('0')
        visit[tmp] = k + 1
        solution(k + 1, cmd + 'D', tmp_deq)

    tmp = (cur + 9999) % 10000
    if not visit[tmp] or visit[tmp] > k + 1:
        tmp_deq = collections.deque(str(tmp))
        for _ in range(4 - len(tmp_deq)):
            tmp_deq.appendleft('0')
        visit[tmp] = k + 1
        solution(k + 1, cmd + 'S', tmp_deq)

    tmp_deq = num.append(num.popleft())
    tmp = int(''.join(tmp_deq))
    if not visit[tmp] or visit[tmp] > k + 1:
        visit[tmp] = k + 1
        solution(k + 1, cmd + 'L', tmp_deq)

    tmp_deq = num.appendleft(num.pop())
    tmp = int(''.join(tmp_deq))
    if not visit[tmp] or visit[tmp] > k + 1:
        visit[tmp] = k + 1
        solution(k + 1, cmd + 'R', tmp_deq)

N = int(input())
for _ in range(N):
    MIN, ANS = 0xffffff, ''
    visit = [0] * 10000
    li, tobe = map(int, input().split())
    num_list = collections.deque(str(li))
    solution(0, '', num_list)
    print(''.join(ANS))
