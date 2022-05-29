# 9-1.py 간단한 다익스트라 알고리즘 
# 방문하지 않은 곳을 무한대로 두고, 방문한 곳에 거리(?)를 표시. 짧을수록 좋다.
import sys  # 인터프리터를 제공해주는 모듈
from turtle import distance  # turtle 모듈은 Python에서 제공하는 기본 모듈이며, 이동을 띄워준다. left, right 등등
input = sys.stdin.readline  # input()으로 여러 반복문을 입력받게 되면 시간초과가 난다. 그래서 대신 사용해주는게 sys.stdin.readline 이다!
INF = int(1e9)  # 무한을 의미하는 값으로 10억을 설정 

# 노드의 개수, 간선의 개수를 입력받기 
n, m = map(int, input().split())  # map은 알다시피 한번에 여러가지 기능을 담게 해준다.

# 시작 노드 번호를 입력받기 
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n+1)]

# 방문한적이 있는지 체크하는 목적의 리스트를 만들기
visited = [[False] * (n + 1)]

# 최단거리 테이블을 모두 무한으로 초기화 
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기 
for _ in range(m):  # i대신 _를 쓴 것은 의미없는 값으로 단순히 반복 횟수만 채울 때 주로 사용한다.
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 C라는 의미
    graph[a].append(b, c)
    
# 방문하지 않은 노드 중에서, 가장 최단거리가 짧은 노드의 번호를 반환 
def get_smallest_node():
    min_value = INF 
    index = 0  # 가장 최단 거리가 짧은 node(인덱스)
    for i in range(1, n+1):
        if distance[i] < min.value and not visited[i]:
            min_value = distance[i]
            index = i 
            
    return index 

def dijkstra(start):
    # 시작 노드에 대해 초기화 
    distance[start] = 0 
    visited[start] = True   
    for j in graph[start]:
        cost = distance[now] + j[1]
        # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[j[0]]:
            distance[j[0]] = cost                  
            
# 다익스트라 알고리즘 수행 
dijkstra(start)

# 모든 노드로 가기 위한 최단거리를 출력 
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력 
    if distance[i] == INF:
        print("INFINITY")
        
    # 도달할 수 있는 경우 거리를 출력 
    else: 
        print(distance[i]) 
        
        
        