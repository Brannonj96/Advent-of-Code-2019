from input import *

def twoAdjacentSame(num):
    num = str(num)
    for i in range(len(num)-1):
        if num[i] == num[i+1]:
            break
    else:
        return False
    return True

def notDecrease(num):
    num = str(num)
    for i in range(len(num)-1):
        if int(num[i]) > int(num[i+1]):
            break
    else:
        return True
    return False

def main():
    print(sum([1 for i in range(mn, mx+1) if twoAdjacentSame(i) and notDecrease(i)]))

if __name__=="__main__":
    main()