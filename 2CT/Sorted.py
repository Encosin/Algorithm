'''
Sorted 
: Data를 특정한 기준에 따라서 순서대로 나열하는 것
 사실 정렬 알고리즘의 종류는 되게 다양하다. 여기선 주로 사용하는 삽입, 퀵, 계수만 설명하고자 한다.
'''

# 선택 정렬 
"""
puppy = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# a = int(input())
for i in range(len(puppy)):
    min_puppy = i  # 가장 작은 원소의 인덱스
    for j in range(i+1, len(puppy)):
        if puppy[min_puppy] > puppy[j]:
            min_puppy = j
            
    puppy[i], puppy[min_puppy] = puppy[min_puppy], puppy[i]  # 스와프 
    
print(puppy) 
"""


# what's the "swap" ??
# : 스와프란  특정한 리스트가 주어졌을때, 두 변수의 위치를 변경하는 작업을 의미한다. 파이썬에서만 있나보다..
"""
Python version 
--------------------
poodle = [3, 5]
poodle[0], poodle[1] = poodle[1], poodle[0] 
print(poodle)

------------------------------------------------------
C version : 책에 써있어서 써봤다... 주석풀기 금지 ^^ 
------------------------
int a = 3;
int b = 5; 

// 스와핑 진행
int temp = a;
a = b;
b = temp;
"""

'''
# 삽입정렬
: 선택정렬에 비해 구현 난이도가 높지만, 성능이 더 뛰어나다.
 삽입정렬은 특정한 Data를 적절한 위치에 '삽입' 한다는 의미다.
 삽입정렬은 두번째부터 시작한다. why? : 첫번째 데이터는 그 자체로 이미 정렬되어 있다고 보기 때문이다.
'''
# ---------------------------------------------
"""
puppy = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(puppy)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if puppy[j] < puppy[j-1]: # 한 칸씩 왼쪽으로 이동
            puppy[j], puppy[j-1] = puppy[j-1], puppy[j] 
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break 
        
print(puppy)
"""

# 삽입정렬은 거의 정렬되어 있는 상태에서는 진짜 속도가 개빠르다...
 
'''
# 퀵정렬
: 지금까지 배운 알고리즘 중에 가장 많이 사용되는 알고리즘, 
 퀵정렬에서는 '피벗' 이 사용된다.  what's the 피벗? : 큰 숫자와 작은 숫자를 교환할 때, 교환하기 위한 기준을 피벗이라고 한다.
 
'''
# ---------------------------
# 6-4.py 퀵정렬 소스코드
"""
puppy = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(puppy, start, end):
    if start >= end: # 원소가 1개인 경우 종료 
        return 
    pivot = start # 피벗은 첫번째 장소 
    left = start + 1
    right = end
    while left <= right :
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while left <= end and puppy[left] <= puppy[pivot]:
            left += 1 
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right >  start and puppy[right] >= puppy[pivot]:
            right -= 1
        if left > right: # 엇갈려다면 작은 데이터의 피벗을 교체 
            puppy[right], puppy[pivot] = puppy[pivot], puppy[right]
        else: 
            puppy[left], puppy[right] = puppy[right], puppy[left]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 
    quick_sort(puppy, start, right-1)
    quick_sort(puppy, right+1, end)
    
quick_sort(puppy, 0, len(puppy)-1)
print(puppy)     
"""

'''
 이는 파이썬의 장점을 살려 짧게 작성한 퀵 정렬 소스코드이다. 전통 퀵정렬의 분할 방식과는 조금 다른데,
 피벗과 데이터를 비교하는 비교 연산 횟수가 증가하므로 시간 면에서는 조금 비효율적이다. 하지만 더 직관적이고 기억하기 쉽다는 장점이 있다.
 '''
#-----------------------------------------------------
# 6-5.py 파이썬의 장점을 살린 퀵 정렬 소스코드
"""
poodle = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(poodle):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료 
    if len(poodle) <= 1:
        return poodle
    
    pivot = poodle[0]  # 피벗은 첫번째 원소
    tail = poodle[1:]  # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for i in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(poodle))
"""

'''
퀵정렬의 시간복잡도에 대해서 알아보겠다. 삽입정렬과 선택정렬 모두 시간복잡도는 O(N^2)이다.
하지만 이는 최악의 경우에도 O(N^2)을 보장한다. 
퀵 정렬의 평균 시간복잡도는 O(NlogN)이다. 두 정렬 알고리즘보다 매우 빠른편이다.
퀵 정렬에서 최선의 경우를 생각해보자. 피벗값의 위치가 변경되어 분할이 일어날 때마다 
정확히 왼쪽 리스트와 오른쪽 리스트를 절반씩 분할한다면 어떨까? 
Data의 개수가 8개라고 가정하고 다음과 같이 정확히 절반씩 나눈다고 도식화 해보면, 
이때 '높이'를 확인해보면 Data의 개수가 N개일 때 높이는 약 logN 이라고 판단할 수 있다. 
 다시 말해 분할이 이루어지는 횟수가 기하급수적으로 감소하게 되는 것이다. 
 일반적으로 CS에서 log의 의미는 밑이 2인 로그를 의미한다. log(밑이 2인)N
 이는 Data의 개수가 많을수록 차이가 더 극명하게 드러나는데, 
 Data의 개수가 많을수록 퀵정렬은 선택정렬, 삽입정렬에 비해 압도적으로 빠르게 동작하리라고 추측할 수 있다. 
'''
#-----------------------------------
'''
계수 정렬 Algorithm은 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 Algorithm이다.
모든 Data가 양의 정수인 상황을 가정해보자. Data의 개수가 N, Data 중 최댓값이 K일 때, 
계수 정렬은 최악의 경우에도 수행시간 O(N+K)를 보장한다. 
이처럼 매우 빠르게 동작할 뿐만 아니라 원리 또한 간단하다. 
다만, 계수 정렬은 "데이터의 크기 범위가 제한되어 정수로 표현할 수 있을 때" 만 사용가능하다.
ex) 0 이상 100 이하인 성적 데이터를 정렬할 때
단, 가장 큰 Data와 가장 작은 값의 차이가 너무 커도 사용할 수 없다.
'''

"""6-6.py 계수 정렬의 소스코드
# 모든 원소의 값이 0보다 크거나 같다고 가정
poodle = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(poodle)):
    count[poodle[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가 
    
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인 
    for j in range(count[i]):
        print(i, end=' ')  # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력 
        
"""

'''계수정렬의 시간복잡도
: O(N+K)이다.
'''

# 사실 sorted는 이미 라이브러리가 따로 있다. 즉 코딩테스트에서는 외워서 잘 풀어낼 수 있으면 된다. 
# 사용법 : sorted()

# 1. list 
"""
poodle = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

# 1. 
result = sorted(poodle)
print(result)
# 
# 2. 리스트 변수가 하나 있을 때 내부 원소를 바로 정렬할 수도 있다. 리스트 객체의 내장함수인 sort를 이용하는 것인데, 
#    이를 이용하면 별도의 정렬된 리스트가 반환되지 않고, 내부 원소가 바로 정렬된다.
poodle.sort() 
print(poodle)
"""

# 2. sorted() 나 sort()를 이용할 땐 key 매개변수를 입력으로 받을 수 있다. 다음은 tuple로 구성될때의 소스코드이다.
"""
poodle2 = [('바나나', 2), ('사과', 5), ('당근', 3)]
def setting(data):
    return data[1]
result = sorted(poodle2, key=setting)
print(result) 
"""

'''그렇다면 라이브러리를 사용할때에 시간복잡도는 어떻게 될까?
우선 라이브러리를 사용하면 최악의 경우에도 O(NlogN)이 보장된다. 
이 라이브러리는 정교하게 잘 설계되어 있어서 우리가 직접 구현하는 것보다 훨씬 나은 퍼포먼스를 보여준다.
그러므로 문제에서 별도로 구현하라고 하지 않는 이상 라이브러리를 애용하도록 하자. 
코테에서 정렬 알고리즘이 사용되는 경우는 3가지다.
1. 정렬 라이브러리로 풀 수 있는 문제 : 단순히 정렬 기법을 알고 있는지 물어보는 문제로 기본 정렬 라이브러리의 사용 방법을 숙지하고 있으면 어렵지 않게 풀 수 있다.
2. 정렬 알고리즘의 원리에 대해서 물어보는 문제 : 선택 정렬, 삽입 정렬, 퀵 정렬 등의 원리를 잘 알고 있어야 문제를 풀 수 있다.
3. 더 빠른 정렬이 필요한 문제  : 퀵 정렬 기반의 정렬 기법으로는 풀 수 없으며 계수 정렬 등의 다른 정렬 알고리즘을 이용하거나 문제에서 기존에 알려진
알고리즘의 구조적인 개선을 거쳐야 풀 수 있다.
'''
