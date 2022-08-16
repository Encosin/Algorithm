n = int(input())
N = n 
cnt = 0

while 1:
    a = N // 10
    b = N % 10
    c = (a+b) % 10
    N = (b*10)+c 
    cnt +=1
    if(N==n):
        break 
    
print(cnt)