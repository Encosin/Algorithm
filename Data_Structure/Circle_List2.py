# 원형 연결리스트를 응용해보고자 한다.
# 우선 원형 연결리스트는 시작을 head로 했다가, 다시 돌아오는 끝맺음도 head로 하는데, 이는 마치 물리학적에서 일이 0 인 것, 또는 스칼라가 0인 것에 속한다.
# 잡소리는 빼고...
# 원을 한번 돌고, 숫자가 홀수이면 -를 붙이고 짝수이면 양수 그대로 두는 그런 코드를 구현해보고자 한다.
#-----------------------------------------------------------------------------------------------------
# # 입력할 데이터를 랜덤하게 7개 발생시켜 dataArray 배열에 저장한다.
# dataArray = []
# for _ in range(7) :
#     dataArray.append(random.randint(1, 100))


# # 데이터를 차례대로 가져와 원형 연결리스트를 만든다. 다음과 같은 원형 연결리스트가 만들어질 수 있다. 
# node = Node()
# node.data = dataArray[0]
# head = node 
# node.link = head 
# memory.append(node)

# for data in dataArray[1:] :
#     pre = node 
#     node = Node()
#     ode.data = data 
#     pre.link = node 
#     node.link = head 
#     memory.append(node)

# # 원형 연결리스트 전체를 1회 방문하면서 홀수와 짝수의 개수를 센다.
# current = head 
# while True :
#     if current.data == evenNum : # 참고로 enenNum은 짝수, oddNum은 홀수다.
#         evenNum += 1
#     else :
#         oddNum += 1
#     if current.link == head :
#         break;
#     current = current.link 

# # 짝수 또는 홀수의 개수 중 많은 쪽 숫자를 음수로 만든다.
# if oddNum > evenNum :
#     reminder = 1 # reminder는 나머지
# else :
#     reminder = 0

# current = head 
# while True :
#     if current.data % 2 == rest :
#         current.data *= 1
#     if current.link == head :
#         break;
#     current = current.link 
#----------------------------------------------------------------------------------------
# 여기까지 각 기능별 순차적 구현방식이었다.

# 이를 하나로 완성하면
#--------------------------------------------------------------
import random 

class Node() :
    def __init__ (self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start 
    if current.link == None :
        return 
    print(current.data, end = ' ')
    while current.link != start :
        current = current.link 
        print(current.data, end = ' ')
        print()

def countOddEven() :
    global memory, head, current, pre

    odd, even = 0, 0

    if head == None :
        return False

    current = head 
    while True:
        if current.data % 2 == 0:
            even += 1
        else :
            odd += 1 
        if current.link == head :
            break;
        current = current.link 
    return odd, even 

def makeZeroNumber(odd, even) :
    if odd > even :
        reminder = 1
    else :
        reminder = 0

    current = head
    while True :
        if current.data % 2 == reminder :
            current.data *= -1 
        if current.link == head :
            break; 
        current = current.link 

memory = []
head, current, pre = None, None, None 

if __name__ == "__main__" :
    dataArray = []
    for _ in range(7) :
        dataArray.append(random.radint(1, 100))
    
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

    oddCount, evenCount = countOddEven()
    print('홀수 ->', oddCount, '\t', '짝수 ->' evenCount)

    makeZeroNumber(oddCount, evenCount)
    printNodes(head)

#------------------------------------------------------------------







