# 1038.py 감소하는 수

def comp(k, prev):
    global selected
    for idx in range(10):
        if idx < prev and not visit[idx]:
            visit[idx] = True
            selected.append(str(idx))
            ansList.append(int(''.join(list(map(str, selected)))))
            comp(k + 1, idx)
            visit[idx] = False
            selected.pop()

visit = [False] * 10
selected = []
ansList = []
N = int(input())
ANS = -1
comp(0, 10)
ansList = sorted(ansList)
if len(ansList) > N:
    ANS = ansList[N]
print(ANS)