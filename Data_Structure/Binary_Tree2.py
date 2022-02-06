# 보통 응용부터는 2에다 저장한다.

# 이진 탐색트리는 Data를 보관하고 검색할 때, 효율적이다. 
# 예로) 도서관에 새로 입고된 책 정보를 이진 탐색트리에 보관해서 검색할 수 있다. 책 이름과 작가 이름을 각각 이진 탐색트리로 검색한다.
import random 
# bookAry = [['어린왕자', '생떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'], 
# ['신곡', '단테'], ['돈키호테', '세르반테스']]

# bookAry = random.shuffle(bookAry)  # random.shuffle은 배열을 랜덤하게 섞어준다.

class TreeNode() :
    def __init__ (self) :
        self.left = None 
        self.data = None 
        self.right = None 
    
memory = [] 
rootBook, rootAuth = None, None 
bookAry = [['어린왕자', '생떽쥐베리'], ['이방인', '까뮈'], ['부활', '톨스토이'], 
['신곡', '단테'], ['돈키호테', '세르반테스']]

random.shuffle(bookAry)

node = TreeNode()
node.data = bookAry[0][0] 
rootBook = node 
memory.append(node)

for book in bookAry[1:] :
    name = book[0] 
    node = TreeNode()
    node.data = name 

    current = rootBook 
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node 
                break
            current = current.left 
        else :
            if current.right == None :
                current.right = node 
                break 
            current = current.right 

    memory.append(node)

print('책 이름 트리 구성 완료!')

# 작가이름 트리
node = TreeNode()
node.data = bookAry[0][1]
rootAuth = node 
memory.append(node)

for book in bookAry[1:] :
    name = book[1]
    node = TreeNode()
    node.data = name 

    current = rootAuth 
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node 
                break 
            current = current.left 
        else :
            if current.right == None :
                current.right = node 
                break 
            current = current.right 

    memory.append(node)

print('작가 이름 트리 ')

# 책 이름 및 작가 이름 검색
bookOrAuth = int(input('책검색(1), 작가검색(2) --> '))
findName = input('검색할 책 또는 작가 --> ')

if bookOrAuth == 1 :
    root = rootBook 
else :
    root = rootAuth 

current = root 
while True :
    if findName == current.data :
        print(findName, '을(를) 찾음.')
        findYN = True  
        break 
    elif findName < current.data :
        if current.left == None :
            print(findName, '이(가) 목록에 없음')
            break 
        current = current.left 

    else :
        if current.right == None :
            print(findName, '이(가) 목록에 없음')
            break 
        current = current.right 


