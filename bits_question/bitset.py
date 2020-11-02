def bitSet(num,pos):
    if (num & (1<<pos)):
        return True
    else:
        return  False
print(bitSet(128,7))