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