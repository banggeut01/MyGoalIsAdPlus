# 17683.py 방금그곡


# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

# m, musicinfos = "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
m, musicinfos = "ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
ANS = '(None)'
# info 나누기
Flag = False
for x in range(len(musicinfos)):
    musicinfos[x] = musicinfos[x].split(',')
    # 재생시간 구하기
    end = musicinfos[x][1].split(':')
    start = musicinfos[x][0].split(':')
    end, start = list(map(int, end)), list(map(int, start))
    if end[1] < start[1]:
        mi = 60 + end[1] - start[1]
        h = end[0] - start[0] + 1
    else:
        mi = end[1] - start[1]
        h = end[0] - start[0]
    totalM = h * 60 + mi
    # 재생시간 동안 음
    tmp = ''
    idx = 0
    mellody = musicinfos[x][3]
    for _ in range(totalM):
        if idx == len(mellody):
            idx = 0
        tmp += mellody[idx]
        idx += 1
        if idx < len(mellody) and mellody[idx] == '#':
            tmp += '#'
            idx += 1
    # m과 일치여부 확인
    if len(m) > len(tmp):
        continue
    for idx in range(len(tmp) - len(m) + 1):
        if m == tmp[idx:idx + len(m)]:
            ANS = musicinfos[x][2]
            flag = True
            break
    if Flag: break
print(ANS)
