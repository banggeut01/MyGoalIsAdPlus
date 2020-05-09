# ka4.py
# 직선: 100 원
# 코너: 500 원
# 처음 방향 4로 두고 시작함! 나중에 -400원 해주기

ANS = 0xffffff

def solution(board):
    N = len(board)

    xy = {
        0: (-1, 0),
        1: (1, 0),
        2: (0, -1),
        3: (0, 1)
    }

    def dfs(x, y, cost, d):
        global ANS
        if cost >= ANS:
            return

        if x == N - 1 and y == N - 1:
            ANS = cost
            return

        for idx in range(4):
            nx, ny = x + xy[idx][0], y + xy[idx][1]
            if -1 < nx < N and -1 < ny < N:
                if d != idx:
                    if not board[nx][ny] or board[nx][ny] >= cost + 600:
                        board[nx][ny] = cost + 600
                        dfs(nx, ny, cost + 600, idx)
                else:
                    if not board[nx][ny] or board[nx][ny] >= cost + 100:
                        board[nx][ny] = cost + 100
                        dfs(nx, ny, cost + 100, idx)

    dfs(0, 0, 0, 1)
    dfs(0, 0, 0, 3)
    answer = ANS
    return answer

# board = [[0,0,0],[0,0,0],[0,0,0]]
board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
# board = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]
# board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]

print(solution(board))