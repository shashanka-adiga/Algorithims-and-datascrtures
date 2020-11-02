def decToHex(num):
    i = 0
    hexadecimal = [0]*32
    element = 0
    while(num>0):
        element = int((num/16-int(num/16))*16)
        if(element > 9):
            if (element == 10):
                element = 'A'
            elif (element == 11):
                element = 'B'
            elif (element == 12):
                element = 'C'
            elif (element == 13):
                element = 'D'
            elif (element == 14):
                element = 'E'
            else:
                element = 'F'
        hexadecimal[i] = element
        num =int(num/16)
        i = i + 1
    for j in range(i-1,-1,-1):
        print(hexadecimal[j],end='')
decToHex(42)