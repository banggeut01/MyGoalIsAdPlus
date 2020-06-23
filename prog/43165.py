# 43165 타겟 넘버
ANS = 0
def solution(numbers, target):
    def dfs(k, total):
        global ANS
        if k == len(numbers):
            if total == target:
                ANS += 1
            return

        dfs(k + 1, total + numbers[k])
        dfs(k + 1, total - numbers[k])

    dfs(0, 0)
    answer = ANS
    return answer

numbers, target = [1, 1, 1, 1, 1],	3
print(solution(numbers, target))