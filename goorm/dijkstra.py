# dijkstra.py
# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
N, E = map(int, input().split())
edge, elist = {}, []

# 1. edge 간선 정보 받기 edge = {(1, 2): 5, ... }
for _ in range(E):
	s, e, w = map(int, input().split())
	min_n, max_n = min(s, e), max(s, e)
	if edge.get((min_n, max_n)): edge[(min_n, max_n)] = min(edge[(min_n, max_n)], w)
	else: edge[(min_n, max_n)] = w

# 시작점 start
start = int(input())

# elist = [(5, 1, 2), ... ] 간선 정보 리스트로
for key, val in edge.items():
	s, e = key
	elist.append((val, s, e))

# start 시작점부터 방문하기
visit = [False] * (N + 1)
dist = [0xffffff] * (N + 1)
visit[start] = True
dist[start] = 0
# print(elist)
for _ in range(N - 1):
	min_n, min_d = 0, 0xffffff
	for i in range(len(elist)):
		w, s, e = elist[i]
		if s == start and not visit[e]:
			dist[e] = min(dist[e], dist[s] + w)
			if min_d > dist[e]:
				min_n, min_d = e, dist[e]
		elif not visit[s] and e == start:
			dist[s] = min(dist[s], dist[e] + w)
			if min_d > dist[s]:
				min_n, min_d = s, dist[s]
	start = min_n
	visit[start] = True

# 출력
for idx in range(1, N + 1):
	print('{}: {}'.format(idx, dist[idx]))
