def ways(s,m,n):
    if m ==0:
        return 0
    if n == 0:
        return 1
    return (ways(s,m-1,n)+ ways(s,m,n-s[m-1]))
s = [3]
m = len(s)
ans = ways(s,m,3)
print(ans)
