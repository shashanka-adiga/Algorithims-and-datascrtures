
def unique(List):
    x = 0
    for i in List:
        x = x^i
    print(x)
List = [1,2,3,2,1]
unique(List)
