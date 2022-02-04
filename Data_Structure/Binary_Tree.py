# 이진트리는 맨위에서부터 0차 아래로 내려갈수록 하나씩 추가되는 형식이다.
# 물론 나뭇가지의 단위는 리스트와 같이 Node다. 
# 컴퓨터는 0과 1로 이루어져있기 때문에, 최대 2차까지만 허용되는 것이 효율적이라 Binary Tree(이진 트리)라고 명명되었다.
# 이진트리는 위Node와 아래Node를 부모 자식 관계로 비유한다. 
# 자식 노드 개수를 degree(차수)라고 하고, 자식이 없는, 즉 차수가 0인 Node를 leaf(리프)하고 한다.

# 포화 이진트리
# : 모든 Node가 꽉 차있는 상태의 트리, 노드 개수가 2^(height+1) - 1 공식으로 계산된다. 
# ex) height(높이)가 3인 포화 이진트리는 노드 개수가 15개다. 

# 완전 이진트리
# : 완전 이진트리는 번호를 부여한 순서로 노드가 배치된다. 노드가 일부 비어있어도 되지만, 끝 번호의 노드는 비어있어야 한다.

# 편향 이진트리
# : 편향 이진트리는 모든 노드가 한쪽 방향으로 연결된 트리다.

# 하나의 트리는 왼쪽으로 뻗어나가는 자식, 오른쪽으로 뻗어나가는 자식으로 구성된다.

# if) 높이가 2, 데이터가 6개인 이진트리를 구현한다고 치면
# 1) 루프 Node를 생성
# 2) 두 번째 Node를 생성, 루트 Node의 왼쪽 Node로 지정
# 3) 세 번째 Node를 생성, 루트 Node의 오른쪽 Node로 지정
# 4) 네 번째부터 여섯 번째까지 Node를 생성하고 부모 Node와 연결한다.

# 이와 같은 과정은 다음과 같이 표기한다.
class TreeNode() :   # 이진 트리 노드 생성
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None 

node1 = TreeNode()   # loot Node를 생성한다.
node1.data = 'Fuzzy' # node1에 Fuzzy를 할당 (0층)

node2 = TreeNode()   
node2.data = 'Hado'
node1.left = node2   # node1 좌측에 node2를 생성 (이때 1층이 생성된다.)

node3 = TreeNode()
node3.data = 'Hampton'
node1.right = node3  # node1 우측에 node3를 생성 (여기까지가 1층)

node4 = TreeNode()
node4.data = 'Dixie'
node2.left = node4   # node2를 부모 Node로 하는 좌측 자식노드 생성(이때 2층이 생성)

node5 = TreeNode()
node5.data = 'Hamster'
node2.right = node2  # node2를 부모 Node로 하는 우측 자식노드 생성(이때 2층)

node6 = TreeNode()
node6.data = 'Dance'
node3.left = node6   # node3를 부모 Node로 하는 좌측 자식 노드 생성(이때 2층)

print(node1.data, end = ' ')
print()
print(node1.left.data, node1.right.data, end = ' ')
print()
print(node1.left.left.data, node1.left.right.data, node1.right.left.data, end = ' ')
#----------------------------------------------------------------------------------------------

# 이렇게 자식노드를  생성했다. 근데 한가지 의문이 든다. 왜 굳이 트리를 만든걸까?
# 답은 간단하다. 속도, 성능 중에서 한가지 이상이 편리하기 때문일 것이다. 
# 앞서봤던 Stack과 Que 에서는 정보를 탐색할때 순차적으로 돌아야하기 때문에, 시간이 오래걸리고, 이는 곧 성능 문제에 도달한다.
# But) Tree는 각 부모 Node 밑으로 자식 Node가 있으므로 탐색을 하기에 최적화 되어있다.
# 이는 알고리즘 문제에 가장 자주 등장하는 이진 탐색에도 응용이 될터이니 꼭 알아두자.

'''
순회
: 이진 트리의 Node를 한번씩 방문하는 것을 의미한다. 필요한 Data를 효과적으로 검색하는데 필요하다.
Node Data를 처리하는 순서에 따라 순회하는 세가지 방법이 있다.

전위 순회 
: Node의 Data를 먼저 처리
1) 현재 Node Data 처리
2) left 서브 트리로 이동
3) right 서브 트리로 이동

중위 순회
: Node의 Data를 중간에 처리한다.
1) left 서브 트리로 이동
2) 현재 NOde Data 처리
3) right 서브 트리로 이동

후위 순회
: Node의 Data를 마지막에 처리한다.
1) left 서브 트리로 이동
2) light 서브 트리로 이동
3) 현재 Node Data 처리
'''

# 이진 트리 순회 구현
# : Stack을 이용하는 방식과 Recursion Function(재귀 함수)을 이용하는 방법이 있다. 
#  Stack을 이용하는 방식은 복잡하므로, 재귀 함수로 구현해보겠다. 
#  참고로 재귀함수는 자신이 자신을 호출하는 함수이다.


class TreeNode() :   # 이진 트리 노드 생성
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None 

node1 = TreeNode()   # loot Node를 생성한다.
node1.data = 'Fuzzy' # node1에 Fuzzy를 할당 (0층)

node2 = TreeNode()   
node2.data = 'Hado'
node1.left = node2   # node1 좌측에 node2를 생성 (이때 1층이 생성된다.)

node3 = TreeNode()
node3.data = 'Hampton'
node1.right = node3  # node1 우측에 node3를 생성 (여기까지가 1층)

node4 = TreeNode()
node4.data = 'Dixie'
node2.left = node4   # node2를 부모 Node로 하는 좌측 자식노드 생성(이때 2층이 생성)

node5 = TreeNode()
node5.data = 'Hamster'
node2.right = node2  # node2를 부모 Node로 하는 우측 자식노드 생성(이때 2층)

node6 = TreeNode()
node6.data = 'Dance'
node3.left = node6   # node3를 부모 Node로 하는 좌측 자식 노드 생성(이때 2층)


def preorder(node) :
    if node == None :
        return 
    print(node.data, end = '->')
    preorder(node.left)
    preorder(node.right)

def inorder(node) :
    if node == None :
        return 
    inorder(node.left)
    print(node.data, end = '->')
    inorder(node.right)

def postorder(node) :
    if node == None :
        return 
    postorder(node.left)
    postorder(node.right)
    print(node.data, end = '->')

print('전위 순회 : ', end =' ')
preorder(node1)
print('끝')

print('중위 순회 : ', end =' ')
inorder(node1)
print('끝')

print('후위 순회 : ', end =' ')
postorder(node1)
print('끝')
#----------------------------------------
"""
이진 탐색 트리
: 이진 트리 중 가장 자주 사용, 데이터 크기를 기준으로 구성한다.
  일정 값을 기준으로 하여 작은 값은 left, 큰 값은 right로 구성
이를 정리하자면
1) 왼쪽 서브 트리는 루트 Node보다 모두 작은 값을 가진다.
2) 오른쪽 서브 트리는 루트 Node보다 모두 큰 값을 가진다.
3) 각 서브 트리도 위와 같은 특징을 갖는다.
4) 모든 Node 값은 중복되지 않는다. 이말은 중복된 값은 이진 탐색 트리에 저장할 수 없다. 라는 뜻이다 
"""
# Data의 개수가 제한적이지 않고 무한해야 하기 때문에, 루트 Node만 root로 사용하고, 나머지 Node는 무한대 메모리에 넣는 형태로 생성한다
memory = []
root = None 
nameAry = ['Fuzzy', 'Hado', 'Hampton', 'Dixie', 'Hamster', 'Dance']

node = TreeNode()       # Node 생성
node.data = nameAry[0]  # Data 입력
root = node             # 첫 번째 Node를 루트 Node로 지정 
memory.append(node)     # 생성한 Node를 메모리에 저장

# 맨 위는 root로 사용하지만, 밑에 뻗어나가는 가지들은 이진 탐색트리를 고려해야 한다.
name = 'Hado'           # 2 번째 Data
node = TreeNode()       # 새 Node 생성
node.data = name        # 새 Node에 Data 입력
current = root          # 현재 작업 Node를 루트 Node로 지정
if name < current.data :
    current.left = node # 작으면 새 노드를 왼쪽 링크로 연결
else :
    current.right = node# 크면 새 노드를 오른쪽 링크로 연결
memory.append(node)     # 새 노드를 메모리에 저장
#-------------------------------------------------------------------------------
# 이진 탐색 트리의 삽입 작동
class TreeNode() :
    def __init__ (self) :
        self.left = None 
        self.data = None
        self.right = None

memory = []
root = None 
nameAry = ['Fuzzy', 'Hado', 'Hampton', 'Dixie', 'Hamster', 'Dance']

node = TreeNode()                  # 클래스에 접근
node.data = nameAry[0]             # 노드에 첫번째 데이터 삽입
root = node 
memory.append(node)

for name in nameAry[1:] :          # [1:] 1부터 끝까지를 의미

    node = TreeNode()
    node.data = name 

    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left == node 
                break 
            current = current.left 
        else :
            if current.right == None :
                current.right = node 
                break 
            current = current.right 
    memory.append(node)
print("이진 탐색 트리 구성 완료!")
#-----------------------------------------------------
"""
이진 탐색 트리에서 Data 검색
if 현재 작업 노드의 Data == 찾을 Data :
    탐색 종료
elif 현재 작업 노드의 Data < 찾을 Data :
    왼쪽 서브 트리 검색 
else :
    오른쪽 서브 트리 검색 
"""
