import sys
def minSum(cost,m,n):
    if n<0 or m<0:
        return  sys.maxsize
    if m == 0 and n == 0:
        return cost[0][0]
    return cost[m][n] + min( minSum(cost,m-1,n-1),minSum(cost,m-1,n),minSum(cost,m,n-1))
def min(x,y,z):
    if (x<y and x<z):
        return  x
    elif (y<x and y<z):
        return y
    else:
        return  z



cost = [[1,2,3],[4,5,6],[7,8,9]]
ans = minSum(cost,2,2)
print(ans)
