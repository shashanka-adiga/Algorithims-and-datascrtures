# def minDenomination(denominations , targetSum):
#     i = len(denominations) - 1
#     toGive = [0]*len(denominations)
#     while(i>=0):
#         while targetSum >= denominations[i]:
#             targetSum = targetSum - denominations[i]
#             toGive[i] = toGive[i] + 1
#             print(denominations[i] ,end=' ')
#         i = i -1
#     print()
#     print("number of denominations of each used:")
#     print(toGive)
# denominations = [1,2,5,20,50,100,500,1000,2000]
# targetSum = 549
# minDenomination(denominations,targetSum)

from collections import OrderedDict
def non_rec(lst):
    d = OrderedDict()
    for i in lst:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i] + 1
    for k,v in d.items():
        if v == 1:
            print(k)




s = [2,2,1,3,1,4,5,3,4]
print(s.count(2))
non_rec(s)