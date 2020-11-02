def remove_duplicate(arr):
    rem = []
    for i in arr:
        if i not in rem:
            print(i, end=' ')
            rem.append(i)

arr = "shashanka"
remove_duplicate(list(arr))