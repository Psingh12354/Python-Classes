a=0;b=1
def fibo(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)

    
for i in range(10):
    print(fibo(i))

    
0
1
1
2
3
5
8
13
21
34
