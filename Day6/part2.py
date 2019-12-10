from input import x

#Could be done with a graph/shortest path or a bidirectional dict, but to make it work with the original data structure,
#its just add the closest shared parent orbit b/w santa and you
def main():
    orbitDict = {orbiter:orbitee for i in x.split() for orbitee, orbiter in [i.split(")")]}
    myDistances = dict()
    currentBody = "YOU"
    i=0
    while currentBody != "COM":
        myDistances[currentBody] = i
        currentBody = orbitDict[currentBody]
        i += 1
    sanDistances = dict()
    currentBody = "SAN"
    i=0
    while currentBody != "COM":
        if currentBody in myDistances:
            sanDistances[currentBody] = i
        currentBody = orbitDict[currentBody]
        i += 1

    min = -1
    for each in sanDistances:
        if min == -1 or sanDistances[each] + myDistances[each] < min:
            min = sanDistances[each] + myDistances[each]
    print(min-2) # minus two because it's not orbit distance, but hops, so hopping to the first orbit isn't counted
if __name__ == "__main__":
    main()