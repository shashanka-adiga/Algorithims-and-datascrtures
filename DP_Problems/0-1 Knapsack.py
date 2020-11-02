
def knapsack(W,w,v,n):
    if n == 0 or W == 0:
        return 0
    if w[n-1] > W:
        return knapsack(W,w,v,n-1)
    else:
        return max(v[n-1]+knapsack(W-w[n-1],w,v,n-1), knapsack(W,w,v,n-1))

w = [10,18,22,4]
v = [10,8,16,6]
W = 40
n = len(v)
print(knapsack(W,w,v,n))


# recursive solution
# def knapsack(W,w,v,n):
#     if n == 0 or w == 0:
#         return 0
#     if w[n-1] > W:
#         return  knapsack(W,w,v,n-1)
#     else:
#         return max(v[n-1] + knapsack(W-w[n-1],w,v,n-1),knapsack(W,w,v,n-1))
#
#
# v = [100,20,30,40,50]
# w = [6,3,5,7,7]
# n = len(v)
# W = 16
# print(knapsack(W,w,v,n))