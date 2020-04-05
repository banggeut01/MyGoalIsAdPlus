#ex5.py

def solution(dataSource, tags):
    answer = []
    isExist = dict()
    for row in dataSource:
        for x in range(1, len(row)):
            isExist[(row[0], row[x])] = True
    num = dict()
    for row in dataSource:
        for tag in tags:
            if isExist.get((row[0], tag)):
                if num.get(row[0]): num[row[0]] += 1
                else: num[row[0]] = 1
    tmp = []
    for key, val in num.items():
        tmp.append((val, key))
    tmp = sorted(tmp, key=lambda x: x[1])
    tmp = sorted(tmp, key=lambda x: x[0], reverse=True)
    answer = [x[1] for x in tmp]
    return answer

dataSource = [
    ["doc1", "t1", "t2", "t3"],
    ["doc2", "t0", "t2", "t3"],
    ["doc3", "t1", "t6", "t7"],
    ["doc4", "t1", "t2", "t4"],
    ["doc5", "t6", "t100", "t8"]
]
tags = ["t1", "t2", "t3"]

print(solution(dataSource, tags))
