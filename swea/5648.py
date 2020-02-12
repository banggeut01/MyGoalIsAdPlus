# 5648.py 원자 소멸 시뮬레이션

def simul():
    global atom
    ret = 0
    t = 0
    while t < 4000 and len(atom) > 1:
        tmp = dict() # 이동 후 원자들
        for key, val in atom.items():
            x, y = key
            d, k = val
            nx, ny = x + D[d][0], y + D[d][1]
            if -2001 < nx < 2001 and -2001 < ny < 2001:
                if tmp.get((nx, ny)):
                    tmp[(nx, ny)].append(k)
                else:
                    tmp[(nx, ny)] = [d, k]
        atom = dict()
        for key, val in tmp.items():
            if len(val) > 2:
                ret += sum(val[1:])
            else:
                atom[key] = val
        t += 1
    return ret

# D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
D = [(1, 0), (-1, 0), (0, -1), (0, 1)]
for tc in range(1, int(input()) + 1):
    N = int(input())
    atom = dict()
    for _ in range(N):
        y, x, d, k = map(int, input().split())
        atom[(x * 2, y * 2)] = [d, k]
    print('#{} {}'.format(tc, simul()))