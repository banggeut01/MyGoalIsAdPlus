# 17825.py 주사위 윷놀이
def back(k, total):
    global MAX
    if k == 10:
        MAX = max(MAX, total)
        return

    flag = False
    for i in range(4): # i 번 말 움직이자
        if horse[i] != -1: # -1:도착
            n = li[k] # n 주사위
            new = origin = horse[i]
            while n > 0:
                new = next[new]
                n -= 1
            if new in blue:
                new = blue[new]
            if new > 38: # 도착
                horse[i] = -1
                visit[origin], visit[new] = False, True
                flag = True
                back(k + 1, total + score[new])
                horse[i] = origin
                visit[origin], visit[new] = True, False
            elif not visit[new]:
                horse[i] = new
                visit[origin], visit[new] = False, True
                flag = True
                back(k + 1, total + score[new])
                horse[i] = origin
                visit[origin], visit[new] = True, False
    if not flag:
        MAX = max(MAX, total)

score = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18,
         20, 22, 24, 26, 28, 30, 32, 34, 36, 38,
         40, 10, 13, 16, 19, 25, 20, 22, 24, 25,
         30, 28, 27, 26, 25, 25, 30, 35, 40, 0,
         0, 0, 0, 0]

next = {}
for i in range(len(score)):
    next[i] = i + 1
next[19] = 38 # 38 -> 40
next[24] = 35 # 19 -> 25
next[28] = 35 # 24 -> 25
next[33] = 35 # 26 -> 25
blue = dict()
blue[5] = 21 # 10 -> 10
blue[10] = 26 # 20 -> 20
blue[15] = 30 # 30 -> 30
li = list(map(int, input().split()))
visit = [False] * len(score)
horse = [0] * 4 # 도착이면 -1
MAX = 0
back(0, 0)
print(MAX)