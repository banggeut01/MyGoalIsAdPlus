# ka2.py
import copy
opr = ['+', '-', '*']
priority = [] # '+', '-', '*'
visit = [False] * 3
ex = []
ANS = 0

def split_ex(expression):
    tmp = ''
    for e in expression:
        if e in opr:
            if tmp:
                ex.append(int(tmp))
            ex.append(e)
            tmp = ''
        else:
            tmp += e
    ex.append(int(tmp))

def get_priority(k):
    if k == 3:
        global ANS
        print(priority)
        e = copy.deepcopy(ex)
        for x in range(3):
            idx = 0
            while idx < len(e):
                if e[idx] == priority[x]:
                    a = e.pop(idx - 1)
                    o = e.pop(idx - 1)
                    b = e.pop(idx - 1)
                    if o == '+': tmp = a + b
                    elif o == '-': tmp = a - b
                    else: tmp = a * b
                    e.insert(idx - 1, tmp)
                else:
                    idx += 1
        ANS = max(ANS, abs(e[0]))
        print(e)
        return

    for i in range(3):
        if not visit[i]:
            visit[i] = True
            priority.append(opr[i])
            get_priority(k + 1)
            visit[i] = False
            priority.pop()

def solution(expression):
    answer = 0

    split_ex(expression)  # ex를 구함
    print(ex)
    get_priority(0)

    answer = ANS
    return answer

expression = "100-200*300-500+20"
# expression = "50*6-3*2"
print(solution(expression))