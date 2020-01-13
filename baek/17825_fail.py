# 17825_fail.py 주사위 윷놀이
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
            while n > 0:
                if score[new] == 40:
                    visit[score[tmp]] = False
                    horse[i] = -1
                    tmpList.append(i)
                    back(k + 1, total)
                    tmpList.pop()
                    horse[i] = tmp
                    visit[score[tmp]] = True
                    break
                else:
                    new += 1
                    n -= 1
            else:
                if new == 5:
                    new = 21
                elif new == 10:
                    new = 29
                elif new == 15:
                    new = 36
                # print(new)
                if not visit[score[new]]:
                    visit[score[tmp]], visit[score[new]] = False, True
                    horse[i] = new
                    tmpList.append(i)
                    back(k + 1, total + score[new])
                    tmpList.pop()
                    horse[i] = tmp
                    visit[score[tmp]], visit[score[new]] = True, False

score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
         20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
         40, 10, 13, 16, 19, 25, 30, 35, 40, 20,
         22, 24, 25, 30, 35, 40, 30, 28, 27, 26,
         25, 30, 35, 40]
# 출발이 40이면 ->
li = list(map(int, input().split()))
visit = [False] * 44 # 0 - 43
horse = [0] * 4
MAX = 0
tmpList = []
back(0, 0)
print(MAX)