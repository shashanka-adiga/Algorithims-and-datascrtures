def indexes(arr, elem):
    n = len(arr) - 1
    first_pos = - 1
    low = 0
    high = n-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] >= elem:
            first_pos = mid
            high = mid -1
        else:
            low = mid + 1
    if first_pos == -1:
        return [-1,-1]
    low = 0
    high = n-1
    last_pos = 0
    while low <= high:
        mid = (low+high)//2
        if arr[mid] <= elem:
            last_pos = mid
            low = mid + 1
        else:
            high = mid - 1
    return [first_pos, last_pos-1]

arr = [2,4,5,8,8,8,10,20]
elem = 8
print(indexes(arr, elem))






# def indexes(arr, elem):
#     count = 0
#     n = len(arr)
#     for i in range(n):
#         if arr[i] == elem:
#             count+=1
#     if count < 2:
#         print("no such element exist")
#         quit()
#     for i in range(n):
#         if arr[i] == elem:
#             print("first index:",i)
#             print("last index:", i+count-1)
#             break