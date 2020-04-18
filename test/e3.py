# e3.py
import copy
ANS = -1
def perm(cur, N, visit, seq, numbers):
    if cur == N:
        global ANS
        cnt = 0
        copied = copy.deepcopy(seq)
        copied = [4, 7, 5, 8, 6, 3, 2, 1]
        for idx in range(N):
            if copied[idx] != numbers[idx]:
                tmp = idx
                while copied[tmp] != numbers[idx]:
                    tmp += 1
                cnt += tmp - idx
                while tmp != idx:
                    copied[tmp], copied[tmp - 1] = copied[tmp - 1], copied[tmp]
                    tmp -= 1
        if ANS == -1: ANS = cnt
        else: min(ANS, cnt)
        return

    for x in range(N):
        if not visit[x]:
            if cur == 0 or abs(seq[cur - 1] - numbers[x]) <= k:
                seq[cur] = numbers[x]
                visit[x] = True
                ret = perm(cur + 1, N, visit, seq, numbers)
                visit[x] = False
    return -1

def solution(numbers, K):
    global ANS
    N = len(numbers)
    seq, visit = [0] * N, [False] * N
    perm(0, N, visit, seq, numbers)
    answer = ANS
    return answer

# numbers, k = [10, 40, 30, 20], 20
numbers, k = [3, 7, 2, 8, 6, 4, 5, 1], 3

print(solution(numbers, k))