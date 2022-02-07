# Graph
# 그래프는 여러 노드가 서로 연결된 자료구조다. 루트에서 하위노드로 이어지고 나서도 계속 다른 방향으로 이어질 수 있다.
# Ex) 지하철 노선도, 인맥 관계도, 전기 회로도

# 그래프는 크게 무방향, 방향, 가중치 그래프가 있다.
'''
무방향 그래프 
: Tree의 Node에 해당하는 용어가 그래프에서는 정점(Vertex)이다. 정점을 연결하는 선은 간선(Edge)이고, 그래프는 정점과 간선의 집합으로 볼 수 있다.
 따라서 정점 집합을 V(G), 간선 집합을 E(G) 로 표기한다.
 정점 집합 V(G1) = { A, B, C, D}, V(G2) = { A, B, C, D }
 간선 집합 E(G1) = { (A, B), (A, C), (A, D), (B, C), (c, D) } 
'''

'''
방향 그래프 
: 방향성이 있는 방향 그래프는 화살표로 간선 방향을 표기하고, 그래프의 정점 집합이 무방향 그래프와 같다.
V(G3) = { A, B, C, D }
E(G3) = { <A, B>, <A, C>, <D, A> }
'''

'''
가중치 그래프
앞서 살펴본 무방향, 방향 그래프는 모두 가중치가 1이라 따로 표기하지 않았지만, 간선마다 가중치가 다르게 부여된 그래프를 가중치 그래프라고 한다.
'''

'''
깊이 우선 탐색의 작동
: 원하는 Data를 찾고자 그래프의 모든 정점을 한번씩 방문하는 방법을 알아보자.

Graph Traversal (그래프의 순회) 
: 그래프의 모든 정점을 한 번씩 방문하는 것, 이는 또 두가지로 나뉘는데, DPS (깊이 우선 탐색), BFS (너비 우선 탐색)가 있다.
'''

'''
그래프의 인접 행렬 표현
: 그래프를 코드로 구현할 때는 인접 행렬(Adjacency Matrix)을 사용한다. 
 인접행렬은 정방향으로 구성된 행렬로 정점이 4개인 그래프는 4X4 인접 행렬로 표현한다.
'''

# 이와 같이 그래프를 실제로 구현해보자.
class Graph() :  # Graph 클래스를 인접 행렬로 정의했다. self.SIZE는 정점 개수(=인접 행렬의 행 및 열 크기)먀, self   
    def __init__(self, size) : 
        self.Size = size  # self.Size는 생성될 그래프 크기고, 
        self.graph = [[0 for _ in range(size)] for _ in range(size)]  # self.graph는 0으로 초기화된 2차원 배열이다.

G1 = Graph(4)
#------
# 그래프의 정점 연결
G1.graph[0][1] = 1 # (A, B) 간선
G1.graph[0][2] = 1 # (A, C) 간선
G1.graph[0][3] = 1 # (A, D) 간선
#----------------------------------------------------------------------------------------------------------------------

# P.324 Code 09-01.py 무방향 그래프 G1과 방향 그래프 G3의 구현
class Graph() : # Graph 클래스를 인접 행렬로 정의했다.   
    def __init__ (self, size) :
        self.SIZE = size # self.SIZE는 정점 개수(=인접 행렬의 행 및 열 크기)
        self.graph = [[0 for _ in range(size) for _ in range(size)]] # self.graph는 인접행렬이다.  

G1, G3 = None, None 
# 초기에 2차원 배열을 생성하고 모두 0으로 초기화한다.

G1 = Graph(4)  # 무방향 그래프로 사용할 G1 그래프를 생성한다. 간선 없이 정점만 4개 생성된다.
# 왼쪽 무방향 그래프의 각 정점마다 간선을 연결했다.
G1.graph[0][1] = 1; G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
# 그래프를 출력한다. 각 행별로 열을 4개씩 출력하여 결국 4X4 인접 행렬이 출력된다.
for row in range(4) :
    for col in range(4) :
        print(G1.graph[row][col], end = ' ')
    print()

# 방향 그래프로 사용할 G3 그래프를 생성한다. 간성 없이 정점만 4개 생성된다.
G3 = Graph(4)
# 오른쪽 방향 그래프의 각 정점마다 간선을 연결했다. 출벌점 A와 D만 간선을 가지고 있다.
G3.graph[0][1] = 1; G3.graph[0][2] = 1
G3.graph[3][0] = 1; G3.graph[3][2] = 1

print('G3 방향 그래프')
# 그래프를 출력한다.
for row in range(4) :
    for col in range(4) :
        print(G3.graph[row][col], end = ' ')
    print()

#-----------------------------------------------------

'''
깊이 우선탐색의 구현
: 스택을 사용해야 한다. 방문한 정점을 스택에 푸시해 놓고, 방문할 곳이 막다른 곳이라면 스택에서 팜하는 방식을 사용한다.
 그리고 기존에 방문했는지 여부를 확인하고자 방문했던 기록을 저장하는데 배열을 사용한다.

# 구현
stack = []
stack.append(값1)  # push(값1) 효과
data = stack.pop()  # data = pop() 효과

if len(stack) == 0 :
    print('스택이 비었음')


# visitAry 배열에 방문 정점을 저장해서 visitedAry 배열에 해당 정점이 있다면 방문한적이 있는 것으로 처리한다.
visitedAry = [] 
visitedAry.append(0)  # 정점 A(번호 0)를 방문했을 때
visitedAry.append(1)  # 정점 B(번호 1)를 방문했을 때

if i in visitedAry :
    print(chr(ord('A')+i), end = ' ')

'''

# 깊이 우선 탐색의 단계별 구현
class Graph() :  # 그래프 클래스 정의
    def __init__ (self, size) :
        self.SIZE = size 
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = None 
stack = [] # stack
visitedAry = []  # 방문한 정점, 방문 배열로 사용한다.

G1 = Graph(4)
# 그래프를 생성
G1.graph[0][2] = 1; G1.graph[0][3] = 1
G1.graph[1][2] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][0] = 1; G1.graph[3][2] = 1

print('## G1 무방향 그래프 ##')
# 그래프 인접행렬을 출력
for row in range(4) :
    for col in range(4) :
        print(G1.graph[row][col], end = ' ')
    print()

current = 0  # 시작 정점
# 시작정점 A를 방문하고 처리한다. stack에 A를 넣고, 방문기록에도 A를 넣는다.
stack.append(current)
visitedAry.append(current)

# stack에 아무것도 없을 때까지 반복한다. stack이 비었다는 의미는 모든 정점을 방문완료 했다는 뜻이다.
while (len(stack) != 0) :
    next = None   # 다음에 방문한 점을 None으로 초기화 
    for vertex in range(4) : # 현재 정점과 연결된 다른 정점을 찾는다. 찾을 정점은 0~4 순서로 반복한다. 
        if G1.graph[current][vertex] == 1 :
            if vertex in visitedAry : # 방문한 적 있는 정점이면 탈락
                pass 
            else : 
                next = vertex 
                break 

    if next != None :  # next가 계속 None이면 else 스택에서 정점을 하나 pop하여 현재 정점으로 지정한다.
        current = next 
        stack.append(current)
        visitedAry.append(current)

    else :
        current = stack.pop()

print('방문 순서 ->', end = ' ')
for i in visitedAry :
    print(chr(ord('A') + i), end = ' ')
#-----------------------------------------------------