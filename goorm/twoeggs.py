# twoeggs.py


def solution(k, s, e, hp):
    for target in range(s, e - 1):
        underS, underE = s, target - 1
        upS, upE = target + 1, e
        if hp == 2:
            # 깨진 경우
            if underE - underS >= 2:
                solution(k + 1, underS, underE, hp - 1)
            # 안깨진 경우
            if upE - upS >= 2:
                solution(k + 1, upS, upE, hp)
        if hp == 1:

N = int(input())
ANS = N
solution(0, 1, N, 2)