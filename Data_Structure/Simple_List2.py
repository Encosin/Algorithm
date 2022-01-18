# 이번에는 삭제부터 검색, 응용까지 다뤄보려고 한다.
# dataArray = ["엔코", "신군", "엔코신군", "챌", "김실버"]

# * 첫 번째 노드 삭제 
# 1) 현재 노드를 삭제할 노드인 head와 동일하게 만든다.
# 2) head를 삭제할 노드(엔코)의 링크가 가리키던 "신군" 으로 변경된다.
# 3) "엔코" 를 메모리에서 제거한다. 

# code) =>
# current = head
# head = head.link
# del(current)

# * 중간 노드 삭제("엔코신군")
# : 이건 알고리즘에 더 가까운 것 같다. 앞에서부터 순차적으로 비교해서 원하는 방식을 찾는 검색 알고리즘을 참고하자.
# 1) head (첫 번째)부터 시작해서 "엔코신군" 이 맞는지 확인하고 아니라면, 두 번째를 확인한다
# 2) 만약 두 번째에서 "엔코신군" 이 아니라면 한칸씩 앞으로 당기는 식으로 확인한다.
# 3) 이제 "엔코신군" 을 확인할 시, 그 노드를 현재 노드로 지정하고 마친다.

# code) =>
# current = head
# while 김실버 :
#     pre = current
#     current = current.link
#     if current.data == "엔코신군" :
#         pre.link = current.link
#         del(current)

# ---------------------------------------------
# 함수 선언부
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

def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData :
        current = head 
        head = head.link
        del(current)
        return 
    
    current = head
    while current.link != None :
        pre = current 
        current = current.link
        
        if current.data == deleteData :
            pre.link = current.link 
            del(current)
            return 

# 전역 변수 선언 부분 
memory = []
head, current, pre = None, None, None
dataArray = ["엔코", "신군", "엔코신군", "챌", "김실버"]

# 메인 코드 부분
if __name__ == "__main__" :

    node = Node()   # 첫 번째 노드
    node.data = dataArray[0]
    head = node 
    memory.append(node)
    for data in dataArray[i] :   
        pre = node 
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    deleteNode("엔코")   # 첫 번째 노드인 "엔코" 를 삭제
    printNodes(head)     # "엔코" 삭제 후 출력

    deleteNode("엔코신군")   # 중간 노드인 "엔코신군" 을 삭제
    printNodes(head)        # "엔코신군" 삭제 후 출력

    deleteNode("김실버")    # 마지막 노드인 "김실버" 를 삭제 후 출력한다. 
    printNodes(head)       
    # 결과 : 신군 챌
# ----------------------------------------------

# * 노드 검색
# 1) 현재 노드(current)를 첫 번째 노드인(head)와 같게 만들고, 현재 노드가 검색할 Data인지 비교한다. 동일하다면 현재 노드를 반환한다.
# 2) Data가 일치하지 않다면 다음 노드로 넘어가서 비교 후 동일하면 반환, 아니면 다시 다음으로 넘어간다.
# 3) 2번째 단계를 끝까지 실행하고 없다면 None 을 반환하고 종료한다.

# --------------------------------------------
# code) 
# 클래스와 함수 선언 부분
class Node() :
    def __init__ (self) :
        self.data = None 
        self.link = None 

def printNodes(start):
    current = start 

    if current == None :
        return 
    print(current.data, end = ' ')

    while current.link != None :
        current = current.link 
        print(current.data, end = ' ')
    print()

def findNode(findData) :
    global memory, head, current, pre 

    current = head 

    if current.data =findData :
        return current 

    while current.link != None :
        current = current.link 

        if current.data == findData : 
            return current 
    return Node()  # 빈 노드 반환 


# 전역 변수 선언 부분
memory = [] 
head, current, pre = None, None, None 
dataArray = ["엔코", "신군", "엔코신군", "챌", "김실버"]

# main code 
if __name__ == "__main__" :

    node = Node()  # 첫번째 노드
    node.data = dataArray[0]
    head = node 
    memory.append(node)

    for data in dataArray[1:] :
        pre = node 
        node = Node()
        node.data = data 
        pre.link = node 
        memory.append(node) 

    printNodes(head)

    fNode = findNode("엔코")
    print(fNode.data)

    fNode = findNode("엔코신군")
    print(fNode.data)

    fNode = findNode("재남")
    print(fNode.data)

# ------------------------------------

# 그렇다면 응용은 어떻게 해야하나??
# 단순 연결리스트 응용 ex) 명함 관리

# 0) 입력할 데이터를 저장한다.
# dataArr = [["엔코", "010-4110-xxxx"], ["신군", "010-4110-OOOO"], ["엔코신군", "010-4110-OXOX"], ["챌", "010-4770-xxxx"], ["김실버", "010-4770-OOOO"]]
# 1) 데이터를 차례로 가져온다
# head = node
# 2) 두 번째 "신군" 을 대입한다 
# node.link = head 
# head = node 
# 3) 다음으로 "엔코신군" 을 대입하고, 새 Data가 첫 node 보다 작다면 새 node의 링크에 첫 node를 입력하고 head에는 새 node를 저장한다.
# 4) 다음으로 "챌"을 입력한다.
# current = head 
# while 김실버 :
#     pre = current 
#     current = current.link 
#     if cur_Node > fut_Node :
#         pre.link = node 
#         node.link = current 

# 5) finally input the "김실버"
# current.link = node 


# 자 이제 명함관리 프로그램을 실제로 구현해보자!
# --------------------------------------------
class Node() :
    def __init__ (self) :
        self.data = None 
        self.link = None 

def printNodes(start) :
    current = start 
    if current == None :
        return 
    print(current.data, end = ' ')

    while current.link != None :
        current = current.link 
        print(current.data, end = ' ')
    print()

def makeSimpleLinkedList(namePhone) :
    global memory, head, current, pre  
    printNodes(head)

    node = Node()
    node.data = namePhone 
    memory.append(node)

    if head == None :
        head = node 
        return 

    if head.data[0] > namePhone[0] :  # 첫 번째 노드보다 작을 때
        node.link = head 
        head = node 
        return 

    # 중간 노드로 삽입하는 경우
    current = head 
    while current.link != None :
        pre = current 
        current = current.link 
        if current.data[0] > namePhone[0] :
            pre.link = node 
            node.link = current 
            return 

    # 삽입하는 노드가 가장 큰 경우
    current.link = node 

# 전역 변수 선언 부분
memory = []
head, current, pre = None, None, None
dataArr = [["엔코", "010-4110-xxxx"], ["신군", "010-4110-OOOO"], ["엔코신군", "010-4110-OXOX"], 
           ["챌", "010-4770-xxxx"], ["김실버", "010-4770-OOOO"]]

# main code 
if __name__ == "__main__" :
    for data in dataArr :
        makeSimpleList(data)
    printNodes(head)
# ------------------------------------------------------------------------
        