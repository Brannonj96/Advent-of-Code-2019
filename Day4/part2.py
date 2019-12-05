from input import *

def notDecrease(num):
    num = str(num)
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            break
    else:
        return True
    return False

def exactlyTwoAdjacentSame(num):
    num = str(num)
    last = num[0]
    satisfied = False
    skip = False
    for i in range(1, len(num)):
        if num[i] != last:
            skip = False
        if num[i] != last and satisfied == True:
            break
        if num[i] == last and not skip:
            if satisfied == True:
                satisfied = False
                skip = True
            else:
                satisfied = True
        last = num[i]

    return satisfied

def main():
    print(sum([notDecrease(i) and exactlyTwoAdjacentSame(i) for i in range(mn, mx+1)]))

if __name__=="__main__":
    main()