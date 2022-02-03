# 자료구조에서 가장 유명한 List, Stack, Que에 대해 배우고 있다.
# List는 배열처럼 순서를 나열하는 자료구조의 일종이고,
# Stack은 비커처럼 Input을 하는 방법에는 여러가지가 있지만, Output에는 꼭 나중에 넣은 것이 먼저 나오는 후입선출 구조였다.
# 그렇다면 여기서 배울 Que는 어떨까? 
# Que는 가장 많이 드는 예시로 보통 음식점에 서는 긴 줄을 빗대어 표현한다. 
# 가장 먼저 줄을 선 사람이 가장 먼저 음식을 맛볼 수 있는 형태가 바로 큐다.
# 큐는 그래서 선입선출 구조를 가지고 있고, 스택과 함께 가장 유용한 자료구조 중 하나다.

# 큐의 공간을 할당해보고 3개 정도 Data를 채워넣어 보겠다.
#---------------------------------------------------------------------------------------
que = [None, None, None, None, None]
front = rear = -1 # front는 맨 처음 들어간 Data를 말하는것이고, rear은 맨 끝머리에 있는 Data를 가리키는 뜻이다.

rear += 1
que[rear] = "엔코"
rear += 1
que[rear] = "신군"
rear += 1
que[rear] = "엔코신군"

print("-----큐 상태--------")
print('[출구] <-- ', end = ' ')
for i in range(0, len(que), 1) :
    print(que[i], end = ' ')
print('<--[입구]')
#-----------------------------------------------------------------------------------------------

# Data 추출할 때 사용하는 deQue

que = ["엔코", "신군", "엔코신군", None, None]
front = -1 # 
rear = 2 # rear에 엔코신군까지 3개의 Data가 저장되어 있으므로, 0, 1, 2 순서대로 할당되어 있는 것이다.

print("-----큐 상태--------")
print('[출구] <-- ', end = ' ')
for i in range(0, len(que), 1) :
    print(que[i], end = ' ')
print('<--[입구]')
print("----------------------")

front += 1
data = que[front]
que[front] = None 
print('deQue --> ', data)

front += 1
data = que[front]
que[front] = None 
print('deQue --> ', data)

front += 1
data = que[front]
que[front] = None 
print('----------------------')

print("-----큐 상태--------")
print('[출구] <-- ', end = ' ')
for i in range(0, len(que), 1) :
    print(que[i], end = ' ')
print('<--[입구]')
#-------------------------------------------------------
# 다음은 Que에 데이터를 삽입하는 법을 구현해보려 한다.
que = [None,None,None,None,None] # 여태까지 이런 식으로 크기를 정해서 할당해왔다. 
# 하지만 실제로는 큐의 값이 무한으로 커야하기 때문에, 하나하나 None을 지정해줋 수 없는 노릇이다.
# 그래서 나온게 SIZE다.
SIZE = 5 
que = [None for _ in range(SIZE)] 
frone = rear = -1
# 이렇게하면 5개의 빈 상태가 완성된다.

# 삽입을 하려면 우선 공간이 꽉 찼는지 확인해줄 필요가 있다. 
# if (rear 값 == 큐 크기-1) :
#     QueFull
#---------------------------------------------------------------------------
def QueFull():
    global size, que, front, rear 
    if (rear == size-1) :
        return True
    else : 
        return False 

size = 5 # Data의 크기를 5만큼 할당
que = ['엔코', '신군', '엔코신군', '챌', '실버'] # Data가 Full인지 확인하기 위해 꽉 채워본다
front = -1
rear = 4

print("큐가 풀인지? ==> ", QueFull)
#-------------------------------------------------------------------------------
# 전 과정에서는 큐가 Full인지 확인했다/
# 이번엔 Que가 Empty인지 확인하는 과정을 보겠다.
def QueEmpty() :
    global size, que, front, rear 
    if (front == rear) :
        return True
    else : 
        return False

size = 5
que = [None for _ in range(size)]
front = rear = -1

print("Que is Empty? -->", QueEmpty)