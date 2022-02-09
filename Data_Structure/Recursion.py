# 재귀 알고리즘이란 무엇인가??
# : 동일한 작동을 무한적으로 반복하는 알고리즘을 의미한다. 
# 예시로 마트료시카라는 큰 인형 안에 작은 인형이 계속 들어있는 것을 생각할 수 있다.

'''
그렇다면 재귀 호출은 무엇인가?? 
: Recursion(재귀 호출)은 자신을 다시 호출하는 것이다. 
마치 강아지가 자신의 꼬리를 물기 위해서 빙글빙글 도는 것과 같이 묘사할 수 있겠다. (동일한 작동을 무한적으로 반복한다는 뜻이다.)
이를 코드로 구현하면 다음과 같다.

P.364 Code10-01.py 재귀 호출 함수 기본

def openBox() :
    print("종이 상자를 엽니다. ^^")
    openBox()

openBox()   # 처음 함수를 다시 호출

Python 에서는 이런식의 무한반복은 지원하지 않으므로 금방 종료되지만, 실제로 이런식으로 무한반복할 일이 거의 없다.
그래서 이걸 10번 정도 반복하고 다시 돌아가는 코드를 구성하면, 
P 366 Code 10-02 재귀 호출 함수 기본(반환 조건 추가)
def openBox() :
    global count # 전역함수 count
    print("종이 상자를 엽니다. ^^ ")
    count -= 1
    if count == 0 :
        print("반지를 넣고 반환합니다.")
        return 
    
    openBox()
    print("종이 상자를 닫습니다. ^^")

count = 10  # 여기서 count의 의미는 종이상자의 겹수를 의미한다. 즉 10겹의 상자에서 꺼내는 동작을 계속 실행한 것이다.
openBox()  # 처음 함수를 다시 호출
'''

''' 
-재귀 호출 작동 방식의 이해-
: 이것은 예시로 이해하는게 빠르다. 우리는 주로 1부터 10까지의 합계를 해결할 때, 주로 반복문을 사용했지만, 이는 재귀호출을 이용하여 해결할 수도 있다.

# 1~10까지 반복문을 이용한 합계
sum = 0
for m in range(10, 0, -1) :
    sum += m
print(sum)
#-----------------------------

# 1~10까지 재귀함수를 이용한 합계
def addNumber(num) :
    if num <= 1 :
        return 1
    return num + addNumber(num-1)
print(addNumber(10))
#-------------------------------
'''

'''
-팩토리얼(!) 구하기-
: 팩토리얼은 확률과 통계에서 나왔던 ! 하나의 주르륵 나오는 그것이다. 이 팩토리얼도 재귀함수를 통해 구현할 수 있다.

# 반복문을 이용한 팩토리얼 구현
factValue = 1  # 곱셈이므로 초깃값을 1로 설정한다.
for n in range(10, 0, -1) :
    factValue *= n
print("10*9*....*1 = ", factValue)
#---------------------------------

# 재귀함수를 이용한 구현
def factorial(num) :
    if num <= 1 :
        return 1 
    return num * factorial(num-1)

print('\n10! = ', factorial(10))
'''

# 재귀호출의 연습
'''
1) 우주선 발사 카운트 다운
def countDown(n) :
    if n == 0 :
        print('발사!')
    else :
        print(n)
        countDown(n-1)

countDown(5)

2) 별 모양 출력하기
def printStar(n) :
    if n > 0 :
        printStar(n-1)
        print('*' * n)

printStar(5)

3) 구구단 출력 
def gugu(dan, num) :
    print("%d X %d = %d", dan, num, dan*num)
    if num < 9 :
        gugu(dan, num+1)

for dan in range(2, 10) :
    print("##%d단 ##" % dan)
    gugu(dan, 1)

4) N 제곱 계산하기
tab = ' '
def pow(x, n) :
    global tab
    tab += ' '
    if n == 0 :
        return 1
    print(tab + "%d*%d^(%d-%d)" % (x, x, n, 1))
    return x * pow(x, n-1)

print('2^4')
print('답-->', pow(2, 4))

5) 배열의 합 계산하기 
import random

def arySum(arr, n) :
    if n <= 0 :
        return arr[0]
    return arySum(arr, n-1) + arr[n]

ary = [random.randint(0, 255) for _ in range
       (random.randint(10, 20))]
print(ary)
print('배열 합계 --> ', arySum(ary, len(ary)-1))

6) 피보나치 수
: 피보나치 수는 첫번째는 0, 두번째는 1이며, 그 이후는 앞 두 숫자의 합계인 수열이다. 이를 재귀함수를 이용해 작성해 보자

def fibo(n) :
    if n == 0 :
        return 0
    elif n == 1:
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

print('피보나치 수 -> 0 1 ', end = ' ')
for i in range(2, 20) :
    print(fibo(i), end = ' ')
'''