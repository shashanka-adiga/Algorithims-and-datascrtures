
def partition(arr,low,high):
    pivot = arr[high]
    i = low - 1
    for j in range(low,high):
        if arr[j] <= pivot:
            i+=1
            arr[i],arr[j] = arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i+1

def quicksort(arr, low, high):
    if low < high:
        sorted_pos = partition(arr,low,high)
        quicksort(arr,low,sorted_pos-1)
        quicksort(arr,sorted_pos+1,high)

def print_array(arr):
    print("sorted array:",end=' ')
    for i in range(len(arr)):
        print(arr[i],end=' ')

arr = [7,1,4,3,8,2,6,5,10,9,0]
n = len(arr)
quicksort(arr, 0, n-1)
print_array(arr)





























# def partition(arr, low, high):
#     pivot = arr[high]
#     i = low - 1
#     for j in range(low, high):
#         if arr[j] <= pivot:
#             i+=1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i+1], arr[high] = arr[high], arr[i+1]
#     return i+1
#
# def quick_sort(arr, low, high):
#     if low < high:
#         sorted_pos = partition(arr, low, high)
#         quick_sort(arr, low, sorted_pos-1)
#         quick_sort(arr, sorted_pos+1, high)
#
# arr = [9,4,7,1,3,5,8,6,2]
# quick_sort(arr, 0, len(arr)-1)
# print(arr)