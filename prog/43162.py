# 43162.py 네트워크
def solution(n, computers):
    answer = 0

    def dfs(x):
        visit[x] = True
        for v in adj[x]:
            if not visit[v]:
                dfs(v)

    adj = [[] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if i != j and computers[i][j]:
                adj[i].append(j)
                adj[j].append(i)
    visit = [False] * n
    for x in range(n):
        if not visit[x]:
            answer += 1
            dfs(x)
    return answer

n, computers = 3,	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))