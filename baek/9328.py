# 9328.py 열쇠
# chr(ord('a') - 32)
import collections
def open_door(x, y):
    board[x][y] = '.'

def open_doors(key):
    if door.get(key):
        for x, y in door[key]:
            board[x][y] = '.'

def bfs():
    dq = collections.deque()
    visit = [[False] * w for _ in range(h)]
    docu_cnt = 0
    for i in range(h):
        for j in range(w):
            if i == 0 or j == 0 or i == h - 1 or j == w - 1:
                if board[i][j] == '.':
                    dq.append((i, j))
                    visit[i][j] = True
                elif board[i][j] == '$':
                    board[i][j] = '.'
                    dq.append((i, j))
                    visit[i][j] = True
                    docu_cnt += 1
                elif 'a' <= board[i][j] <= 'z':
                    keys.add(board[i][j].upper())
                    open_doors(board[i][j].upper())
                    board[i][j] = '.'
                    dq.append((i, j))
                    visit[i][j] = True
                elif 'A' <= board[i][j] <= 'Z':
                    dq.append((i, j))
                    visit[i][j] = True


    while dq:
        updated = 0
        for _ in range(len(dq)):
            x, y = dq.popleft()
            if board[x][y] == '.':
                for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
                    nx, ny = x + dx, y + dy
                    if -1 < nx < h and -1 < ny < w and not visit[nx][ny]:
                        if board[nx][ny] == '.':
                            dq.append((nx, ny))
                            visit[nx][ny] = True
                            updated += 1
                        elif board[nx][ny] == '$':
                            board[nx][ny] = '.'
                            dq.append((nx, ny))
                            visit[nx][ny] = True
                            docu_cnt += 1
                            updated += 1
                        elif 'a' <= board[nx][ny] <= 'z':
                            keys.add(board[nx][ny].upper())
                            open_doors(board[nx][ny].upper())
                            board[nx][ny] = '.'
                            dq.append((nx, ny))
                            visit[nx][ny] = True
                            updated += 1
                        elif 'A' <= board[nx][ny] <= 'Z':
                            dq.append((nx, ny))
                            visit[nx][ny] = True
                            updated += 1
            else: # door
                dq.append((x, y))
        if not updated:
            return docu_cnt
    return docu_cnt

T = int(input())
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for tc in range(1, T + 1):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    keys = set(input().upper())
    door = dict()
    for i in range(h):
        for j in range(w):
            if 'A' <= board[i][j] <= 'Z':
                if door.get(board[i][j]):
                    door[board[i][j]].append((i, j))
                else:
                    door[board[i][j]] = [(i, j)]
    for key in keys:
        open_doors(key)
    print(bfs())

