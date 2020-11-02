def first_non_recc_num(arr):
    arr = list(arr)
    d = {}
    for i in arr:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    for j in arr:
        if d[j] == 1:
            print(j)
            break










# def solution(arr):
#     l = []
#     r = []
#     for i in arr:
#         if i in l:
#             pos = l.index(i)
#             r.append(l.pop(pos))
#         else:
#             if i not in r:
#                 l.append(i)
#     if l:
#         print(l[0])
#     else:
#         print("no such character!")
arr = "abaabcdd"
first_non_recc_num(arr)