from input import x
from itertools import permutations

global lastVal
def getSpecificDigit(num, pos):
    return (num // (10**pos)) % 10

def saveInputAtPlace(currentIntcodeList, position, inp):
    changeIndex = currentIntcodeList[position+1]
    currentIntcodeList[changeIndex] = inp

def outputValAtPlace(currentIntcodeList, position):
    global lastVal
    if getSpecificDigit(currentIntcodeList[position], 2) == 0:
        val = currentIntcodeList[currentIntcodeList[position+1]]
    else:
        val = currentIntcodeList[position+1]
    lastVal = val

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
    #print("Position: ", position, "Opcode: ", opCode)
    if opCode == 99:
        return -1, True
    if opCode == 3:
        saveInputAtPlace(currentIntcodeList, position, inp)
        return position + 2, False
    if opCode == 4:
        outputValAtPlace(currentIntcodeList, position)
        return position + 2, True
    if opCode == 1:
        readTwoAdd(currentIntcodeList, position)
        return position + 4, False
    if opCode == 2:
        readTwoMultiply(currentIntcodeList, position)
        return position + 4, False
    if opCode == 5:
        return jumpIfTrue(currentIntcodeList, position), False
    if opCode == 6:
        return jumpIfFalse(currentIntcodeList, position), False
    if opCode == 7:
        lessThan(currentIntcodeList, position)
        return position + 4, False
    if opCode == 8:
        equals(currentIntcodeList, position)
        return position+4, False
    print("Unexpected op code", currentIntcodeList[position], position)
    return -2, True


#Without threading/waiting, it was all run sequentially
#To know when to skip to the next amplifier, it returns True.  This only happens on halt codes, unknown codes, and
#when output is given because output should immediately move onto the next amp.  A dictionary keeps track of the different
#list states and positions of each list.  the global lastVal is always the last output.  To handle phase states,
#the 5 lists are initialized with them, and then the first amplifier is initialized with 0 input.  Then the loop can
#continue normally.
#
#Basically a queue implementation using dictionary.
def main():
    global lastVal
    orig = list(map(int, x.split(",")))
    max = -1
    answerPermutation = []
    for each in permutations([5,6,7,8,9]):
        lastVal = 0
        a = orig + []
        b = orig + []
        c = orig + []
        d = orig + []
        e = orig + []
        phase = each
        amp = 0
        amps = {0:a, 1:b, 2:c, 3:d, 4:e}
        posDict = {0:0, 1:0, 2:0, 3:0, 4:0}

        #Seed the initial phase state for each amplifier
        for i in range(5):
            posDict[i], _ = intcodeDriver(amps[i], 0, phase[i])
        #Give the initial input to amp A, i.e. last val is 0
        posDict[0], _ = intcodeDriver(amps[0], posDict[0], 0)
        done = False
        while not done:
            while True:
                posDict[amp], next = intcodeDriver(amps[amp], posDict[amp], lastVal)
                if next:
                    if amp == 4 and posDict[amp] == -1: #-1 means it halted.  If the 4th amp, the final one, halted, it means the output is done
                        #print("Final amp halted")
                        done = True
                    break
            amp += 1
            amp %= 5
        if lastVal > max:
            max = lastVal
            answerPermutation = each
    print(max, answerPermutation)

if __name__=="__main__":
    main()