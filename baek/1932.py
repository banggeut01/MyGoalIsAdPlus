# 정수 삼각형 1932.py
N = int(input())
val = []
for _ in range(N):
    li = list(map(int, input().split()))
    for x in li:
        val.append(x)

memo = [-1] * len(val)
num = len(val) - 1
for i in range(N, -1, -1): # 5, 4, 3, 2, 1
    if i == N:
        for j in range(i): # 0, 1, 2, 3, 4
            memo[num - j] = val[num - j]
    for j in range(i): # 5(0~4)
        left_up = num - i
        right_up = num - i + 1
        if j == 0:
            memo[left_up] = max(memo[left_up], memo[num] + val[left_up])
        elif j == i - 1:
            memo[right_up] = max(memo[right_up], memo[num] + val[right_up])
        else:
            memo[left_up] = max(memo[left_up], memo[num] + val[left_up])
            memo[right_up] = max(memo[right_up], memo[num] + val[right_up])
        num -= 1
    # val[i] == (13, 4) or (14, 4)
# print(memo)
print(memo[0])