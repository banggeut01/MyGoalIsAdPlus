# 17825.py 주사위 윷놀이

# visit : list 0 ~ 40
# horse : list 0~3 (말4개) 값은 현재 위치
def back(k, total):
    # global MAX
    # MAX = max(MAX, total)
    if k == 10:
        global MAX
        if MAX < total:
            print(tmpList)
        MAX = max(MAX, total)
        return

    for i in range(4): # i 번 말 움직이자
        if horse[i] != -1: # -1:도착
            n = li[k] # n 주사위
            new = tmp = horse[i]
            flag = False
            while n > 0:
                print(new)
                if score[new] == 40:
                    visit[tmp] = False
                    horse[i] = -1
                    tmpList.append(i)
                    back(k + 1, total)
                    tmpList.pop()
                    horse[i] = tmp
                    visit[tmp] = True
                    break
                else:
                    if not flag:
                        new = dct[new]
                        n -= 1
                        flag = True
                    else:
                        new += 1
                        n -= 1
            else:
                if not visit[new]:
                    print(score[new])
                    visit[tmp], visit[new] = False, True
                    horse[i] = new
                    tmpList.append(i)
                    back(k + 1, total + score[new])
                    tmpList.pop()
                    horse[i] = tmp
                    visit[tmp], visit[new] = True, False

score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
         20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
         40, 13, 16, 19, 25, 30, 35, 22, 24, 28,
         27, 26]
dct = {}
for i in range(31):
    dct[i] = i + 1
dct[5] = 21
dct[10] = 27
dct[15] = 29
dct[26] = 20
dct[28] = 24
dct[31] = 24
# 출발이 40이면 ->
li = list(map(int, input().split()))
visit = [False] * 32 # 0 - 31
horse = [0] * 4
MAX = 0
tmpList = []
back(0, 0)
print(MAX)