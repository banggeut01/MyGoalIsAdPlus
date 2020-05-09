# 징검다리 건너기 64062.py

def solution(stones, k):
    answer = 0
    maxX = max(stones)
    for _ in range(maxX):
        flag = False
        i = 0
        tmp = [0] * len(stones)
        while i < len(stones):
            origin = i
            if i + 1 < len(stones) and not stones[i + 1]:
                cnt = 1
                i = i + 1
                while i < len(stones):
                    if not stones[i]:
                        cnt += 1
                    else:
                        if cnt > k:
                            flag = True
                        break
                    i += 1
                    # if not stones[i] and cnt + 1 <= k:
                    #     cnt += 1
                    #     i += 1
                    # else:
                    #     cnt += 1
                    #     if cnt > k:
                    #         flag = True
                    #         break
            else:
                i += 1

            tmp[origin] += 1
            if flag:
                break
        if not flag:
            answer += 1
            for i in range(len(stones)):
                stones[i] -= tmp[i]
    return answer

stones, k = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
print(solution(stones, k))