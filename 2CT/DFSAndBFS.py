'''
Search (탐색) DFS/BFS 는 탐색 Algorithm 에서 매우 빈번히 출제되는 문제이다. 
이 두 탐색 알고리즘을 배우는데 선행하여 필요한 지식이 있는데 바로 Data_Structure에 Stack과 Queue이다. 
음 귀찮으니 생략하겠다.

스택 구현은 이거면 충분하다.
stack = []
stack.append(5)
stack.append(2)
stack.append(4)
stack.pop()
stack.append(7)
stack.append(1)
stack.append(6)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

#----------------------

다음은 queue 구현이다.

from collections import deque

# 큐 구현을 위해 deque 라이브러리 사용
queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
'''











'''
재귀함수는 자기 자신을 다시 호출하는 함수이다.
# 재귀함수 호출을 반복하는 코드
def recursive_function(i):
    # 100번째 호출을 했을 때 종료되도록 종료 조건 명시
    if i == 100 :
        return 
    print(i, '번째 재귀함수에서', i+1, '번째 재귀함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀함수를 종료합니다.')

recursive_function(1)
# 실행시켜보니 1~99까지 올라갔다가 다시 99부터 1까지 떨어진 후 종료되었다.

'''

'''
다음은 ! (팩토리얼) 구현 방법이다.
# 반복적으로 구현한 n! 
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기 
    for i in range(1, n+1) :
        result *= 1
    return result 

# 재귀적으로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    # n! = n * (n-1)!를 그대로 코드로 작성하기 
    return n * factorial_recursive(n-1)

# 각각의 방식으로 구현한 n! 출력 (n=5)
print('반복적으로 구현:', factorial_iterative(5))
print('재귀적으로 구현:', factorial_recursive(5))
'''

'''
최대공약수 계산(유클리드 호제법) 예제
* 두 개의 자연수에 대한 최대공약수를 구하는 대표적인 Algorithm으로는 유클리드 호제법이 있습니다.
what's the Uclid???? 
: 두 자연수 A, B에 대하여 (A>B) A를 B로 나눈 나머지를 R이라고 하자.
  이때 A와 B의 최대공약수는 B와 R의 최대공약수와 같습니다.

if) GCD(192, 162) 
단계    A      B
1      192    162
2      162    30
3      30     12
4      12     6

위의 if 예시와 같이 192를 162로 나눈 나머지 30을 B에 두고 다시 162를 30으로 나눈 나머지 12, 다시 30을 12로 나눈 나머지 6 이렇게 차례로 나열한다.

def gcd(a, b):
    if a % b == 0:
        return b 
    else:
        return gcd(b, a, b%a)

print(gcd(192, 162))

이렇듯 재귀함수를 잘 활용하면 복잡한 Algorithm을 간결하게 작성할 수 있습니다.
 오히려 다른사람이 이해하기 어려운 형태의 코드가 될수있으니 주의..
모든 재귀함수는 반복문을 이용하여 동일한 기능을 구현할 수 있습니다.
재귀함수가 반복문보다 유리한 경우도 있고, 반대로 불리한 경우도 있습니다.
컴퓨터가 함수를 연속적으로 호출하면 컴퓨터 메모리 내부의 스택 프레임에 쌓입니다. 
 그래서 스택을 사용해야 할 때, 구현상 스택 라이브러리 대신에 재귀함수를 이용하는 경우가 많습니다.
'''

'''
이제 진짜 DFS다..
what's the DFS(Depth-First Search)
: DFS는 깊이 우선 탐색이라고 부르며, 그래프에서 깊은 부분을 우선적으로 탐색하는 알고리즘 입니다.

DFS는 스택 자료구조(혹은 재귀함수)를 이용하며, 구체적인 동작과정은 다음과 같습니다. 
1) 탐색 시작 노드를 스택에 삽입하고 방문 처리를 합니다.
2) 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문 처리합니다. 
   방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냅니다.
3) 더 이상 2번의 과정을 수행할 수 없을때까지 반복합니다.

# DFS 메서드 정의
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v] = True  
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# 각 노드가 연결된 정보를 표현(2차원 리스트)
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7],
]

# 각 노드가 방문된 정보를 표현 
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph, 1, visited)
'''

'''
BFS(Breath-First Search) - 출제빈도 높다!
: 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 Algorithm 입니다.
BFS는 큐 자료구조를 이용하며, 구체적인 동작 과정은 다음과 같습니다. 
1) 탐색 시작 노드를 큐에 삽입하고 방문 처리를 합니다.
2) 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리합니다.
3) 더 이상 2번의 과정을 수행할 수 없을때까지 반복합니다.

일반적으로 수행시간은 DFS보다 좋은 편이다.
'''

# 5-9.py
'''
from collections import deque 

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    
    # 현재 노드를 방문처리
    visited[start] = True

    # 큐가 빌때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v= queue.popleft()
        print(v, end='')
        # 해당원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True  

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현
visited = [False]*9
bfs(graph, 1, visited)
'''

'''
<실전문제> 음료수 얼려먹기
N X M크기의 얼음틀이 있다. 구멍이 뚫려있는 부분은 0, 칸막이가 존재하는 부분은 1로 표시된다.
구멍이 뚫려있는 부분끼리 상, 하, 좌, 우로 붙어 있는 경우 서로 연결되어 있는 것으로 간주한다.
이때 얼음 틀의 모양이 주어졌을 때 생성되는 총 아이스크림의 개수를 구하는 프로그램을 작성하시오.
다음의 4X5 틀 예시에서는 아이스크림이 총 3개 생성된다.

입력조건:
1) 첫번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어진다.
2) 두번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어진다.
3) 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1이다.
'''

# N, M을 공백으로 구분하여 입력받기
n, m =map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False   

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        # 해당 노드 방문 처리
        graph[x][y] = 1
        # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출 
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True  
    return False   

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0 
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행 
        if dfs(i, j) == True:
            result += 1

print(result) # 정답 출력
