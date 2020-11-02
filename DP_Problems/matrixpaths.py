def ways(m,n):
    if m < n:
        mat = [[0 for i in range(n+1)] for j in range(n+1)]
    else:
        mat = [[0 for i in range(m + 1)] for j in range(m + 1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if i==1 or j==1:
                mat[i][j] = 1
            else:
                mat[i][j] = mat[i-1][j] + mat[i][j-1] + mat[i-1][j-1]
    print(mat[m][n])
ways(2,4)