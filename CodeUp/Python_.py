# 이코테 Python

# # 시간복잡도가 궁금할때 주로 사용하는 코드이다.
# import time 
# start_time = time.time() # 측정 시작 

# # 프로그램 소스코드
# end_time = time.time() # 측정 종료
# print("time :", end_time - start_time) # 수행시간 출력 

# 선택 정렬과 기본 정렬 라이브러리의 수행시간 비교
from random import randint 
import time 

# 배열에 10,000 개의 정수를 삽입 
array = [] 
for _ in range(10000) :
    array.append(randint(1, 100)) # 1 부터 100 사이의 랜덤한 정수 

# 선택 정렬 프로그램 성능 측정 
start_time = time.time() 

# 선택정렬 프로그램 소스코드 
for i in range(len(array)) :
    min.index = i # 가장 작은 원소의 인덱스 
    for j in range(i+1, len(array)) :
        if array[min_index] > array[j] :
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]  # 스와프 

end_time = time.time()  # 측정 종료 
print("선택 정렬 성능 측정 : ", end_time - start_time)  # 수행시간 출력

# 배열을 다시 무작위 데이터로 초기화
array = [] 
for _ in range(10000) :
    array.append(randint(1, 100)) # 1부터 100 사이의 정수 

# 기본 정렬 라이브러리 성능 측정 
start_time = time.time() 

# 기본 정렬 라이브러리 사용
array.sort() 

end_time = time.time() # 측정 종료
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time) # 수행 시간 출력 

# ----------------------------------------------

# 배열 정렬
# arr = [9, 2, 3, 4, 5]
# temp = 0 
# for i in arr :
#     if arr[i] > arr[i+1] :
#         temp = arr[i]
#         arr[i] = arr[i+1]
#         arr[i+1] = temp 
#     else :

         
