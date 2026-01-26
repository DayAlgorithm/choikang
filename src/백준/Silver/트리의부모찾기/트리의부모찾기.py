import sys
from collections import deque
def bfs(current):
    queue=deque([current])
    # 현재 정점 방문 처리
    visited[current]=True
    # 현재 정점과 연결된 정점들 중 아직 방문하지 않은 정점이 있다면
    while queue:
        current = queue.popleft()
        for next in graph[current]:
            if not visited[next]:
                visited[next]=True
                parent[next]=current
                queue.append(next)

#정점의 개수
n=int(sys.stdin.readline())
#그래프
graph=[[]for _ in range(n+1)]
#해당 정점을 방문했는지 여부
visited=[False]*(n+1)
#부모 자식 관계
parent=[0]*(n+1)

for _ in range(n-1):
    a,b=map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(1)

for i in range(2,(n+1)):
    print(parent[i])
