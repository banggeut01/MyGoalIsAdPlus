# e3.py
import copy
ANS = -1
def perm(cur, N, visit, seq, numbers, K):
    if cur == N:
        print(seq)
        global ANS
        cnt = 0
        copied = copy.deepcopy(seq)
        for idx in range(N):
            if copied[idx] != numbers[idx]:
                tmp = idx
                while copied[tmp] != numbers[idx]:
                    tmp += 1
                copied[tmp], copied[idx] = copied[idx], copied[tmp]
                cnt += 1
        if ANS == -1: ANS = cnt
        else: ANS = min(ANS, cnt)
        return

    for x in range(N):
        if not visit[x]:
            if cur == 0 or abs(seq[cur - 1] - numbers[x]) <= K:
                seq[cur] = numbers[x]
                visit[x] = True
                perm(cur + 1, N, visit, seq, numbers, K)
                visit[x] = False
    return

def solution(numbers, K):
    global ANS
    N = len(numbers)
    seq, visit = [0] * N, [False] * N
    perm(0, N, visit, seq, numbers, K)
    answer = ANS
    return answer

numbers, K = [10, 40, 30, 20], 20
# numbers, K = [3, 7, 2, 8, 6, 4, 5, 1], 3

print(solution(numbers, K))