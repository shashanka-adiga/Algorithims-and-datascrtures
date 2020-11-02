# def lcs(str1, str2):
#     m = len(str1)
#     n = len(str2)
#     tab = [[0 for i in range(m+1)] for j in range(n+1)]
#     for col in range(1, n+1):
#         for row in range(1, m+1):
#             if str1[col-1] == str2[row-1]:
#                 tab[col][row] = 1 + tab[col-1][row-1]
#             else:
#                 tab[col][row] = max(tab[col-1][row], tab[col][row-1])
#     print(tab)
#     return tab[m][n]




# using DP
def lcs(x,y):
    m = len(x)
    n = len(y)
    if m<n:
        l = [[None]*(n+1) for i in range(n+1)]
    else:
        l = [[None] * (m+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i ==0 or j==0:
                l[i][j] = 0
            elif x[i-1] == y[j-1]:
                l[i][j] = l[i-1][j-1] + 1
            else:
                l[i][j] = max(l[i][j-1],l[i-1][j])
    print(l[m][n])
#
# x = 'abefg'
# y = 'abegcizpqrs'
# lcs(x,y)



# recursive solution
# def lcs(x,y,m,n):
#     if m <1 or n < 1:
#         return 0
#     if x[m-1]==y[n-1]:
#         return 1 + lcs(x,y,m-1,n-1)
#     else:
#         return max(lcs(x,y,m-1,n),lcs(x,y,m,n-1))
# x = 'abefg'
# y = 'abegcizpqrs'
# m = len(x)
# n = len(y)
# print(lcs(x,y,m,n))

str1 = 'asdc'
str2 = 'cabsc'
lcs(list(str1), list(str2))