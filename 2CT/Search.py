# 탐색 Algorithm 다른말로 검색 알고리즘이라고도 한다.
# 실제로 검색 엔진에서는 탐색 알고리즘을 사용한다.

'''순차 탐색
가장 기본적인 탐색 방법,
리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법.
처리 방법 :
1) 초기에 뒤죽박죽 섞여있는 Data 존재.
2) 제일 앞에 있는 데이터 확인, if) 일치 return, elif) 일치x 다음 단어
3) 바로 우측에 있는 데이터 확인 if) 일치 return, elif) 일치x? 다음 데이터.
4) 바로 우측에 있는 데이터 확인 if) 일치 return 
for문에 전체 리스트의 개수를 len()으로 넣고, i로 count해가면서 코드를 짜면 될것같다.
예시)'''

# 순차 탐색 코드
"""
def sequential_search(n, target, array):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if array[i] == target:
            return i+1  # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)
        
print("생성할 원소 개수를 입력한 다음 한칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0])  # 원소의 개수
target = input_data[1]  # 찾고자 하는 문자열 
print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

# 순차 탐색 수행 결과 출력
print(sequential_search(n, target, array))
"""

'''이진탐색? : 반으로 쪼개면서 탐색(단, 정렬이 되어있어야 한다.) 
 : 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 과정
 1) 시작점과 끝점을 확인한 다음 둘 사이에 중간점을 정한다. ? : 중간점이 실수면?.. -> 소수점 이하를 버린다 사실 왼쪽이 오른쪽보다 1정도 많은건 별 문제가 되지 않는다.
 2) 찾으려는 값이 중간점보다 크면 우측을 비교, 중간점보다 작으면 좌측을 비교.
    참고로 비교할때도 또 다시 반을 쪼개본다.
  
시간복잡도 : O(logN)이다. 이는 이진탐색 특성상 한번 확인절차를 거칠때마다 절반씩 줄어들기 때문에 훨씬 빨리 탐색할 수 있다.

'''
# 재귀함수로 구현한 이진탐색
"""
def binary_search(array, target, start, end):
    if start > end:
        return None 
    mid = (start+end) // 2
    # 찾은 경우 중간점 인덱스 변환 
    if array[mid] == target:
        return mid 
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end)
    
# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기 
n, target = list(map(int, input().split()))
# 전체 원소 입력받기 
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
"""



# 이번엔 반복문으로 이진 탐색을 구현해보겠다.
"""
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2 
        
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid 
        
        # 중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인 
        else:
            start = mid + 1
            
    return None 

# n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기 
n, target = list(map(int, input().split()))

# 전체 원소 입력받기 
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력 
result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result+1)
    
"""

# 코드양이 짧아보여도 이진탐색 문제는 쉽지않다. 다른문제와 결합할 가능성도 높고, 
# 아무래도 데이터 양이 2000만을 넘어가면 이진탐색을 들이대볼 것을 권한다.

'''트리 자료구조 
이진탐색은 전제 조건이 데이터 정렬이다. Database는 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를
이용하여 항상 데이터가 정렬되어 있다. 
1) 트리는 부모 노드와 자식 노드의 관계로 표현된다.
2) 트리의 최상단 노드를 루트 노드라고 한다.
3) 트리의 최하단 노드를 단말 노드라고 한다.
4) 트리에서 일부를 떼어내도 트리구조이며 이를 서브 트리라 한다.
5) 트리는 파일 시스템과 같이 계층적이고 정렬된 데이터를 다루기에 적합하다. '''

'''이진 탐색 트리
트리 자료구조 중에서 가장 간단한 형태가 이진 탐색 트리이다. 
이는 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조이다. 
1) 부모 노드보다 왼쪽 자식 노드가 작다.
2) 부모 노드보다 오른쪽 자식 노드가 크다.
왼쪽 자식노드 < 부모노드 < 오른쪽 자식노드

Data가 1000만개를 넘어가거나 탐색범위의 크기가 1000억 이상이라면 이진탐색 알고리즘 말고
sys 라이브러리의 readline()함수를 이용하는게 좋다.
'''

# 한 줄 입력받아 출력
"""
import sys 
# 하나의 문자열 데이터 입력받기 
input_data = sys.stdin.readline().rstrip() 

# 입력받은 문자열 그대로 출력 
print(input_data)
"""



# 실전문제 : 부품 찾기
'''동빈이네 전자매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다. 어느날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다. 이때 가게 안에 부품이 모두 있는지 확인하는 프로그램을 작성해보자.
Ex) N=5 [8, 3, 7, 9, 2]  
N은 가게의 부품의 수, 옆에 list는 가게에 있는 부품의 번호
    M=3 [5, 7, 9] 
M은 손님이 찾는 부품의 개수, 옆 list는 필요한 부품의 번호
가게의 list 안에 손님이 요청한 list가 포함된다면 => Yes를 출력, 포함되지 않는다면 No를 출력
'''

'''해설
1) 이진탐색 알고리즘 
: 먼저 N개의 부품을 번호를 기준으로 정렬, 그 이후에 M개의 찾고자 하는 부품이 매장에 존재하는지 검사
이렇게하면 최악의 경우에도 시간 복잡도 : O(M*logN) 의 연산이 필요하다. 최대 2만번의 연산
하지만 N개의 부품을 정렬하기 위해서는 O(NxlogN) 이론적으로 약 2000만, 더 많은 연산이 필요하다.
그래서 최종 시간복잡도는 O((M + N) x logN)'''

# p.198 7-5.py 이진탐색 답안 예시
def binary_search(array, target, start, end):
    while start <- end:
        mid = (start + end) // 2
        
        # 찾은 경우 중간점 인덱스 반환 
        if array[mid] == target:
            return mid 
        
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
            
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인 
        else:
            start = mid + 1
            
    return None

# N(가게의 부품 개수) 입력 
n = int(input())

# 가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()  # 이진탐색을 수행하기 위해 사전에 정렬 수행

# M(손님이 확인 요청한 부품 개수) 입력 
m = int(input())

# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

# 손님이 확인 요청한 부품 번호를 하나씩 확인 
for i in x :
    # 해당 부품이 존재하는지 확인 
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end=' ')
    else:
        print('no', end=' ') 
        

