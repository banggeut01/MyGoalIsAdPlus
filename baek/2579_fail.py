# 2579_fail.py 계단 오르기

def step(k, total, cnt): # cnt: 연속 한칸씩오른 횟수
    # 한칸
    if k + 1 <= N and cnt < 2:
        if memo[k + 1] < total + score[k + 1]:
            memo[k + 1] = total + score[k + 1]
            step(k + 1, memo[k + 1], cnt + 1)
    # 두칸
    if k + 2 <= N:
        if memo[k + 2] < total + score[k + 2]:
            memo[k + 2] = total + score[k + 2]
            step(k + 2, memo[k + 2], 1)
score = [0]
N = int(input())
for _ in range(N):
    score.append(int(input()))
memo = [[0, 0] for _ in range(N + 1)]
step(0, 0, 0)
print(memo[-1])