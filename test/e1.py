# e1.py
def solution(p, s):
    p, s = list(map(int, list(p))), list(map(int, list(s)))
    answer = 0
    for x in range(len(p)):
        if p[x] == s[x]: continue
        big, small = max(p[x], s[x]), min(p[x], s[x])
        answer += min(big - small, (small + 10) - big)
    return answer

# str1, str2 = "82195",	"64723"
str1, str2 = "00000000000000000000", "91919191919191919191"

print(solution(str1, str2))