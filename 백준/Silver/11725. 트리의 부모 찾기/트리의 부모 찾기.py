#BFS
#크리스마스 이브라 트리 문제
from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
parent = [0] * (n + 1)
queue = deque([1])
parent[1] = -1
while queue:
    cur = queue.popleft()
    for nxt in graph[cur]:
        if parent[nxt] == 0:
            parent[nxt] = cur
            queue.append(nxt)
for i in range(2, n + 1):
    print(parent[i])