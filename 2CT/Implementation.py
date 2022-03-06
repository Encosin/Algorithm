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

# 이동 계획을 하나씩 확인하기
for plan in plans :
    