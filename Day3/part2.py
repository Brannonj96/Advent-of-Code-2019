from input import x,y

#Same idea as part 1 except now we keep track of the distance traveled and store it in a dictionary.  Then just keep track
#of the min distance to a point we already visited
def main():
    wire1 = x
    wire2 = y
    visitedPoints = set()
    points2Distance = dict()
    wire1Distance = 0
    wire1Start = [0,0]
    for eachPoint in wire1.split(","):
        dir = eachPoint[0]
        distance = int(eachPoint[1:])
        if dir == "R":
            for eachJump in range(distance):
                wire1Distance+=1
                wire1Start[0] += 1
                tup = tuple(wire1Start)
                if tup not in visitedPoints:
                    points2Distance[tup] = wire1Distance
                visitedPoints.add(tup)
        if dir == "L":
            for eachJump in range(distance):
                wire1Distance+=1
                wire1Start[0] -= 1
                tup = tuple(wire1Start)
                if tup not in visitedPoints:
                    points2Distance[tup] = wire1Distance
                visitedPoints.add(tup)
        if dir == "U":
            for eachJump in range(distance):
                wire1Distance+=1
                wire1Start[1] += 1
                tup = tuple(wire1Start)
                if tup not in visitedPoints:
                    points2Distance[tup] = wire1Distance
                visitedPoints.add(tup)
        if dir == "D":
            for eachJump in range(distance):
                wire1Distance+=1
                wire1Start[1] -= 1
                tup = tuple(wire1Start)
                if tup not in visitedPoints:
                    points2Distance[tup] = wire1Distance
                visitedPoints.add(tup)

    wire2Start = [0,0]
    wire2Distance = 0
    min = -1
    for eachPoint in wire2.split(","):
        dir = eachPoint[0]
        distance = int(eachPoint[1:])
        if dir == "R":
            for eachJump in range(distance):
                wire2Distance += 1
                wire2Start[0] += 1
                tup = tuple(wire2Start)
                if tup in visitedPoints:
                    dist = wire2Distance + points2Distance[tup]
                    if min == -1 or dist < min :
                        min = dist
        if dir == "L":
            for eachJump in range(distance):
                wire2Distance += 1
                wire2Start[0] -= 1
                tup = tuple(wire2Start)
                if tup in visitedPoints:
                    dist = wire2Distance + points2Distance[tup]
                    if min == -1 or dist < min :
                        min = dist
        if dir == "U":
            for eachJump in range(distance):
                wire2Distance += 1
                wire2Start[1] += 1
                tup = tuple(wire2Start)
                if tup in visitedPoints:
                    dist = wire2Distance + points2Distance[tup]
                    if min == -1 or dist < min :
                        min = dist
        if dir == "D":
            for eachJump in range(distance):
                wire2Distance += 1
                wire2Start[1] -= 1
                tup = tuple(wire2Start)
                if tup in visitedPoints:
                    dist = wire2Distance + points2Distance[tup]
                    if min == -1 or dist < min :
                        min = dist
    print(min)

if __name__=="__main__":
    main()