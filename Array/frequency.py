d = {}
l = []
n = int(input('number of items:\n'))
print('enter items:\n')
for i in range(0,n):
    l.append(input())

def frequency(l):
    for i in l:
        if i not in d:
            d[i] = 1
        else:
            d[i] = d[i]+1
    return d
def unique(l):
    f = frequency(l)
    for k,v in f.items():
        if v<2:
            print(k)
unique(l)