# 1952.py 수영장

def updateMIN(k, cur): # k:현재달 0~11, cur: 현재 요금
    global MIN
    if cur >= MIN:
        return

    if k >= 12:
        MIN = min(MIN, cur)
        return

    # 이용 o
    if sum(fee[k : k + 3]) > cost[2]:
        updateMIN(k + 3, cur + cost[2])
    # 이용 x
    updateMIN(k + 1, cur + fee[k])

for tc in range(1, int(input()) + 1):
    cost = list(map(int, input().split()))
    use = list(map(int, input().split()))
    fee = [0] * 12
    # 1일 vs 1달
    for idx in range(12):
        if use[idx]:
            fee[idx] = min(cost[0] * use[idx], cost[1])
    MIN = sum(fee)
    # 3달
    updateMIN(0, 0)
    # 1년
    MIN = min(MIN, cost[3])
    print('#{} {}'.format(tc, MIN))