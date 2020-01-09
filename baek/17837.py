# 17837.py 새로운 게임 2
import pprint
def isEnd(r, c):
    if len(chess[r][c]) >= 4: return True
    else: return False

N, K = map(int, input().split()) # 크기, 말개수
board = [list(map(int, input().split())) for _ in range(N)]
dir = [0, (0, 1), (0, -1), (-1, 0), (1, 0)] # 1우,2좌,3상,4하
rev = {1:2, 2:1, 3:4, 4:3} # 반대
chess  = [[[] for _ in range(N)] for _ in range(N)]
horse = []
for idx in range(K):
    x, y, d = map(int, input().split()) # 행, 열, 방향
    x, y = x - 1, y - 1
    horse.append([x, y, d])
    chess[x][y].append(idx)
turn = 1
while turn <= 1000:
    # pprint.pprint(chess)
    # print(horse)
    # print('======================')
    flag = False
    for idx in range(K): # idx 현재말
        x, y, d = horse[idx]
        dx, dy = dir[d]
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N:
            if board[nx][ny] == 0: # 흰
                tmp = []
                for i in range(len(chess[x][y]) - 1, -1, -1):
                    num = chess[x][y][-1]
                    horse[num][0], horse[num][1] = nx, ny
                    tmp.append(chess[x][y].pop())
                    if num == idx: break
                while tmp:
                    chess[nx][ny].append(tmp.pop())
                if isEnd(nx, ny):
                    flag = True
                    break
            elif board[nx][ny] == 1: # 빨
                tmp = []
                for i in range(len(chess[x][y]) - 1, -1, -1):
                    num = chess[x][y][-1]
                    horse[num][0], horse[num][1] = nx, ny
                    tmp.append(chess[x][y].pop())
                    if num == idx: break
                tmp = list(reversed(tmp))
                while tmp:
                    chess[nx][ny].append(tmp.pop())
                if isEnd(nx, ny):
                    flag = True
                    break
            else: # 파
                newD = rev[horse[idx][2]]
                dx, dy = dir[newD]
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < N:
                    if board[nx][ny] == 0: # 흰
                        horse[idx][2] = newD # 방향 바꾸기
                        tmp = []
                        for i in range(len(chess[x][y]) - 1, -1, -1):
                            num = chess[x][y][-1]
                            horse[num][0], horse[num][1] = nx, ny
                            tmp.append(chess[x][y].pop())
                            if num == idx: break
                        while tmp:
                            chess[nx][ny].append(tmp.pop())
                        if isEnd(nx, ny):
                            flag = True
                            break
                    elif board[nx][ny] == 1: # 빨
                        horse[idx][2] = newD  # 방향 바꾸기
                        tmp = []
                        for i in range(len(chess[x][y]) - 1, -1, -1):
                            num = chess[x][y][-1]
                            horse[num][0], horse[num][1] = nx, ny
                            tmp.append(chess[x][y].pop())
                            if num == idx: break
                        tmp = list(reversed(tmp))
                        while tmp:
                            chess[nx][ny].append(tmp.pop())
                        if isEnd(nx, ny):
                            flag = True
                            break
                    else: # 파
                        horse[idx][2] = newD  # 방향 바꾸기
                else: # 경계선 or 흰, 빨
                    horse[idx][2] = newD  # 방향 바꾸기
        else: # 파란색
            newD = rev[horse[idx][2]]
            dx, dy = dir[newD]
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N:
                if board[nx][ny] == 0:  # 흰
                    horse[idx][2] = newD  # 방향 바꾸기
                    tmp = []
                    for i in range(len(chess[x][y]) - 1, -1, -1):
                        num = chess[x][y][-1]
                        horse[num][0], horse[num][1] = nx, ny
                        tmp.append(chess[x][y].pop())
                        if num == idx: break
                    while tmp:
                        chess[nx][ny].append(tmp.pop())
                    if isEnd(nx, ny):
                        flag = True
                        break
                elif board[nx][ny] == 1:  # 빨
                    horse[idx][2] = newD  # 방향 바꾸기
                    tmp = []
                    for i in range(len(chess[x][y]) - 1, -1, -1):
                        num = chess[x][y][-1]
                        horse[num][0], horse[num][1] = nx, ny
                        tmp.append(chess[x][y].pop())
                        if num == idx: break
                    tmp = list(reversed(tmp))
                    while tmp:
                        chess[nx][ny].append(tmp.pop())
                    if isEnd(nx, ny):
                        flag = True
                        break
                else:  # 파
                    horse[idx][2] = newD  # 방향 바꾸기
            else:  # 경계선 or 흰, 빨
                horse[idx][2] = newD  # 방향 바꾸기
    if flag: break
    else: turn += 1
if turn > 1000: turn = -1
print(turn)