# 그래프의 응용
''' 
1) 특정 정점이 그래프에 연결되어 있는지 확인하는 함수
gSize = 6 
def fineVertex(g, findVtx) :
    stack = []    # 방문 기록을 쌓기 위한 스택
    visitAry = []  # 방문한 정점

    current = 0  # 시작 정점
    stack.append(current)  # 스택에 현재 정점을 추가한다.
    visitedAry.append(current)  # 방문한 정점에 현재 정점 추가

    while (len(stack) != 0) :  # stack에 0이 될때까지, 즉 한번 다 돌때까지 무한루프
        next = None  # 다음 정점을 담을 곳을 초기화시켜놓는다.
        for vertex in range(gSize) :
            if g.graph[current][vertex] != 0 :
                if vertex in visitedAry :  # 방문한적 있는 정점이면 탈락
                    pass 
                else : # 방문한적이 없으면 다음 정점으로 지정
                    next = vertex 
                    break 
        if next != None :  # 다음에 방문할 정점이 있는 경우
            current = next  # 현재 정점을 다음 정점으로 초기화
            stack.append(current)  # 스택에 현재 정점을 쌓는다.
            visitedAry.append(current)
        else :
            current = stack.pop()  # 다음에 방문할 정점이 없는 경우

    if findVtx in visitedAry :
        return True 
    else :
        return False
'''
''' 
2) 최소 비용으로 자전거 도로 연결
Spanning Tree(신장 트리) 
: 최소 간선으로 그래프의 모든 정점이 연결되는 그래프. 
Minimum Cost Spanning Tree(최소 신장 트리)
: 가중치 그래프에서 만들 수 있는 신장 트리 중 합계가 최소인 것.
 보통 도시 간 도로를 건설할 때 가장 적은 비용으로 도로망을 구축하는 방법으로 활용된다. 

최소 신장 트리를 활용하면 자전거 도로를 최소 비용으로 연결 가능하다. 
이때 쓰이는 Algorithm이 Prim Algorithm, Kruskal Algorithm 등이 있다.

#----
 전체 자전거 도로를 위한 가중치 그래프 구현
: 전체 비용이 나와있는 가중치 그래프를 구현해보자.
G1 = None 
nameAry = ['춘천', '서울', '속초', '대전', '광주', '부산']
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5, 6

gSize = 6
G1 = Graph(gSize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25 
#----------------------------------------

가중치와 간선 목록 생성
: 가중치와 간선을 별도 배열로 만들어보자.
edgeAry = []
for i in range(gSize) :
    for k in range(gSize) :
        if G1.graph[i][k] != 0 :
            edgeAry.append([G1.graph[i][k], i, k])
#----------------------------------------------

간선 정렬
from operator import itemgetter
edgeAry = sorted(edgeAry, key = itemgetter(0), reverse = True)
#----------------------------------------

중복 간선 제거
nameAry = [] 
for i in range(0, len(edgeAry), 2) :
    nameAry.append(edgeAry[i])

-1 가중치가 높은 간선부터 제거
: 그래도 모든 도시는 서로 연결되어 방문이 가능해야 한다. 이 점을 꼭 고려하자.

-1) 서울-광주 간선 제거
index = 0
start = newAry[index][1]  # 서울
end = newAry[index][2]    # 광주

G1.graph[start][end] = 0
G1.graph[end][start] = 0

del(newAry[index])

-2) 서울-속초 간선 제거
index = 0
start = newAry[index][1]  # Seoul
end = newAry[index][2]  # 속초

G1.graph[start][end] = 0
G1.graph[end][start] = 0

del(newAry[index])

살펴보니 간선 간 제거 코드는 다 같았다.

그렇다면 제거 시도 후 원상 복구는 어떻게 다를까?
index = 0

start = newAry[index][1] 
end = newAry[index][2]  

G1.graph[start][end] = 0
G1.graph[end][start] = 0

startYN = findVertex(G1, start)
endYN = findVertex(G1, end)

if startYN and endYN :  # 두 정점 모두 그래프와 연결되어 있다면
    del(newAry[index])  # 가중치 배열에서 완전히 제거
else :
    G1.graph[start][end] = saveCost 
    G1.graph[end][start] = saveCost
    index += 1
#---------
'''

# P.350 Code 09-05.py 최소 비용으로 자전거 도로를 건설하는 전체 코드
class Graph() :
    def __init__ (self, size) :
        self.SIZE = size 
        self.graph = [[0 for _ in range(size)] for _ in range(size)]
        
def printGraph(g) :
    print(' ', end = ' ')
    for v in range(g.SIZE) :
        print(nameAry[v], end = ' ')
    print()
    for row in range(g.SIZE) :
        print(nameAry[row], end = ' ')
        for col in range(g.SIZE) :
            print(g.graph[row][col], end = ' ')
        print()

    print()

def findVertex(g, findVtx) :
    stack = []    # 방문 기록을 쌓기 위한 스택
    visitedAry = []  # 방문한 정점

    current = 0  # 시작 정점
    stack.append(current)  # 스택에 현재 정점을 추가한다.
    visitedAry.append(current)  # 방문한 정점에 현재 정점 추가

    while (len(stack) != 0) :  # stack에 0이 될때까지, 즉 한번 다 돌때까지 무한루프
        next = None  # 다음 정점을 담을 곳을 초기화시켜놓는다.
        for vertex in range(gSize) :
            if g.graph[current][vertex] != 0 :
                if vertex in visitedAry :  # 방문한적 있는 정점이면 탈락
                    pass 
                else : # 방문한적이 없으면 다음 정점으로 지정
                    next = vertex 
                    break 
        if next != None :  # 다음에 방문할 정점이 있는 경우
            current = next  # 현재 정점을 다음 정점으로 초기화
            stack.append(current)  # 스택에 현재 정점을 쌓는다.
            visitedAry.append(current)
        else :
            current = stack.pop()  # 다음에 방문할 정점이 없는 경우

    if findVtx in visitedAry :
        return True 
    else :
        return False

G1 = None 
nameAry = [ '춘천', '서울', '속초', '대전', '광주', '부산' ]
춘천, 서울, 속초, 대전, 광주, 부산 = 0, 1, 2, 3, 4, 5, 6

gSize = 6
G1 = Graph(gSize)
G1.graph[춘천][서울] = 10; G1.graph[춘천][속초] = 15
G1.graph[서울][춘천] = 10; G1.graph[서울][속초] = 40; G1.graph[서울][대전] = 11; G1.graph[서울][광주] = 50
G1.graph[속초][춘천] = 15; G1.graph[속초][서울] = 40; G1.graph[속초][대전] = 12
G1.graph[대전][서울] = 11; G1.graph[대전][속초] = 12; G1.graph[대전][광주] = 20; G1.graph[대전][부산] = 30
G1.graph[광주][서울] = 50; G1.graph[광주][대전] = 20; G1.graph[광주][부산] = 25
G1.graph[부산][대전] = 30; G1.graph[부산][광주] = 25 

print('## 자전거 도로 건설을 위한 전체 연결도 ##')
printGraph(61)

# 가중치 간선 목록
edgeAry = []
for i in range(gSize) :
    for k in range(gSize) :
        if G1.graph[i][k] != 0 :
            edgeAry.append([G1.graph[i][k], i, k])

from operator import itemgetter 
edgeAty = sorted(edgeAry, key = itemgetter(0), reverse = True)

newAry = [] 
for i in range(0, len(edgeAry), 2) :
    newAry.append(edgeAry[i])

index = 0 
while (len(newAry) > gSize-1) :  # 간선 개수가 '정점 개수 - 1'일 때까지 반복
    start = newAry[index][1]
    end = newAry[index][2]
    saveCost = newAry[index][0]

    G1.graph[start][end] = 0
    G1.graph[end][start] = 0

    startYN = findVertex(G1, start)
    endYN = findVertex(G1, end)

    if startYN and endYN :
        del(newAry[index])
    else :
        G1.graph[start][end] = saveCost 
        G1.graph[end][start] = saveCost 
        index += 1 

print('## 최소 비용의 자전거 도로 연결도 ##')
printGraph(G1)
#--------------------------