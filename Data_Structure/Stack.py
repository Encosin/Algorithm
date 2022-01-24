# 스택은 프링글스 통이라고 생각하면 된다, 후입선출 또는 선입후출 구조다.
# 넣는건 마음대로 할 수 있지만, 뺄때는 가장 위에 있는 것부터 차례대로 빼야한다.
#------------------------------------------------------------------------------
# push
from ctypes.wintypes import SIZE
import turtle


stack = [None, None, None, None, None]
top = -1 # top은 스택에 제일 윗부분을 뜻한다. 그런 top에 -1을 넣는다는 것은 아직 아무것도 들어있지 않다는 뜻이다.

top += 1            # 이러면 top[0] 맨 아랫부분을 가리키고
stack[top] = "커피" # 맨 처음 or 맨 아래칸에 "커피" 를 삽입한다는 뜻이다.

top += 1             # top[1] 아래에서 두번째 칸, list는 0부터 읽기 때문에
stack[top] = '녹차'  # top[1] 즉 두번째 칸에 '녹차' 를 넣는다.

top += 1            # top[2] 아래에서 세번째칸
stack[top] = "꿀물" # top[2] 아래서부터 세번째칸에 "꿀물" 을 넣는다.

print("-----스택 상태-------")
for i in range(len(stack)-1, -1, -1) :
    print(stack[i])

#------------------------------------------------------------------------------------
# pop 
stack = ['커피', '녹차', '꿀물', 'None', 'None']
top = 2

print("-----스택 상태-------")
for i in range(len(stack)-1, -1, -1) :
    print(stack[i])

print("----------------------------")
data = stack[top]
stack[top] = None 
top -= 1
print("pop --> ", data)

data = stack[top]
stack[top] = None 
top -= 1
print("pop --> ", data)

data = stack[top]
stack[top] = None 
top -= 1
print("pop --> ", data)
print("----------------------------")

print("-----------스택상태-----------------")
for i in range(len(stack)-1, -1, -1) :
    print(stack[i])
#-------------------------------------------------------------

# 여태까지는 스택에 하나씩 값을 지정해준 리스트를 사용하였는데, 실제로는 정말 많은 양의 데이터가 필요하기 때문에, 일일이 지정해줄 수가 없다.
# 그래서 우리는 stack의 크기를 한정짓지 않고 크게 만드는 작업을 공부해보자

#------------------------------------------------------
SIZE = 5  # stack 크기
stack = [None for _ in range(SIZE)]
top = -1 
# 여태껏 스택을 세워진 형태로 표현했지만, 실제 코드에서는 누운 상태로 표현한다.

# stack이 꽉 찾는지 확인하려면?
#-----------------------------------------------
def StackFull() :
    global SIZE, stack, top

    if(top >= SIZE-1) :
        return True
    else :
        return False

SIZE = 5
stack = ["스벅", "이디야", "투썸", "뜨아", "아아"]
top = 4

print("Stack is Full?? ==> ", StackFull)
#----------------------------------------------

# Data를 추출해보려 하는데 그 전에 Stack이 비어있는지부터 확인해보려 한다. 
# 만약 stack에 Data가 없는데도 데이터를 추출하려고 하는 시도는 위험할 수 있다.
# if (top == -1) :
#     stack is empty! 

#---------------------------------------
def StackEmpty() :
    global SIZE, stack, top
    if(top == -1) :
        return True
    else :
        return False

SIZE = 5
stack = [None for _ in range(SIZE)]
top -= 1

print("스택이 비었는지 여부 --> ", StackEmpty())
#--------------------------------------------------

# Stack 함수들
def StackFull():
    global SIZE, stack, top
    if(top >= SIZE-1):
        return True
    else:
        return False 

def StackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else :
        return False

def push(data):
    global SIZE, stack, top
    if (StackFull()):
        print("Stack is Full")
        return 
    top += 1
    stack[top] = data

def pop() :
    global SIZE, stack, top
    if(StackEmpty) :
        print('Stack is Empty')
        return None
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek() :
    global SIZE, stack, top
    if(StackEmpty()) :
        print('Stack is Empty')
        return None
    return stack[top]

SIZE = int(input("스택 크기를 입력하세요 ==> "))
stack = [None for _ in range(SIZE)]
top -= 1

if __name__ == "__main__" :
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 --> ")

    while (select != 'x' and select != 'x') :
        if select == 'I' or select == 'i' :
            data = input("입력할 데이터 ==> ")
            push(data)
            print("스택 상태 : ", stack)
        
        elif select == 'E' or select == 'e' :
            data = pop()
            print("추출된 데이터 ==> ", data)
            print("스택 상태 : ", stack)
        
        elif select == 'V' or select == 'v' :
            data = peek()
            print("확인된 데이터 ==> ", data)
            print("스택 상태", stack)
        
        else :
            print("Input Wrong")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 --> ")

    print("End")













