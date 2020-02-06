# 2529.py 부등호
def isPossible():
    prev = num[0]
    for x in range(1, N):
        if li[x - 1] == "<":
            if prev >= num[x]:
                return False
        else:
            if prev <= num[x]:
                return False
        prev = num[x]
    return True

def perm(k):
    if k == N:
        if isPossible():
            tmp = int(''.join(list(map(str, num))))
            global MIN, MAX, MINANS, MAXANS
            if MIN > tmp:
                MIN = min(MIN, tmp)
                MINANS = ''.join(list(map(str, num)))
            if MAX < tmp:
                MAX = max(MAX, tmp)
                MAXANS = ''.join(list(map(str, num)))
        return

    for i in range(10):
        if not visit[i]:
            visit[i] = 1
            num[k] = i
            perm(k + 1)
            visit[i] = 0

N = int(input()) + 1
li = list(input().split())
MAX, MIN = 0, 9999999999
visit = [0] * 10
num = [0] * N
MAXANS, MINANS = '', ''
perm(0)
print(MAXANS)
print(MINANS)