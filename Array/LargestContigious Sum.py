def lcs(arr):
    cur_sum = arr[0]
    largest_sum = cur_sum
    for i in range(1, len(arr)):
        cur_sum = max(arr[i], cur_sum + arr[i])
        largest_sum = max(cur_sum, largest_sum)

    return largest_sum


arr = [-1,-2,4,-1,-1,3,-5]
print(lcs(arr))