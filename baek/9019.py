# 9019.py DSLR
import collections
def D(num):
    return num * 2 % 10000

def S(num):
    if not num: return 9999;
    return num - 1

def L(num):
    n3, num = num % 10, num // 10
    n2, num = num % 10, num // 10
    n1, num = num % 10, num // 10
    n4 = num
    return n1 * 1000 + n2 * 100 + n3 * 10 + n4

def R(num):
    n1, num = num % 10, num // 10
    n4, num = num % 10, num // 10
    n3, num = num % 10, num // 10
    n2 = num
    return n1 * 1000 + n2 * 100 + n3 * 10 + n4

def bfs(num, tobe):
    visit = [False] * 10000
    dq = collections.deque()
    dq.append((num, ''))
    while dq:
        cur, cmd = dq.popleft()

        tmp = D(cur)
        if not visit[tmp]:
            if tmp == tobe: return cmd + 'D'
            visit[tmp] = True
            dq.append((tmp, cmd + 'D'))

        tmp = S(cur)
        if not visit[tmp]:
            if tmp == tobe: return cmd + 'S'
            visit[tmp] = True
            dq.append((tmp, cmd + 'S'))

        tmp = L(cur)
        if not visit[tmp]:
            if tmp == tobe: return cmd + 'L'
            visit[tmp] = True
            dq.append((tmp, cmd + 'L'))

        tmp = R(cur)
        if not visit[tmp]:
            if tmp == tobe: return cmd + 'R'
            visit[tmp] = True
            dq.append((tmp, cmd + 'R'))

N = int(input())
for _ in range(N):
    li, tobe = map(int, input().split())
    ANS = bfs(li, tobe)
    print(ANS)
