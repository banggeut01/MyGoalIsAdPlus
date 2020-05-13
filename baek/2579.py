# 2579.py 계단 오르기
def step(k, cnt): # cnt: 연속 한칸 내려갈 수 있는 횟수
    if k == 0:
        return 0

    # 한칸
    MAX = 0
    if k - 1 >= 0 and cnt:
        if not memo[k - 1][0]: memo[k - 1][0] = step(k - 1, 0)
        MAX = max(MAX, memo[k - 1][0])
    if k - 2 >= 0:
        if not memo[k - 2][1]: memo[k - 2][1] = step(k - 2, 1)
        MAX = max(MAX, memo[k - 2][1])
    memo[k][cnt] = MAX + score[k]
    return memo[k][cnt]

score = [0]
N = int(input())
for _ in range(N):
    score.append(int(input()))
memo = [[0] * 2 for _ in range(N + 1)]
print(step(N, 1))
# print(memo)
# print(memo[-1])