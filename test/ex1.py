# ex1.py

def solution(inputString):
    answer = -1
    open_exp, close_exp = ['(', '{', '[', '<'], [')', '}', ']', '>']
    garo, cnt = 0, 0
    for char in inputString:
        if char in open_exp:
            garo += 1
            cnt += 1
        elif char in close_exp:
            if garo > 0:
                garo -= 1
            else: return answer
    if garo == 0:
        answer = cnt
    return answer