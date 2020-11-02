#
# def prefix_sum(arr, n, l):
#     summ = 0
#     l[0] = arr[0]
#     for i in range(1, n):
#         l[i] = l[i-1] + arr[i]
#     for val in l:
#         summ = summ + val
#     print(summ)
#
# def array_queries(q, n):
#     li = [0]*(n+1)
#     l = [0]*(n+1)
#     for i in range(q):
#         left = int(input("left index:"))
#         right = int(input("right index:"))
#         li[left]+=1
#         li[right+1]-=1
#     print(li)
#     prefix_sum(li, len(li), l)
#
# array_queries(3, 10)

