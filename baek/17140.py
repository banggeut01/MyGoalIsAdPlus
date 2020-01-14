# 17140.py 이차원 배열과 연산

def colCal():
    global RL
    maxRL = RL
    for j in range(CL):
        tmp = []
        for i in range(RL):
            if not A[i][j]: continue
            tmp.append(A[i][j])
        tmp = sorted(tmp)
        tupTmp = []
        prev, cnt = 0, 0
        # 세기
        for num in tmp:
            if prev != num:
                tupTmp.append((cnt, prev))
                cnt = 1
                prev = num
            else:
                cnt += 1
        tupTmp.append((cnt, prev))
        # 정렬
        tupTmp = sorted(tupTmp[1:])
        # 바꾸기
        newRL = len(tupTmp) * 2
        if newRL > 100: newRL = 100
        for i in range(0, newRL // 2):
            A[i * 2][j], A[i * 2 + 1][j] = tupTmp[i][1], tupTmp[i][0]
        for i in range(newRL // 2, RL):
            A[i * 2][j], A[i * 2 + 1][j] = 0, 0
        # RL 값 갱신
        maxRL = max(maxRL, newRL)
    RL = maxRL

def rowCal():
    global CL
    maxCL = CL
    for i in range(RL):
        tmp = []
        for j in range(CL):
            if not A[i][j]: continue
            tmp.append(A[i][j])
        tmp = sorted(tmp)
        tupTmp = []
        prev, cnt = 0, 0
        # 세기
        for num in tmp:
            if prev != num:
                tupTmp.append((cnt, prev))
                cnt = 1
                prev = num
            else:
                cnt += 1
        tupTmp.append((cnt, prev))
        # 정렬
        tupTmp = sorted(tupTmp[1:])
        # 바꾸기
        newCL = len(tupTmp) * 2
        if newCL > 100: newCL = 100
        for j in range(0, newCL // 2):
            A[i][j * 2], A[i][j * 2 + 1] = tupTmp[j][1], tupTmp[j][0]
        for j in range(newCL // 2, CL):
            A[i][j * 2], A[i][j * 2 + 1] = 0, 0
        # CL 값 갱신
        maxCL = max(maxCL, newCL)
    CL = maxCL

r, c, k = map(int, input().split())
A = [[0] * 100 for _ in range(100)]
for i in range(3):
    li = list(map(int, input().split()))
    for j in range(3):
        A[i][j] = li[j]
t = 0
RL, CL = 3, 3
while t <= 100:
    if A[r - 1][c - 1] == k:
        break
    t += 1
    if t > 100:
        t = -1
        break
    # print(A)
    if RL >= CL:
        rowCal()
    else:
        colCal()


print(t)