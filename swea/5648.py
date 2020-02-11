# 5648.py 원자 소멸 시뮬레이션
# 초기 보드 0
# 이동하는데
# 이동 전 자신의 자리에 원자가 있으면 폭발
# 이때                새로운 자리에 표시 해준다.
#               이동하려는 자리에 원자 있으면 폭발
#               이때 새로운 자리에 표시해준다.

def bfs():
    ret = 0
    while len(atom) > 1:
        idx = 0
        board = [[0] * 4001 for _ in range(4001)]
        while idx < len(atom):
            num, x, y = atom[idx]
            nx, ny = x + dir[D[num]][0], y + dir[D[num]][1]
            if maxX < nx or maxY < ny or minX > nx or minY > ny:
                die[num] = True
                atom.remove((num, x, y))
                ret += energe[num]
            else:
                if -1 < nx < 4001 and -1 < ny < 4001:
                    if board[nx][ny]:
                        if not die[board[nx][ny]]:
                            die[board[nx][ny]] = True
                            atom.remove((board[nx][ny], nx, ny))
                            idx -= 1
                            ret += energe[board[nx][ny]]
                        die[num] = True
                        ret += energe[num]
                    else:
                        board[nx][ny] = num
                        idx += 1
    return ret

dir = [(-1, 0), (1, 0), (0, -1), (0, 1)] # 0상1하2좌3우
for tc in range(1, int(input()) + 1):
    N = int(input()) # 원자수
    atom = []
    die = [False] * (N + 1)
    energe = [0] * (N + 1)
    D = [0] * (N + 1)
    maxX, maxY, minX, minY = 0, 0, 4000, 4000
    for num in range(1, N + 1):
        x, y, d, K = map(int, input().split()) # x,y : 0~4000
        x, y = (x + 1000) * 2, (y + 1000) * 2
        maxX, maxY, minX, minY = max(maxX, x), max(maxY, y), min(minX, x), min(minY, y)
        atom.append((num, x, y))
        D[num] = d
        energe[num] = K
    ANS = bfs()
    print('#{} {}'.format(tc, ANS))