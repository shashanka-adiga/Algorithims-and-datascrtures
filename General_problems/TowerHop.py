def towerhop(towers,target):
    length = target
    for i in range(length-1,-1,-1):
        if (i+towers[i]) >= target:
            target = target - towers[i]
    if target > 0:
        return  False
    return True

towers = [5,0,0,0,0,1]
print(towerhop(towers,len(towers)))