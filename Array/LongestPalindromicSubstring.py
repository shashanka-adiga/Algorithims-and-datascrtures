# def is_palindrome(arr):
#    i = 0
#    n = len(arr)
#    while i < (n-1-i):
#        if arr[i] != arr[n-i-1]:
#             return False
#        i+=1
#    return True
#
# def lps(arr):
#     longest_string = [None]
#     n = len(arr)
#     max_length = 1
#     length = 0
#     for i in range(n):
#         for j in range(i,n):
#             if is_palindrome(arr[i:(j+1)]):
#                 length = j-i+1
#             if length > max_length:
#                 max_length = length
#                 longest_string = "from index" + " " + str(i)+" "+ "to" +" " + str(j) + " " +str(arr[i:(j+1)])
#     print(longest_string)
#     return max_length
#
# arr = "kjlabcxcbakj"
# print("longest palindromic substring:",end=' ')
# print("length:",lps(list(arr)))


def lps(arr):
    max_val1 = 1
    max_val2 = 1
    n = len(arr)
    str1 = [None]
    str2 = [None]
    for k in range(0,n):
        i = k
        j = k + 1
        cur_len1 = 0
        while i >= 0 and j < n:
            if arr[i] == arr[j]:
                cur_len1 = j-i+1
            else:
                break
            if cur_len1 >= max_val1:
                max_val1 = cur_len1
                str1[0] = arr[i:(j+1)]
            i -= 1
            j += 1

        l = k
        m = k
        cur_len2 = 0
        while l >= 0 and m < n:
            if arr[l] == arr[m]:
                cur_len2 = m-l+1
            else:
                break
            if cur_len2 >= max_val2:
                max_val2 = cur_len2
                str2 = arr[l:(m+1)]
            l -= 1
            m += 1
    if max_val1 > max_val2:
        return str1
    else:
        return str2


print("longest common sub string",end=' : ')
arr = "dsknjcnjncdcunajncebjbabdjbdvjbdj"
print(lps(arr))

