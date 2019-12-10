from input import x

def howManyOrbits(orbitDict, currentBody):
    #Returning 0 here accounts for the fact that the initial element does not count as an orbit
    if currentBody == "COM":
        return 0
    else:
        return 1 + howManyOrbits(orbitDict, orbitDict[currentBody])

def main():
    orbitDict = {orbiter:orbitee for i in x.split() for orbitee, orbiter in [i.split(")")]}
    print(sum(howManyOrbits(orbitDict, body) for body in orbitDict))


if __name__ == "__main__":
    main()