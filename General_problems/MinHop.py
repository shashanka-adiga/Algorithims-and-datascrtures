def min_jumps(arr):
    if arr[0] < 1:
        print(" end can not be reached")
        return

    length = len(arr)
    positions = []
    count = 1
    i = 0
    while i < length:
        positions.append(arr[i])
        reach = i + arr[i]
        if reach >= length - 1:
            print("minimum number of jumps:",count,positions)
            return
        pos = maximum(arr,i+1,reach)
        count+=1
        i = pos
    print(" end can not be reached")
    return

def maximum(arr,start,end):
    largest = arr[start]
    for i in range(start+1,end+1):
        if arr[i] > largest:
            largest = arr[i]
    return arr.index(largest)



arr = [1,3,6,3,2,3,6,8,9,5]
min_jumps(arr)

