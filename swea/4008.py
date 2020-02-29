# 4008.py 숫자 만들기
import sys
# sys.stdin = open('4008input.txt', 'r')
def calculate():
    global MIN, MAX
    total = NUM[0]
    for idx in range(N - 1):
        if seq[idx] == '+':
            total += NUM[idx + 1]
        elif seq[idx] == '-':
            total -= NUM[idx + 1]
        elif seq[idx] == '*':
            total *= NUM[idx + 1]
        else:
            if total < 0: total = abs(total) // NUM[idx + 1] * (-1)
            else: total //= NUM[idx + 1]
    MIN, MAX = min(MIN, total), max(MAX, total)

def perm(k):
    if k == N - 1:
        calculate()
        return

    for idx in range(4):
        if CNT[idx]:
            seq[k] = OPER[idx]
            CNT[idx] -= 1
            perm(k + 1)
            CNT[idx] += 1

for tc in range(1, int(input()) + 1):
    N = int(input())
    CNT = list(map(int, input().split())) # + - * /
    NUM = list(map(int, input().split()))
    OPER = ['+', '-', '*', '//']
    seq = [''] * (N - 1)
    MIN, MAX = 100000000, -100000000
    perm(0)
    print('#{} {}'.format(tc, MAX - MIN ))