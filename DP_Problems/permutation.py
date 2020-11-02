string = "123"
result = []
def perm(data,i,length):
    if i == length:
        result.append(''.join(data))
    for j in range(i,length):
        data[i],data[j] = data[j],data[i]
        perm(data,i+1,length)
        data[i], data[j] = data[j], data[i]
perm(list(string),0,len(string))
print("resultant permutation",str(result))
print(len(result))
