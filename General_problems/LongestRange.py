def longest_range(arr):
    best_range = []
    longest_length = 0
    nums = {}
    for num in arr:
        nums[num] = True
    for num in nums:
        current_length = 0
        if not nums[num]:
            continue
        nums[num] = False
        current_length = current_length + 1
        left = num-1
        right = num+1
        while left in nums:
            nums[left] = False
            current_length = current_length + 1
            left = left -1
        while right in nums:
            nums[right] = False
            current_length = current_length + 1
            right = right + 1
        if current_length > longest_length:
            longest_length = current_length
            best_range = best_range + [left+1,right-1]
    print("longest range:",best_range[-2],"to",best_range[-1])

arr = [0,1,14,17,2,16,3,15,4,5,9,6]
longest_range(arr)