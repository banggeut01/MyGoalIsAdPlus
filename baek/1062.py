# 1062.py 가르침
def readWord():
    global MAX
    cnt = 0
    for i in range(N):
        for j in range(4, len(word[i])):
            if not dt.get(word[i][j]):
                break
        else:
            cnt += 1
    MAX = max(MAX, cnt)

def comp(k, s):
    if k == K - 5:
        readWord()
        return

    for idx in range(s, 123):
        if not dt.get(chr(idx)):
            dt[chr(idx)] = True
            comp(k + 1, idx + 1)
            dt.pop(chr(idx))

N, K = map(int, input().split())
MAX = 0
dt = { 'a': True, 'n': True, 't': True, 'i': True, 'c': True }
word = [list(input()) for _ in range(N)]
if K >= 5:
    comp(0, 98)
print(MAX)