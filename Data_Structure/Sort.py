'''
정렬은 간단히 자료들을 일정한 순서대로 나열하는 것이다.
주로 1) 작은 것부터 나열(내림차순), 2) 큰 것부터 나열(오름차순) 등이 있다. 
'''

'''
Selection Sort(선택정렬)
: 선택정렬은 여러 데이터 중에서 가장 작은 값을 뽑는 작동을 반복하여 값을 정렬하는 방식이다.

최솟값을 찾는 방법
: 선택정렬을 구현하려면 가장 작은 값을 찾는 함수가 필요하다. 
1) 배열의 첫 번째 값을 가장 작은 값으로 지정한다.
2) 가장 작은 값으로 지정한 값을 다음 차례의 값과 비교하여 가장 작은 값을 변경하거나 그대로 두는 방법으로 마지막 값까지 비교를 마친 후 가장
   작은 값으로 지정된 값을 가장 작은 값으로 결정한다.

'''
# P.396 Code 11-04 배열에서 최솟값 위치를 찾는 함수
def findMinIdx(ary) :  # 배열에서 가장 작은 값의 위치를 찾아서 반환하는 함수
    minIdx = 0   # 배열의 첫 번째 값을 현재 최솟값 위치로 지정한다.
    for i in range(1, len(ary)) :  # 배열의 두번째 값부터 마지막까지 반복하는 반복문
        if (ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx  # 찾아낸 배열의 최솟값 위치를 변환한다.

testAry = [55, 88, 33, 77]
minPos = findMinIdx(testAry)  # 배열에서 최솟값 위치를 찾고
print('최솟값 -->', testAry[minPos])  # 찾은 최솟값 위치를 반환한다.

# P.398 Code11-02 선택정렬 구현
def findMinIdx(ary) :  # 배열에서 가장 작은 값의 위치를 찾아서 반환하는 함수
    minIdx = 0   # 배열의 첫 번째 값을 현재 최솟값 위치로 지정한다.
    for i in range(1, len(ary)) :  # 배열의 두번째 값부터 마지막까지 반복하는 반복문
        if (ary[minIdx] > ary[i]) :
            minIdx = i
    return minIdx  # 찾아낸 배열의 최솟값 위치를 변환한다.

before = [188, 162, 168, 120, 50, 150, 177, 105]  # 정렬 전 배열
after = []  # 정렬 후 배열

print('정렬 전 --> ', before)
for _ in range(len(before)) :  # 배열 크기만큼 돌아가는 반복문
    minPos = findMinIdx(before)
    after.append(before[minPos])
    del(before[minPos])
print('정렬 후 --> ', after)

# 변수 값 교환
'''
알고리즘 구현 중에 두 변수의 값을 교환해야 하는 경우가 생긴다. 이때는 즉시 교환할 수 없으니 빈공간에 한번 옮겼다가 다시 옮기는 형식으로 사용하는게 좋다.
C언어에서 좋아하는 예로 
temp = A 
A = B
B = temp 
그치만 우리 시간을 아껴주기 위해 Python은 
A, B = B, A 
와 같은 문법도 제공해준다.....
'''

# 개선된 선택 정렬 구현
'''
앞에서 정렬을 사용할때 배열을 정렬 전, 정렬 후 이렇게 두개를 할당해서 사용하였는데, 솔직히 비효율적이다. 
간단히 Data 4개를 정렬해보면, '배열 크기 -1 '회의 Cycle(큰 반복)을 돌리고, 반복되는 변수를 i라하면 3번 돌아가는 것이다.
'''
# P.403 Code11-03 개선된 선택 정렬
def selectionSort(ary) :  # 배열을 전달받아 선택 정렬 방식으로 정렬한 후 반환하는 함수이다.
    n = len(ary)  # 배열 길이를 구해서 n 변수에 대입한다.
    for i in range(0, n-1) :
        minIdx = i  # 각 Cycle의 맨 앞 Data를 최솟값 위치로 일단 지정한다. 가장 작은 값 지정.
        for k in range(i+1, n) :
            if (ary[minIdx] > ary[k]) :
                minIdx = k 
        tmp = ary[i]  # 각 Cycle의 첫 번째 값과 찾은 최솟값을 교환한다.
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp  

    return ary 

dataAry = [188, 162, 168, 120, 50, 150, 177, 185]

print('정렬 전 --> ', dataAry) 
dataAry = selectionSort(dataAry)
print('정렬 후 --> ', dataAry)



# 선택 정렬 성능
'''
우리가 Algorithm과 DataStructure을 배우는 이유는 코드의 성능을 높이기 위해서다. 
정렬에서의 중요한 사항 중 하나는 정렬을 완료하는 비교 횟수다. 큰 Cycle 안에서 비교 후 이동이 몇번 이뤄졌는지가 이것을 의미한다.

i    k       반복 횟수
0    1,2,3   3회
1    2,3     2회
2    3       1회
'''

'''
# 삽입 정렬
: 기존 데이터 중에서 자신의 위치를 찾아 데이터를 삽입하는 정렬 방식을 사용한다.



'''
