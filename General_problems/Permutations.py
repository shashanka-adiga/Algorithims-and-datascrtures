def permutations(arr, left, right, l):
    if left == right:
        if arr not in l:
            print(arr, end=' ')
            l.append(arr)
    else:
        for i in range(left, right+1):
            swapped = swap(list(arr), left, i)
            permutations(swapped, left+1, right, l)

def swap(arr, left, i):
    temp = arr[left]
    arr[left] = arr[i]
    arr[i] = temp
    return ''.join(arr)

arr = "ABCDE"
n = len(arr)
l = []
permutations(arr, 0, n-1, l)

