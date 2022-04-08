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
# 퀵정렬 소스코드
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