from part1 import *
from input import x

def main():
    orig = list(map(int, x.split(",")))
    for i in range(100):
        for j in range(100):
            currentList = orig + []
            currentList[1] = i
            currentList[2] = j
            pos = 0
            while True:
                pos = intcodeDriver(currentList, pos)

                #-1 means unexpected intcode operation
                if pos == -1:
                    print("Unexpected intcode operation.  Unable to continue")
                    break
                #0 Means it has returned to the start, i.e. the halt code was given
                if pos == 0:
                    break
            if currentList[0] == 19690720:
                print("Found the solution:", 100 * i + j)
                return
    print("No solution found. Double check input")

if __name__=="__main__":
    main()