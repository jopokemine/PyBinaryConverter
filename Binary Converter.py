def numToBin(num):
    binList = []
    binary = ""
    while(num != 0 or (len(binList) % 8) != 0):
        if (num == 0):
            binList.append(0)
        else :
            binList.append(num % 2)
            num //= 2
    binList.reverse()
    for num in binList:
        binary += str(num)
    return binary
    
def binToNum(bin):
    bin = str(bin)
    num = 0
    for binNum in bin:
        num = 2 * num + int(binNum)
    return num
    

