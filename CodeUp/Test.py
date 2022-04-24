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
 
try:
    import numpy 
    print("Numpy is installed")
except:
    print("Not")