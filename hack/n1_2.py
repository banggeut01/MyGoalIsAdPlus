def solution(A):
    result = 0
    idx = 0
    while idx < len(A):
        visit = [False] * 123 # a:97 ~ z:122
        for c in A[idx]:
            if not visit[ord(c)]:
                visit[ord(c)] = True
            else:
                A.pop(idx)
                break
        else:
            idx += 1
    if not A:
        return result

    MAX = 0
    AL = len(A)
    for i in range(1 << AL):
        g1, g2 = [], []
        for j in range(AL):
            if i & 1 << j:
                g1.append(j)
        if len(g1) >= 1:
            word = ""
            for x in g1:
                word += A[x]
            # 중복 검사
            visit = [False] * 123  # a:97 ~ z:122
            for c in word:
                if not visit[ord(c)]:
                    visit[ord(c)] = True
                else: break
            else:
                result = max(result, len(word))
    return result