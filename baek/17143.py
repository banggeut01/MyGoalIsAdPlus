# 17143.py 낚시왕
import pprint
R, C, M = map(int, input().split())
board = [[0] * C for _ in range(R)]
dir = [0, (-1, 0), (1, 0), (0, 1), (0, -1)]
rev = {1: 2, 2: 1, 3: 4, 4: 3}
shark = dict()
die = [False] * (M + 1)
for idx in range(1, M + 1):
    r, c, s, d, z = map(int, input().split()) 
    r, c = r - 1, c - 1
    board[r][c] = idx
    shark[idx] = [r, c, s, d, z] # 행, 열, 속력, 방향, 크기

result = 0
for j in range(C):
    # 사냥
    for i in range(R):
        if board[i][j]:
            idx = board[i][j]
            r, c, s, d, z = shark[idx]
            result += z
            # print(shark)
            # print('{} 더하기'.format(s))
            die[idx] = True
            # print('사냥하기 {}번상어'.format(idx))
            break
    # 이동
    # board 초기화
    for r, c, s, d, z in shark.values():
        board[r][c] = 0
    for idx in shark.keys():
        if die[idx]: continue
        r, c, s, d, z = shark[idx]
        news = s
        dr, dc = dir[d]
        while news > 0:
            if -1 < r + dr < R and -1 < c + dc < C:
                r, c = r + dr, c + dc
            else:
                d = rev[d]
                dr, dc = dir[d]
                r, c = r + dr, c + dc
            news -= 1
        if board[r][c]:
            ori = board[r][c]
            if shark[ori][4] < z:
                board[r][c] = idx
                shark[idx][0], shark[idx][1], shark[idx][3] = r, c, d
                die[ori] = True
                # print('잡아먹기 {}가 {}번상어'.format(idx, ori))
            else:
                die[idx] = True
                # print('잡아먹기 {}가 {}번상어'.format(ori, idx))
        else:
            board[r][c] = idx
            shark[idx][0], shark[idx][1], shark[idx][3] = r, c, d
    # board 세팅
    # for idx in shark.keys():
    #     if die[idx]: continue
    #     board[shark[idx][0]][shark[idx][1]] = idx
    # pprint.pprint(board)
print(result)


