def negatives(mat,m,n):
    i = 0
    j = n-1
    count = 0
    while i < m and j >= 0:
        if mat[i][j]<0:
            count = count + (j+1)
            i = i+1
        else:
            j = j-1
    print(count)
mat = [[-3,-2,-1,1],[-4,-3,-2,0]]
negatives(mat,2,4)