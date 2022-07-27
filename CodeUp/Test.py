'''
1. 파이썬 변수와 타입
파이썬은 동적타입이다. 그러므로 변수에 값을 넣으면 알아서 타입이
변경된다.

'''
# a = "hello"
# print("type: ", type(a), "value: ", a)

# type: <class 'str'> value: hello
# import numpy as np
# import pandas as pd 

# myarray = [[1,2,3], [4,5,6], [7,8,9]]
# myarray = np.array(myarray)
# myarray = pd.DataFrame(myarray)
 
# try:
#     import numpy 
#     print("Numpy is installed")
# except:
#     print("Not")

a = int(input())
b = input()
# a는 int로 b는 문자로 입력을 받으려 한다. 
print(a * int(b[-1]), a*int(b[-2]), a*int(b[-3]), sep='\n')
# 참고로 sep은 Python List에서 주로 사용하는 문법으로 각 값들 사이에 

one = int(input())
two = input()
print(one * int(two[-1]), one * int(two[-2]), one * int(two[-3]), one * int(two), sep='\n')