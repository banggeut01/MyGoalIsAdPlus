# ka_2.py
cal_list = [['*', '+', '-'], ['*', '-', '+'], ['+', '*', '+'], ['+', '-', '*'],
            ['-', '*', '+'], ['-', '+', '*']]


def solution(expression):
    answer = 0
    number = ''
    numlist = []
    operator = []
    for exp in expression:
        if exp in "-+*":
            numlist.append(int(number))
            number = ''
            operator.append(exp)
        else:
            number += exp
    numlist.append(int(number))
    for cal in cal_list:
        cal_nums = [num for num in numlist]
        cal_oper = [oper for oper in operator]
        for c in cal:
            cnt = 0
            for i in range(len(cal_oper)):
                if cal_oper[i - cnt] == c:
                    cal_oper.pop(i - cnt)
                    a = cal_nums.pop(i - cnt)
                    b = cal_nums.pop(i - cnt)
                    if c == '+':
                        a += b
                    elif c == '-':
                        a -= b
                    else:
                        a *= b
                    cal_nums.insert(i - cnt, a)
                    cnt += 1
        if abs(cal_nums[0]) > answer:
            answer = abs(cal_nums[0])

    return answer

expression = "100-200*300-500+20"
# expression = "50*6-3*2"
print(solution(expression))