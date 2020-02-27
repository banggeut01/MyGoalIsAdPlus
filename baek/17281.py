# 17281.py 야구공
def updateMax():
    global MAX
    score = 0
    idx = 0
    for turn in range(N):
        plist = inning[turn] # 타수
        out = 0
        base = []
        while out < 3:
            tmp = plist[player[idx]] # plist[idx]: 타자번호, tmp: 타수
            if tmp:
                base.append(1)
                for _ in range(tmp - 1):
                    base.append(0)
                score += sum(base[-3 - tmp : -3])
            else:
                out += 1
            idx = (idx + 1) % 9
    MAX = max(MAX, score)

def perm(k):
    if k == 9:
        updateMax()
        return

    if k == 3:
        perm(k + 1)
    else:
        for idx in range(9):
            if not visit[idx]:
                visit[idx] = True
                player[k] = idx
                perm(k + 1)
                visit[idx] = False

N = int(input())
player = [-1] * 9
player[3] = 0
MAX = 0
visit = [False] * 9 # 0~8
visit[0] = True
inning = []
for _ in range(N):
    inning.append(list(map(int, input().split())))
perm(0)
print(MAX)
