
def merge(arr,low,mid,high):
    n1 = mid - low + 1
    n2 = high - mid
    l = [0]*n1
    r = [0]*n2
    for i in range(n1):
        l[i] = arr[low+i]
    for j in range(n2):
        r[j] = arr[mid+1+j]
    i = j = 0
    k = low
    while i< n1 and j < n2:
        if l[i] < r[j]:
            arr[k] = l[i]
            i+=1
        else:
            arr[k] = r[j]
            j+=1
        k+=1
    while i < n1:
        arr[k] = l[i]
        i+=1
        k+=1
    while j < n2:
        arr[k] = r[j]
        j+=1
        k+=1

def merge_sort(arr, low, high):
    if low < high:
        mid = (low+high)//2
        merge_sort(arr,low,mid)
        merge_sort(arr,mid+1,high)
        merge(arr,low,mid,high)

def print_array(arr):
    print("sorted array:",end=' ')
    for i in range(len(arr)):
        print(arr[i],end=' ')

arr = [10,6,2,4,1,3,7,9,8,0,5]
n = len(arr)
merge_sort(arr, 0, n-1)
print_array(arr)