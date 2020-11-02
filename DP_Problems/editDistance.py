def editDistance(str1,str2,m,n):
    tab = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
        for j in range(m+1):
            if i == 0:
                tab[i][j] = j
            elif j == 0:
                tab[i][j] = i
            elif str2[i-1] == str1[j-1]:
                tab[i][j] = tab[i-1][j-1]
            else:
                tab[i][j] = min(1+tab[i][j-1],1+tab[i-1][j],1+tab[i-1][j-1])
    print(tab[n][m])
str1 = "abcd"
str2 = "a"
editDistance(str1,str2,len(str1),len(str2))














#reccursion
# def editDistnce(str1,str2,m,n):
#     if m <= 0:
#         return n
#     if n <= 0:
#         return m
#     if str1[m-1] == str2[n-1]:
#         return editDistnce(str1,str2,m-1,n-1)
#     return min(1+editDistnce(str1,str2,m-1,n),
#                1+editDistnce(str1,str2,m-1,n-1),
#                1+editDistnce(str1,str2,m,n-1))
# str1 = "abcd"
# str2 = "ef"
# print(editDistnce(str1,str2,len(str1),len(str2)))