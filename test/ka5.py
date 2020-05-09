# ka5.py

def solution(n, path, order):
    answer = False
    adj = [[] for _ in range(9)]
    for s, e in path:
        adj[s].append(e)
    print(adj)

    return answer

n, path, order = 9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[8,5],[6,7],[4,1]]
# n, path, order = 9,	[[8,1],[0,1],[1,2],[0,7],[4,7],[0,3],[7,5],[3,6]],	[[4,1],[5,2]]
# n, path, order = 9,	[[0,1],[0,3],[0,7],[8,1],[3,6],[1,2],[4,7],[7,5]],	[[4,1],[8,7],[6,5]]

print(solution(n, path, order))