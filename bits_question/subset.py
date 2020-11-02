def subset(List,N):
    for i in range(0,(1<<N)):
        for j in range(0,N):
            if(i & (1<<j)):
                print(List[j],end=' ')
        print('')
List = ['a','b','c']
N = len(List)
subset(List,N)