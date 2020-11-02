def bubblesort(arr):
    n = len(arr)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                arr[i] , arr[j] = arr[j],arr[i]
    print(arr)
bubblesort(arr)