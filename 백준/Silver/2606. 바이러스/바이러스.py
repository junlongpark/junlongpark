import sys
from collections import deque
n = int(sys.stdin.readline())
line = int(sys.stdin.readline())
net = [[] for _ in range(n+1)]
for _ in range(line):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True
    count = 0
    while q:
        cur = q.popleft()
        for i, val in enumerate(net[cur]):
            if visited[val] == False:
                q.append(val)
                visited[val] = True
                count += 1
    print(count)
visited = [False for _ in range(n+1)]
bfs()