# Que.py까지는 순차큐를 다뤘다. 
# 하지만 실제로 더 많이 사용되는 것은 원형 큐이다.
# 순차큐의 경우 크기가 100,000개인 데이터가 있으면 처음부터 끝까지 99,000 이상을 돌아야 하기 때문에, 시간이 매~~~~~우 오래 걸린다.
# 이러면 오버헤드가 발생하여 상당히 비효율적이다.

# 원형 큐의 원리를 살펴보고 구현을 해보자.

# 초기화
# : 순차 큐처럼 배열을 사용하며 0번 칸 앞쪽이 -1이 아니므로 초깃값 설정에 유의해야 한다.
CircleQue = [None, None, None, None, None]
front = rear = 0
"""
# 빈 큐와 꽉 찬 큐
if (front == rear) :
    Empty

if ((rear+1) % 5 == front) :
    Full

# CircleQue의 데이터 삽입과 호출
    if (Que is Full) :         # Que 가 Full일때,
        return 
rear = (rear+1) % QueSize  # QueSize 는 큐의 크기
que[rear] = "Hampton"      # Que에 Hampton(햄스터)를 삽입


    if (Que is Empty) :
        return
front = (front+1) % QueSize
Data = que[front]
que[front] = None 
"""

# 여태까지 CircleQue의 구현과 개념을 알아보았다. 이제 이것을 종합적으로 사용하는 코드를 살펴보겠다.
def QueFull() :
    global Size, que, front, rear 
    if (rear+1) % Size == front():
        return True 
    else : 
        return False     

def QueEmpty() :
    global Size, que, front, rear
    if (front == rear) :
        return True 
    else :
        return False 

def enQue(data) :
    global Size, que, front, rear
    if(QueFull()) :
        print("Que is Full !!")
        return
    rear = (rear+1) % Size 
    que[rear] = data

def deQue() :
    global Size, que, front, rear
    if(QueEmpty()) :
        print("Que is Empty.")
        return None
    front = (front+1) % Size 
    data = que[front]
    que[front] = None 
    return data 

def peek() :
    global Size, que, front, rear
    if (QueEmpty()) :
        print("Que is Empty")
        return None 
    return que[(front+1) % Size]
    

Size = int(input("Que Size? ==> "))
que = [None for _ in range(Size)]
front = rear = 0

if __name__ == "__main__" :
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while (select != 'X' and select != 'x') :
        if select == 'I' or select == 'i' :
            data = input("입력할 Data --> ")
            enQue(data)
            print("Que status : ", que)
            print("front : ", front, ", rear : ", rear)
        elif select == 'E' or select == 'e' :
            data = input("추출된 Data --> ", data)
            print("Que status : ", que)
            print("front : ", front, ", rear : ", rear)

        elif select == 'V' or select == 'v' :
            data = peek()
            print("확인된 Data ==> ", data)
            print("Que status : ", que)
            print("front : ", front, ", rear : ", rear)

        else :
            print("입력이 잘못됨")

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    print("프로그램 종료!")


#---------------------------------------------------------------------------

# 맛집 대기줄 구현
# : 대기줄에 손님들이 들어온 순서대로 줄을 선다. (Que) 손님이 꽉 차면 더이상 손님을 받지 않고, 
#   대기줄 손님들은 자리가 날때마다, 한칸씩 자리를 당겨서 식당으로 들어간다. 
# 필요한거 : 대기공간 : Wait, 꽉 찬 대기공간 : Full, 식당공간 : res_Q, 꼬리줄 : rear, 머리줄 : front  
def Full() :
    global wait_Q, Res_Q, rear, front
    if (rear == wait_Q - 1) : 
        return True 
    else : 
        return False    

def Wait() :
    global wait_Q, Res_Q, rear, front
    if (front == rear) :
        return True 
    else :
        return False 

def en_Que(data) :
    global wait_Q, Res_Q, rear, front
    if(Full()) :
        print("Que is Full !!")
        return 
    rear += 1
    Res_Q[rear] = data

def de_Que(data) :
    global wait_Q, Res_Q, rear, front
    if (Wait()) :                   # 만약 자리가 났으면?
        print("Que is Empty !!")
        return None                 
    front += 1                      # 한자리를 더해서
    data = Res_Q[front]             # 맨 앞쪽 손님이 식당에 들어간다.
    Res_Q[front] = None             # 손님이 들어가신 빈자리를 None 으로 채우고

    for i in range(front+1, rear+1) :
        Res_Q[i-1] = Res_Q[i]
        Res_Q[i] = None 
    front = -1
    rear -= 1

    return data 

def peek() :
    global wait_Q, Res_Q, rear, front
    if (Wait()) :
        print("Que is Empty")
        return None 
    return Res_Q[front+1]

# 전역변수
wait_Q = 5 
Res_Q = [None for _ in range(wait_Q)]
front = rear = -1
    
if __name__ == "__main__" :
    en_Que('Fuzzy')
    en_Que('Hado')
    en_Que('Hampton')
    en_Que('Dixie')
    en_Que('Hamster')
    print("대기 줄 상태 : ", Res_Q)

    for _ in range(rear + 1) :
        print(de_Que(), '식당에 입장')
        print('대기 줄 상태 : ', Res_Q)

    print("식당 영업 종료!")