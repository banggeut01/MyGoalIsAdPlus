# ex2.py

def solution(answer_sheet, sheets):
    answer = -1
    for i in range(len(sheets) - 1):
        for j in range(i + 1, len(sheets)):
            max_cnt, cnt, total = 0, 0, 0
            for x in range(len(sheets[i])):
                if answer_sheet[x] != sheets[i][x] and sheets[i][x] == sheets[j][x]:
                    cnt += 1
                    max_cnt, total = max(max_cnt, cnt), total + 1
                else:
                    cnt = 0
            print('=====')
            print(i, j)
            print(total, max_cnt)
            answer = max(answer, total + max_cnt ** 2)
    return answer

answer_sheet, sheets = "4132315142",	["3241523133","4121314445","3243523133","4433325251","2412313253"]
# answer_sheet, sheets = "53241",	["53241", "42133", "53241", "14354"]
# answer_sheet, sheets = "24551",	["24553", "24553", "24553", "24553"]
print(solution(answer_sheet, sheets))