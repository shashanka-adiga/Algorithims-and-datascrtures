def decToBin(num):
    binaryNum = [0]*32
    i = 0
    while(num>0):
        binaryNum[i] = num % 2
        num = int(num/2)
        i = i + 1
    for j in range(i-1,-1,-1):
        print(binaryNum[j],end='')
decToBin(100)
print('\n')

