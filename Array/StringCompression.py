
def last_index(arr, elem):
    print(arr)
    count = 0
    n = len(arr)
    for i in range(n):
        if arr[i] == elem:
            count+=1
    if count < 2:
        print("no such element exist")
        quit()
    for i in range(n):
        if arr[i] == elem:
            return  i+count-1


def compressor(string):
    n = len(string)
    look_up = {}
    i = 0
    while i < n:
        lst_idx = last_index(string, string[i])
        look_up[i] = lst_idx-i+1
        i = lst_idx + 1
    print(look_up)


s = "aabbccca"
compressor(list(s))

