

def rotate_anticlock(mat,m,n):
    print('rotated anti-clockwise:')
    for i in range(m-1,-1,-1):
        print('')
        for j in range(0,n):
            print(mat[j][i],end = ' ')
    print('\n')

def print_mat(mat,m,n):
    print('original matrix:')
    for i in range(0,m):
        print('')
        for j in range(0,n):
            print(mat[i][j],end = " ")
    print('\n')

def rotate_clock(mat,m,n):
    print('rotated clock-wise:')
    for i in range(0,m):
        print('')
        for j in range(0,n):
            print(mat[j][i],end=' ')
    print('\n')

mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
n = len(mat)
m = len(mat[0])

print_mat(mat,n,m)
rotate_anticlock(mat,m,n)
rotate_clock(mat,m,n)