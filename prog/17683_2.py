# 17683_2.py 27번 테케 통과 못함
def solution(m, musicinfos):
    answer = "`(None)`"
    max_time = 0
    # info 나누기
    for x in range(len(musicinfos)):
        musicinfos[x] = musicinfos[x].split(',')
        # 재생시간 구하기
        end = musicinfos[x][1].split(':')
        start = musicinfos[x][0].split(':')
        end, start = list(map(int, end)), list(map(int, start))
        # 27번 테케 통과 x
        # if end[1] < start[1]:
        #     mi = 60 + end[1] - start[1]
        #     h = end[0] - start[0] + 1
        # else:
        #     mi = end[1] - start[1]
        #     h = end[0] - start[0]
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
        # print(m, mellody)
        # m과 일치여부 확인
        if len(m) > len(tmp):
            continue
        for idx in range(len(tmp) - len(m) + 1):
            if m == tmp[idx:idx + len(m)]:
                if idx + len(m) < len(tmp) and tmp[idx + len(m)] == '#':
                    continue
                if max_time < totalM:
                    answer = musicinfos[x][2]
                    max_time = totalM
    return answer

# m = "ABCDEFG"
# musicinfos = ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]

m, musicinfos = "CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]
# m, musicinfos = "ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]
print(solution(m, musicinfos))