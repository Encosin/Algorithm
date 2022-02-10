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

# 재귀호출의 응용
'''
1) 회문 판단하기 
: 우선 회문은 앞에서 읽든 뒤에서 읽든 동일한 단어나 문장을 의미한다. 앞에도 뒤에도 이효리~ 
특히나 대소문자 구분, 띄어쓰기 구분을 제외하면 의외로 정말 많은 예시가 있다. 

회문을 확인하는 코드를 구현해보자.
p.380 Code10-11 회문 여부 구별

def paintedrome(pSrt) :
    if len(pStr) <= 1 :
        return True

    if pStr[0] != pStr[-1] :
        return False 

    return palindrome(pStr[1:len(pStr)-1])

strAry = ["reaver", "kayak", "Borrow or rob", "주유소의 소유주", "야 너 이번 주 주번이 너야", "살금 살금"]

for testStr in strAry :
    print(testStr, end = '-->')
    testStr = trstStr.lower().replace(' ', '')
    if palindrome(testStr) :
        print('0')
    else :
        print('x')
#--------------------------------------
2) 프랙탈 그리기
: 프랙탈은 작은 조각이 전체와 비슷한 기하학적인 형태를 의미하는데, 이런 특징을 자기유사성 이라고 한다.
프랙탈은 수학적 도형으로도 구현할 수 있는데, 삼각형, 사각형 원등의 구조를 자기 복제 형태로 반복해서 구성하기도 한다.
도형을 그릴 때는 GUI 형식의 화면 출력이 필요하다. Python은 thinter 라는 라이브러리를 제공하고 있다.

Code10-12 간단한 원을 그리는 GUI 프로그래밍
from tkinter import *  # GUI 프로그래밍에 필수인 tkinter을 사용

window = Tk()  # 윈도우창 생성
canvas = Canvas(window, height = 1000, width = 1000, bg ='white')  # 선, 원 등을 그리고자 캔버스(=도화지)를 생성한다. 
# 매개변수 window는 윈도 창에 캔버스를 출력한다, height, width는 캔버스의 높이, 폭 이다. bg(back ground)로 배경색을 지정
canvas.pick()

# cx와 cy는 원을 그리기 위한 중심점
cx = 1000//2
cy = 1000//2
r = 400
canvas.create_oval(cx-r, cy-r, cx+r, cy+r, width=2, outline="red")

window.mainloop()  # 화면 출력
#-------------------------------------------

P384 code10-13 3단계의 프랙탈 원 그리기

from tkinter import *

def drawCircle(x, y, r) :
    global count 
    count += 1
    canvas.create_oval(x-r, y-r, x+r, y+r)
    canvas.create_text(x,y-r, text = str(count), font = ('', 30))
    if r >= radius/2 :
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)

count = 0
wSize = 1000
radius = 400

window = Tk()
canvas = Canvas(window, height=wSize, width=wSize, bg='white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()
#------------------------------------------------------
code10-14 전체 프랙탈 원 그리기

from tkinter import *
import random

def drawCircle(x, y, r) :
    canvas.create_oval(x-r, y-r, x+r, y+r, width=2, outline=random.choice(colors))
    if r >= 5 :
        drawCircle(x-r//2, y, r//2)
        drawCircle(x+r//2, y, r//2)

colors = ["red", "green", "blue", "black", "orange", "indigo", "violet"]
wSize = 1000
radius = 400

window = Tk()
window.title("원 모양의 프랙탈")
canvas = Canvas(window, height=wSize, bg = 'white')

drawCircle(wSize//2, wSize//2, radius)

canvas.pack()
window.mainloop()
'''







