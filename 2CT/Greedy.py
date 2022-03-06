# 2CT는 이것이 코딩테스트다의 줄임말이다.
'''
Greedy는 탐욕스럽다는 뜻으로 Algorithm 서적에서는 주로 탐욕법이라고 표현한다.
이는 최적의 경로 또는 최단거리 등을 표현하기에 유용하며, 우리가 일상생활에서 문제를 주로 해결할때 가장 자주 사용하는 해결법이기도 하다.
여러 강의들을 찾아본 결과 "거스름돈" 과 관련된 알고리즘이 가장 많이 채택되는 듯 하다.

'''
n = 1260 
count = 0 
# 큰 단위의 화폐부터 차례대로 확인
array = [500, 100, 50, 10]

for coin in array :
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기 
    n %= coin

print(count)
# 여기까지 남은 돈을 최적으로 거슬러주는 방법이 담긴 코드였다면 

# 다음은 1이 될때까지 최소한의 나눔법에 관한 문제다.

# n, k 을 공백을 기준으로 구분하여 입력받기
n, k = map(int, input().split())  
result = 0 
while True : 
    # N이 K로 나누어 떨어지는 수가 될때까지 빼기
    target = (n//k) *k 
    result += (n - target)
    n = target 
    # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k :
        break 
    # k로 나누기 
    result += 1 
    n //= k 

# 마지막으로 남은 수에 대하여 1씩 빼기 
result += (n-1) 
print(result)



'''
# N, M, K 를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split()) # 변수를 한번에 입력할때 칸을 줄여줄수있는 map 

# N개의 수를 공백으로 구분하여 입력받기 
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기 
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두번째로 큰 수

result = 0

while True :
    for i in range(k) : # 가장 큰 수를 k번 더하기
        if m == 0 : # m이 0이라면 반복문 탈출 
            break 
        result += first            
        m -= 1 # 더할 때마다 1씩 빼기

    if m == 0 : # m이 0이라면 반복문 탈출
        break 
    result += second # 두번째로 큰 수를 한 번 더하기 
    m -= 1 # 더할 때마다 1씩 빼기 

print(result) # 최종 답안 출력
'''


# 곱하기 혹은 더하기 
# 문자열에 숫자가 나열되어있으면 순서대로 (우선순위를 적용하지 않고) 계산해나가는 코드를 작성
data = input()

# 첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0]) 
for i in range(1, len(data)) :
    # 두 수 중에서 하나라도 '0' 혹은 '1'인 경우, 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1 :
        result += num 
    else : 
        result *= num 

print(result)
#-----------------------

# 모험가 길드 : 답안 예시
n = int(input())
data = list(map(int(input().split()))) 
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data : # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i : #  현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기 
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
