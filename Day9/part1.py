from input import x

global relativeBase
relativeBase = 0

def getSpecificDigit(num, pos):
    return (num // (10**pos)) % 10

#offset is how far right from the position the desired parameter is
def getIndex(currentIntcodeList, position, offset=1):
    instructionNum = currentIntcodeList[position]
    mode = getSpecificDigit(instructionNum, offset+1)
    if mode == 0: #position mode
        getPos = currentIntcodeList[position+offset]
        return getPos
    elif mode == 1: #immediate mode
        return position+offset
    elif mode == 2: #relative mode
        getPos = currentIntcodeList[position+offset]
        return getPos + relativeBase

def saveInputAtPlace(currentIntcodeList, position, inp):
    changeIndex = getIndex(currentIntcodeList, position, 1)
    currentIntcodeList[changeIndex] = inp

def outputValAtPlace(currentIntcodeList, position):
    ind = getIndex(currentIntcodeList, position, 1)
    val = currentIntcodeList[ind]
    if val != 0:
        print("NON ZERO DIAGNOSTIC CODE")
    print(val)

def readTwoAdd(currentIntcodeList, position):
    object1 = currentIntcodeList[getIndex(currentIntcodeList, position, 1)]
    object2 = currentIntcodeList[getIndex(currentIntcodeList, position, 2)]
    changeIndex = getIndex(currentIntcodeList, position, 3)
    currentIntcodeList[changeIndex] = object1 + object2

def readTwoMultiply(currentIntcodeList, position):
    object1 = currentIntcodeList[getIndex(currentIntcodeList, position, 1)]
    object2 = currentIntcodeList[getIndex(currentIntcodeList, position, 2)]
    changeIndex = getIndex(currentIntcodeList, position, 3)
    currentIntcodeList[changeIndex] = object1 * object2

def jumpIfTrue(currentIntcodeList, position):
    val = currentIntcodeList[getIndex(currentIntcodeList, position, 1)]
    if val == 0:
        return position+3

    return currentIntcodeList[getIndex(currentIntcodeList, position, 2)]

def jumpIfFalse(currentIntcodeList, position):
    val = currentIntcodeList[getIndex(currentIntcodeList, position, 1)]
    if val != 0:
        return position+3
    return currentIntcodeList[getIndex(currentIntcodeList, position, 2)]


def lessThan(currentIntcodeList, position):
    object1 = currentIntcodeList[getIndex(currentIntcodeList, position, 1)]
    object2 = currentIntcodeList[getIndex(currentIntcodeList, position, 2)]
    changeIndex = getIndex(currentIntcodeList, position, 3)
    currentIntcodeList[changeIndex] = int(object1 < object2)

def equals(currentIntcodeList, position):
    object1 = currentIntcodeList[getIndex(currentIntcodeList, position, 1)]
    object2 = currentIntcodeList[getIndex(currentIntcodeList, position, 2)]
    changeIndex = getIndex(currentIntcodeList, position, 3)
    currentIntcodeList[changeIndex] = int(object1 == object2)

def intcodeDriver(currentIntcodeList, position, inp):
    global relativeBase
    opCode = getSpecificDigit(currentIntcodeList[position], 0) + (getSpecificDigit(currentIntcodeList[position],1) * 10)
    #print("Position: ", position, "Opcode: ", opCode)
    if opCode == 99:
        return -1
    if opCode == 3:
        saveInputAtPlace(currentIntcodeList, position, inp)
        return position + 2
    if opCode == 4:
        outputValAtPlace(currentIntcodeList, position)
        return position + 2
    if opCode == 1:
        readTwoAdd(currentIntcodeList, position)
        return position + 4
    if opCode == 2:
        readTwoMultiply(currentIntcodeList, position)
        return position + 4
    if opCode == 5:
        return jumpIfTrue(currentIntcodeList, position)
    if opCode == 6:
        return jumpIfFalse(currentIntcodeList, position)
    if opCode == 7:
        lessThan(currentIntcodeList, position)
        return position + 4
    if opCode == 8:
        equals(currentIntcodeList, position)
        return position+4
    if opCode == 9:
        relativeBase += currentIntcodeList[getIndex(currentIntcodeList, position, 1)]
        return position+2
    print("Unexpected op code", currentIntcodeList[position], position)
    return -2

def main():
    orig = list(map(int, x.split(",")))
    orig = orig + [0]*3000000
    pos = 0

    while True:
        #print(orig[:16], orig[100], orig[101], relativeBase)
        pos = intcodeDriver(orig, pos, 1)
        if pos == -2:
            break
        if pos == -1:
            print("Finished")
            break

if __name__=="__main__":
    main()