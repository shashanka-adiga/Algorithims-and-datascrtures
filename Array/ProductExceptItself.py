# without dividing anything

def left(arr, n, l):
    l[0] = 1
    for i in range(1,n):
        l[i] = arr[i-1]*l[i-1]
    return l

def right(arr, n, r):
    r[n-1] = 1
    for i in range(n-2,-1,-1):
        r[i] = arr[i+1]*r[i+1]
    return r


def solution(arr):
    l = [0] * len(arr)
    r = [0] * len(arr)
    output = [0] * len(arr)
    left_arr = left(arr, len(arr), l)
    right_arr = right(arr, len(arr), r)
    k = 0
    for i,j in zip(left_arr,right_arr):
        output[k] = i*j
        k+=1
    return output




arr = [1,2,3,4]
print(solution(arr))




# def solution(arr):
#     output = [0]*len(arr)
#     product = 1
#     for i in arr:
#         product = product*i
#     for j in range(len(arr)):
#         output[j] = product//arr[j]
#     return output




