def fib(num):
    l = [0]*(num+1)
    l[0] = 0
    l[1] = 1
    for i in range(2,num+1):
        l[i] = l[i-1]+l[i-2]
    print(l[num])
fib(7)