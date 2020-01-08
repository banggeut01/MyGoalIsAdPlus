# 17837.py 새로운 게임 2
def isEnd(r, c):
    if len(chess[r][c] == K): return True
    else: return False

N, K = map(int, input().split()) # 크기, 말개수
board = [list(map(int, input().split())) for _ in range(N)]
# 0흰, 1빨, 2파
# 내가가려고 하는 좌표가 무슨색인지? 어떤 말들이 있는지
# 현재 나의 좌표에 어떤 말이 있는지?
# 내가 가려고 하는 좌표 - > 현재 좌표 + 방향
# 배열 만들어서 말 리스트 넣기
# 말을 인덱스로 하는 좌표, [0, (1, 3), (2, 2)] 1번말은 1,3에 있다.
# 이동 후 그 좌표의 말 개수가 K이면 종료!

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
    for idx in range(K): # idx 현재말
        x, y, d = horse[idx]
        dx, dy = dir[d]
        nx, ny = x + dx, y + dy
        if -1 < nx < N and -1 < ny < N:
            if board[nx][ny] == 0: # 흰
                tmp = []
                for i in range(len(chess[x][y]) - 1, 0, -1):
                    num = chess[x][y][-1]
                    horse[num][0], horse[num][1] = nx, ny
                    tmp.append(chess[x][y].pop())
                    if i == idx: break
                while tmp:
                    chess[nx][ny].append(tmp.pop())
                chess[x][y] = []
            elif board[nx][ny] == 1: # 빨
                tmp = []
                for i in range(len(chess[x][y]) - 1, 0, -1):
                    num = chess[x][y][-1]
                    horse[num][0], horse[num][1], horse[num][2] = nx, ny, rev[horse[num][2]]
                    tmp.append(chess[x][y].pop())
                    if i == idx: break
                tmp = list(reversed(tmp))
                while tmp:
                    chess[nx][ny].append(tmp.pop())
                chess[x][y] = []
            else: # 파
                newD = rev[horse[idx][2]]
                dx, dy = dir[newD]
                nx, ny = x + dx, y + dy
                if -1 < nx < N and -1 < ny < N:
                    horse[idx][2] = newD # 방향 바꾸기
                    if board[nx][ny] != 2: # 이동
                        tmp = []
                        for i in range(len(chess[x][y]) - 1, 0, -1):
                            num = chess[x][y][-1]
                            horse[num][0], horse[num][1] = nx, ny
                            tmp.append(chess[x][y].pop())
                            if i == idx: break
                        while tmp:
                            chess[nx][ny].append(tmp.pop())
                else: # 경계선
                    horse[idx][2] = newD  # 방향 바꾸기
        else: # 파란색
            newD = rev[horse[idx][2]]
            dx, dy = dir[newD]
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N:
                horse[idx][2] = newD  # 방향 바꾸기
                if board[nx][ny] != 2:  # 이동
                    tmp = []
                    for i in range(len(chess[x][y]) - 1, 0, -1):
                        num = chess[x][y][-1]
                        horse[num][0], horse[num][1] = nx, ny
                        tmp.append(chess[x][y].pop())
                        if i == idx: break
                    while tmp:
                        chess[nx][ny].append(tmp.pop())
            else:  # 경계선
                horse[idx][2] = newD  # 방향 바꾸기
        # if len(좌표):
        #     turn = -1
        #     break
        # else: turn += 1
print(turn)