# ka3_1.py

def solution(gems):
    uniqe_gems = set(gems)
    N = len(uniqe_gems)
    answer = []
    min_len = 100001
    start, end = 0, 0
    for idx in range(len(gems) - N + 1):
        tmp = set()
        for x in range(idx, len(gems)):
            tmp.add(gems[x])
            if min_len <= x - idx + 1:
                break
            if len(tmp) == N:
                if start == 0 or end - start > x - idx:
                    min_len = x - idx + 1
                    start = idx + 1
                    end = x + 1
                break
    answer = [start, end]
    return answer

# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
print(solution(gems))