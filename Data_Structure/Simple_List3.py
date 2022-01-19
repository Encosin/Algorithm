# 3에선 응용 예제를 풀어볼까 한다.

# 1) 사용자가 이름, 이메일 등을 입력하면 순서대로 리스트를 작성해주는 프로그램
# Life is short, You need Python!
# 인생은 짧으니, 파이썬을 쓰자! ㅋㅋㅋㅋㅋ
#--------------------------------------------------------------------------
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

def makeSimpleLinkedList(nameEmail) :
    global memory, head, current, pre 

    node = Node()         # 새 노드를 생성 후
    node.data = nameEmail # 메모리 공간에
    memory.append(node)   # 새 노드를 넣는다

    if head == None : # 첫 번째 노드
        head = node   # 새 노드가 head 라면
        return

    if head.data[1] > nameEmail[1] :  # 새 노드의 Emial이 첫 node의 이메일보다 빠르면
        node.link = head              # 새 노드의 link에 첫 노드 head를 지정하고
        head = node                   # head를 새 node로 지정하고 함수를 종료한다.
        return 

    current = head 
    while current.link != None :
        pre = current 
        current = current.link 

        if current.data[1] > nameEmail[1] :
            pre.limk = node 
            node.link = current 
            return 

    current.link = node 

memory = [] 
head, current, pre = None, None, None 

# 메인 코드 
if __name__ == "__main__" :
    
    while True :
        name = input("이름-> ")
        if name == "" or name == None :
            break 
        email = input("이메일 -> ")
        makeSimpleLinkedList(name,email)
        printNodes(head)
#------------------------------------------------------------------------------------


# 2) 로또 추첨 with Python    
# 이번엔 인생에서 매우 중요한 로또 골라주는 코드를 Python 과 함께 해보려고 한다.
# Life is short, You need Python!! 

# 1~45 중에서 숫자 6개를 뽑는 로또 추첨 프로그램
#------------------------------------------------------------------------------------
import random 

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

def makeLottoList(num) :
    global memory, head, current, pre 

    node = Node()
    node.data = num 
    memory.append(node)
    if head == None :
        head = node 
        return 

    if head.data > num :
        node.link = head  
        head = node 
        return 

    current = head 
    while current.link != None :
        pre = current 
        current = current.link 
        if current.data > num :
            pre.link = node 
            node.link = current 
            return 

    current.link = node 

def findNumber(num) :
    global memory, head, current, pre

    if head == None :
        return False 
    current = head 
    if current.data == num :
        return True 
    while current.link != None :
        current = current.link
        if current.data == num :
            return True 
    return False

memory = []
head, current, pre = None, None, None

# main code
if __name__ == "__main__" :

    lottoCount = 0
    while True :
        lotto = random.rand(1,45)
        if findNumber(lotto) :
            continue
        lottoCount += 1 
        makeLottoList(lotto) 
        if lottoCount >= 6 :
            break 

    printNodes(head)
#-----------------------------------------