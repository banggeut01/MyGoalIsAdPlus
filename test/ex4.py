# ex4.py


def solution(snapshots, transactions):
    # answer = [[]]
    answer = dict(snapshots)
    for key, val in answer.items():
        answer[key] = int(val)
    used_trans = dict()
    for tran in transactions:
        num, cate, acc, mon = tran # id, 종류, 계좌, 돈
        mon = int(mon)
        if used_trans.get(num): continue
        used_trans[num] = True
        if answer.get(acc):
            if cate == "SAVE": answer[acc] += mon
            else: answer[acc] -= mon
        else:
            answer[acc] = mon
    ret = []
    for key, val in answer.items():
        ret.append([key, str(val)])
    return sorted(ret)

snapshots = [
  ["ACCOUNT1", "100"],
  ["ACCOUNT2", "150"]
]

transactions = [
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["2", "WITHDRAW", "ACCOUNT1", "50"],
  ["1", "SAVE", "ACCOUNT2", "100"],
  ["4", "SAVE", "ACCOUNT3", "500"],
  ["3", "WITHDRAW", "ACCOUNT2", "30"]
]

print(solution(snapshots, transactions))