# 구현 
# 사실 구현은 알고리즘 기법이 아니지만 따로 연습해두는게 좋다고 생각한다.

'''
상하좌우 벡터를 이용해서 위치까지 이동하는 알고리즘을 구현한다.

'''
# N 입력받기
n = int(input())
x,y = 1, 1
plans = input().split() 

# Left, Right, Up, Down 
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']





'''
시각 
입력 조건 : 첫째 줄에 정수 N이 입력된다.(0 <= N <= 23)
출력 조건 : 00시 00분 00초부터 N시 59분 59초 까지의 모든 시각 중에서 3이 하나라도
포함되는 모든 경우의 수를 출력합니다.

해결 : 
* 이 문제는 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제입니다.
* 하루는 86,400초이므로, 00시 00분 00초부터 23시 59분 59초 까지의 모든 경우는
  24 * 60 * 60 = 86,400
* 따라서 단순히 시각을 1씩 증가시키면서 3이 하나라도 포함되어 있는지를 확인하면 됩니다.
* 이러한 유형은 완전탐색 문제 유형이라고 불립니다.

'''

# H 입력 받기
h = int(input())

count = 0 
for i in range(h+1) :
    for j in range(60) :
        for k in range(60) :
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 증가
            if '3' in str(i) + str(j) + str(k) :
                count += 1 

print(count)


# <문제> 왕실 나이트

# 현재 나이트의 위치 입력받기
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

# 나이트가 이동할 수 있는 8가지 방향 정의
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2)]