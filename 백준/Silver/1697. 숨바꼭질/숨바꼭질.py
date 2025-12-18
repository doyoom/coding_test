from collections import deque

def bfs(n, k):
    MAX = 100001
    visited = [-1] * MAX
    queue = deque()
    
    queue.append(n)
    visited[n] = 0

    while queue:
        x = queue.popleft()

        if x == k:
            return visited[x]

        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx < MAX and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                queue.append(nx)

n, k = map(int, input().split())
print(bfs(n, k))
