# e2.py
R = { 0: 1, 1: 2, 2: 3, 3: 0 }
L = { 0: 3, 3: 2, 2: 1, 1: 0 }
D = [(-1, 0), (0, 1), (1, 0), (0, -1)] # 상, 우, 하, 좌

def solution(office, r, c, move):
    # idx 방향, 0~3
    N = len(office)
    answer, office[r][c], idx = office[r][c], 0, 0
    for m in move:
        if m == 'right':
            idx = R[idx]
        elif m == 'left':
            idx = L[idx]
        else:
            dr, dc = D[idx]
            nr, nc = r + dr, c + dc
            if -1 < nr < N and -1 < nc < N and office[nr][nc] > -1:
                r, c = nr, nc
                answer += office[r][c]
                office[r][c] = 0
    return answer

office = [[5,-1,4],[6,3,-1],[2,-1,1]]
r, c = 1, 0
move = ['go','go','right','go','right','go','left','go']
print(solution(office, r, c, move))