def edit(p, o):
    stack = []
    ret = ""
    for idx in range(len(p)):
        if p[idx] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                ret += ')'
            else:
                stack.append('(')
                o -= 1
                ret += '('
        else:
            if o > 0:
                stack.append('(')
                o -= 1
                ret += '('
            else:
                stack.pop()
                ret += ')'
    return ret


def solution(p):
    answer = ''
    if not p: return answer
    o, c = 0, 0  # (, ) 갯수
    s, e = 0, 0  # start, end index
    while e < len(p):
        if p[e] == '(':
            o += 1
        else:
            c += 1
        if o == c:  # 균형
            answer += edit(p[s: e + 1], o)
            s = e + 1
            o, c = 0, 0
        e += 1


    return answer

p = "()))((()"
print(solution(p))