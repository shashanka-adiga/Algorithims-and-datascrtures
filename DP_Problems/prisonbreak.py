def pbreak(cost,m,n):
    if n<0 or m<0:
        return 0
    if n==0 and m==0 and cost[0][0] == 0:
        return  1
    if cost[m][n] ==1:
        return 0;
    if cost[m][n] == 0:
        return  pbreak(cost,m-1,n) + pbreak(cost,m,n-1) + pbreak(cost,m-1,n-1)



cost = [[0,0,0],[1,1,0],[1,1,0]]

print(pbreak(cost,2,2))