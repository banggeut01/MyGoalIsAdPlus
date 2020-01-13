# 17140.py 이차원 배열과 연산

def rowCal():
    global RL
    for i in range(RL):
        pass

def colCal():
    global CL
    for i in range(RL):
        tmp = []
        for j in range(CL):
            if not A[i][j]: continue
            tmp.append(A[i][j])
        tmp = sorted(tmp)
        tupTmp =


r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]
t = 1
RL, CL = 3, 3
while t <= 100:
    if RL >= CL:
        rowCal()
    else:
        colCal()
    if A[r][c] == k:
        break
    if t == 100:
        t = -1
        break
print(t)