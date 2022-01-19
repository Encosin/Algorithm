# 원형 연결리스트에 대해 학습해보자.
# 근데 사실 단순연결 리스트랑 다를게 별로 없다.
# 오늘도 외치고 시작하자! 
# Life is short, You need Python!
#--------------------------------------------
class Node() :
    def __init__ (self) :
        self.data = None 
        self.link = None 

node1 = Node()
node1.data = "엔코"
node1.link = node1 

node2 = Node()
node2.data = "신군"
node1.link = node2 
node2.link = node1

node3 = Node()
node3.data = "엔코신군"
node2.link = node3 
node3.link = node1 

node4 = Node()
node4.data = "챌"
node3.link = node4 
node4.link = node1 

node5 = Node()
node5.data = "김실버"
node4.link = node5 
node5.link = node1 

current = node1 
print(current.data, end = ' ')
while current.link != node1 :
    current = current.link 
    print(current.data, end = ' ')
#--------------------------------------------------
# 중간 노드 삽입 구현
#--------------------------------------------------
newNode = Node()
newNode.data = "재남"
newNode.link = node2.link 
node2.link = newNode 
#---------------------------------------------------

# 원형 연결 리스트의 생성 함수
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

memory = []
head, current, pre = None, None, None
dataArray = ["엔코", "신군", "엔코신군", "챌", "김실버"]

# main
if __name__ == "__main__" :

    node = Node()
    node.data = dataArray[0] 
    head = node 
    node.link = head 
    memory.append(node)

    for data in dataArray[1:] :
        pre = node 
        node = Node() 
        node.data = data  
        pre.link = node 
        node.link = head 
        memory.append(node)

    printNodes(head)
#--------------------------------------------------------------

# 노드 삽입 함수의 완성(맨 앞, 중간, 끝)
class Node() :
    def __init__ (self) :
        self.data =None 
        se;f.link = None 

def printNondes(start) :
    current = start 
    if current.link == None :
        return 
    print(current.data, end = ' ')
    while current.link != start :
        current = current.link 
        print(current.data, end = ' ')
    print()

def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData :
        node = Node() 
        node.data = insertData 
        node.link = head 
        last = head 
        while last.link != head :
            last = last.link 
        last.link = node 
        head = node 
        return 

    current = head 
    while current.link != head :
        pre = current 
        current = current.link 
        if current.data == findData :
            node = Node()
            node.data = insertData 
            node.link = current 
            pre.link = node 
            return 
    
    node = Node()
    node.data = insertData
    current.link = node 
    node.link = head 

    memory = [] 
    head, current, pre = None, None, None 
    dataArray = ['엔코', '신군', '엔코신군', '챌', '김실버']

# main code 
if __name__ == "__main__" :
    node = Node()
    node.data = dataArray[0] 
    head = node 
    node.link = head 
    memory.append(node)

    for data in dataArray[1:] :
        pre = node 
        node = Node() 
        node.data = data  
        pre.link = node 
        node.link = head 
        memory.append(node)

    printNodes(head)

    insertNode("엔코", "엔코pre")
    printNodes(head)

    insertNode("챌", "챌pre")
    printNodes(head)
    
    insertNode("notData", "김실버")
    printNodes(head)
#---------------------------------------------------