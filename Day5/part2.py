from input import x

def getSpecificDigit(num, pos):
    return (num // (10**pos)) % 10

def saveInputAtPlace(currentIntcodeList, position, inp):
    changeIndex = currentIntcodeList[position+1]
    currentIntcodeList[changeIndex] = inp

def outputValAtPlace(currentIntcodeList, position):
    if getSpecificDigit(currentIntcodeList[position], 2) == 0:
        val = currentIntcodeList[currentIntcodeList[position+1]]
    else:
        val = currentIntcodeList[position+1]
    if val != 0:
        print("NON-ZERO DIAGNOSTIC CODE")
        print(val)

def readTwoAdd(currentIntcodeList, position):
    instruction = currentIntcodeList[position]
    if getSpecificDigit(instruction, 2) == 0:
        object1 = currentIntcodeList[currentIntcodeList[position+1]]
    else:
        object1 = currentIntcodeList[position+1]

    if getSpecificDigit(instruction, 3) == 0:
        object2 = currentIntcodeList[currentIntcodeList[position+2]]
    else:
        object2 = currentIntcodeList[position+2]
    changeIndex = currentIntcodeList[position+3]
    currentIntcodeList[changeIndex] = object1 + object2

def readTwoMultiply(currentIntcodeList, position):
    instruction = currentIntcodeList[position]
    if getSpecificDigit(instruction, 2) == 0:
        object1 = currentIntcodeList[currentIntcodeList[position+1]]
    else:
        object1 = currentIntcodeList[position+1]

    if getSpecificDigit(instruction, 3) == 0:
        object2 = currentIntcodeList[currentIntcodeList[position+2]]
    else:
        object2 = currentIntcodeList[position+2]
    changeIndex = currentIntcodeList[position+3]
    currentIntcodeList[changeIndex] = object1 * object2

def jumpIfTrue(currentIntcodeList, position):
    instruction = currentIntcodeList[position]
    if getSpecificDigit(instruction, 2) == 0 :
        val = currentIntcodeList[currentIntcodeList[position+1]]
    else:
        val = currentIntcodeList[position+1]
    if val == 0:
        return position+3

    if getSpecificDigit(instruction, 3) == 0:
        return currentIntcodeList[currentIntcodeList[position+2]]
    else:
        return currentIntcodeList[position+2]

def jumpIfFalse(currentIntcodeList, position):
    instruction = currentIntcodeList[position]
    if getSpecificDigit(instruction, 2) == 0 :
        val = currentIntcodeList[currentIntcodeList[position+1]]
    else:
        val = currentIntcodeList[position+1]
    if val != 0:
        return position +3
    if getSpecificDigit(instruction, 3) == 0:
        return currentIntcodeList[currentIntcodeList[position+2]]
    else:
        return currentIntcodeList[position+2]

def lessThan(currentIntcodeList, position):
    instruction = currentIntcodeList[position]
    if getSpecificDigit(instruction, 2) == 0:
        object1 = currentIntcodeList[currentIntcodeList[position+1]]
    else:
        object1 = currentIntcodeList[position+1]

    if getSpecificDigit(instruction, 3) == 0:
        object2 = currentIntcodeList[currentIntcodeList[position+2]]
    else:
        object2 = currentIntcodeList[position+2]
    currentIntcodeList[currentIntcodeList[position+3]] = int(object1 < object2)

def equals(currentIntcodeList, position):
    instruction = currentIntcodeList[position]
    if getSpecificDigit(instruction, 2) == 0:
        object1 = currentIntcodeList[currentIntcodeList[position+1]]
    else:
        object1 = currentIntcodeList[position+1]

    if getSpecificDigit(instruction, 3) == 0:
        object2 = currentIntcodeList[currentIntcodeList[position+2]]
    else:
        object2 = currentIntcodeList[position+2]
    currentIntcodeList[currentIntcodeList[position+3]] = int(object1 == object2)

def intcodeDriver(currentIntcodeList, position, inp):
    opCode = getSpecificDigit(currentIntcodeList[position], 0) + (getSpecificDigit(currentIntcodeList[position],1) * 10)
    print("Position: ", position, "Opcode: ", opCode)
    if opCode == 99:
        return 0
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
    print("Unexpected op code", currentIntcodeList[position], position)
    return -1

def main():
    inp = int(input("Enter your system ID: "))
    pos = 0
    currentIntcodeList = list(map(int, x.split(",")))
    while True:
        pos = intcodeDriver(currentIntcodeList, pos, inp)
        if pos == 0:
            print("Received halt code.")
            return
        if pos == -1:
            return


if __name__=="__main__":
    main()