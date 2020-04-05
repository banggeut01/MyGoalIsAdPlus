#ex3.py

# road = 도로
# n = 보수 가능한 최대 횟수


def solution(road, n):
    answer = -1
    for i in range(len(road)):
        # avail: 보수가능횟수, cnt: 현재 길이, pos: 현재 위치
        avail, cnt, pos = n, 0, i
        if len(road) - i <= answer: break
        while pos < len(road):
            if road[pos] == '0':
                if avail > 0:
                    avail -= 1
                else:
                    break
            cnt += 1
            answer = max(answer, cnt)
            pos += 1
    return answer


# road, n = "111011110011111011111100011111"	, 3
# road, n = "001100", 5
road, n = '0' * 300000, 300000
print('\"' + road + '\"')


print(solution(road, n))