def zero_sum_prefix(arr, num):
    summ = 0
    count = 0
    s = list()
    for value in arr:
        summ = summ + value
        if summ == num or (summ-num) in s:
            start = s.index(summ-num) + 1
            end = arr.index(value)
            if start!= end:
                count += 1
                print("subarray exists from",start,"to",end,"values:",arr[start:end+1])
        s.append(summ)
    if count < 1:
        print("subarray does not exist")
    else:
        print(count)

arr = [4,3,6,-2,-4,7]
num = 0
zero_sum_prefix(arr, num)

# def sum_subarray(arr, num):
#     n = len(arr)
#     count = 0
#     for i in range(n-1):
#         summ = arr[i]
#         # if summ == num:
#         #     count+=1
#         #     continue
#         j = i + 1
#         while j < n:
#             summ = summ + arr[j]
#             if summ == num:
#                 print("from",i+1,"to",j+1)
#                 count+=1
#                 break
#             j+=1
#     if count > 0:
#         print("total ways:",count)
#     else:
#         print("no such sum exists")
#
# arr = [x for x in range(1,100001)]
# num = 100001
# sum_subarray(arr, num)
