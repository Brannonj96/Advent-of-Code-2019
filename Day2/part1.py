from input import x

def readTwoAdd(currentIntcodeList, position):
    changeIndex = currentIntcodeList[position+3]
    object1 = currentIntcodeList[position+1]
    object2 = currentIntcodeList[position+2]
    currentIntcodeList[changeIndex] = currentIntcodeList[object1] + currentIntcodeList[object2]

def readTwoMultiply(currentIntcodeList, position):
    changeIndex = currentIntcodeList[position+3]
    object1 = currentIntcodeList[position+1]
    object2 = currentIntcodeList[position+2]
    currentIntcodeList[changeIndex] = currentIntcodeList[object1] * currentIntcodeList[object2]

def intcodeDriver(currentIntcodeList, position):
    if currentIntcodeList[position] == 99:
        return 0
    if currentIntcodeList[position] == 1:
        readTwoAdd(currentIntcodeList, position)
        return position + 4
    if currentIntcodeList[position] == 2:
        readTwoMultiply(currentIntcodeList, position)
        return position + 4
    return -1

def main():
    intcodeList = list(map(int, x.split(",")))
    intcodeList[1] = 12
    intcodeList[2] = 2
    pos = 0
    while True:
        pos = intcodeDriver(intcodeList, pos)

        #-1 means unexpected intcode operation
        if pos == -1:
            print("Unexpected intcode operation.  Unable to continue")
            return
        #0 Means it has returned to the start, i.e. the halt code was given
        if pos == 0:
            #Print the first value for task 1
            print("Done. First value is", intcodeList[0])
            return

if __name__=="__main__":
    main()