# 클래스와 함수 선언 부분 
class Node() : # Node 클래스를 정의한다.
    def __init__(self) :
        self.data = None
        self.link = None

def printNodes(start) : # 단순 연결 리스트에 전체 노드를 출력한다.
    current = start 
    if current == None : # 현재의 None을 대입
        return

    print(current.data, end = ' ')
    while current.link != None :
        current = current.link
        print(current.data, end = ' ')
    print()


# 전역변수 선언 부분
memory = []
head, current, pre = None, None, None
dataArray = ["엔코", "신군", "엔코신군", "챌", "김실버"]

# 메인코드 부분
if __name__ == "__main__" :

    node = Node()   # 첫번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] :  # 두번째 이후 노드
        pre = node
        node = Node()
        node.data =data
        pre.link = node
        memory.append(node)

    printNodes(head)


# 노드 삽입
# : 완성된 단순 연결 노드에서 맨 앞, 중간, 맨 끝에 코드를 넣는 방식을 각각 구현해볼 것이다.
#   우선 맨 앞에 넣는 로직을 설명하자면
#   0) 맨 앞에 노드를 삽입하기 전 상태
#   1) 새 노드를 생성
#   2) 새 노드의 링크로 head가 가리키는 노드를 저장
#   3) head를 새 노드로 지정
#
# node = Node()
# node.data = "엔코"
# node.link = head
# head = node


#  중간 노드에 삽입하는 과정
#  0) 중간 노드 삽입 전 원래 노드
#  1) head 에서 시작해 현재 노드가 '엔' 인지 확인
#  2) 현재 노드를 이전 노드로 저장, 현재 노드를 다음 노드로 이동, 현재 노드가 '엔' 인지 확인
#  3) 현재 노드가 '엔' 일때까지 2) 단계를 반복수행
#  4) 현재 노드가 '엔' 이라면 새 노드를 생성 후 이전 노드의 링크를 새 노드의 링크로 지정.
#  5) 이전 노드의 링크를 새 노드로 지정
#
# current = head
# while 마지막 노드까지 :
#     pre = current
#     current = current.link

#     if current.data == "엔":
#         node = Node()
#         node.data = "코"
#         node.link = current
#     pre.link = node


# 마지막 노드 삽입
# 1~3) 까지 중간 노드 삽입과 과정이 같으므로 참고하면 된다.
# 4) 마지막 노드가 '신' 을 찾지 못했다면 우선 새 노드를 생성한 후 현재 노드의 링크를 새 노드로 지정.


# 노드 삽입 함수의 완성

## class와 function 선언 부분
class Node() :
    def __init__(self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start 
    if current == None : # 현재의 None을 대입
        return

    print(current.data, end = ' ')
    while current.link != None :
        current = current.link
        print(current.data, end = ' ')
    print()


def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData :
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData :
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    
    node = Node()  # 마지막 노드 삽입
    node.data = insertData
    current.link = node

# 전역변수 선언부분
memory = []
head, current, pre = None, None, None
dataArray = ["엔코", "신군", "엔코신군", "챌", "김실버"]

# 메인코드부분
if __name__ == "__main__" :


    node = Node()   # 첫번째 노드
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:] :  # 두번째 이후 노드
        pre = node
        node = Node()
        node.data =data
        pre.link = node
        memory.append(node)

    printNodes(head)

    insertNode("엔코", "엔")
    printNodes(head)

    insertNode("챌", "코")
    printNodes(head)

    insertNode("재남", "신")
    printNodes(head)