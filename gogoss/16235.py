# 16235.py 나무 재테크
# 봄 나이만큼 양분 먹고, 나이 1 증가,, 나무 여러개면 가장 어린 나무부터
# 양분 부족해 나이만큼 양분 못먹으면 -> 죽음

# 죽은 나무 -> 양분 (나이 // 2)

# 번식, 5의 배수이면 인접 8 칸에 나이 1인나무 생성

# 양분 추가
def solution():
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) > 0:
                board[i][j] = sorted(board[i][j])
                for idx in range(len(board[i][j])):
                    if food[i][j] >= board[i][j][idx]:
                        food[i][j] -= board[i][j][idx]
                        board[i][j][idx] += 1
                    else:
                        for _ in range(idx, len(board[i][j])):
                            food[i][j] += board[i][j][idx] // 2
                            board[i][j].pop(idx)
                        break

    for x in range(N):
        for y in range(N):
           if len(board[x][y]) > 0:
                for namoo in board[x][y]:
                    if namoo > 0 and not namoo % 5:
                        for dx, dy in (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1):
                            nx, ny = x + dx, y + dy
                            if -1 < nx < N and -1 < ny < N:
                                board[nx][ny].append(1)
           food[x][y] += A[x][y]

N, M, K = map(int, input().split())
food = [[5] * N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
board = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().split())
    board[x - 1][y - 1].append(z)
for _ in range(K):
    solution()
cnt = 0
for i in range(N):
    for j in range(N):
        cnt += len(board[i][j])
print(cnt)