def reverse(str):
    n = len(str)-1
    mid = int(len(str)/2)
    s = list(str)
    for i in range(0,mid):
        temp = s[i]
        s[i] = s[n]
        s[n] = temp
        n=n-1
    return  s
def rev(num):
    rev = 0
    while(num>0):
        remainder = num%10
        rev = rev*10 + remainder
        num = int(num/10)
    return rev
str = "hello"
a = rev(12345)
print(a)
ans = reverse(str)
print(ans)