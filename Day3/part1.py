from input import x,y

def manhattanDistance(x1, y1, x2, y2):
    return abs(x1-x2) + abs(y1-y2)

#We only need to store all points from the first wire and it going to the same position twice doesn't matter, so use a set
#Then check if that point is in the set for wire2 and if so add it to shared points. Then evaluate all shared points
def main():
    wire1 = x
    wire2 = y
    visitedPoints = set()
    sharedPoints = set()
    wire1Start = [0,0]
    for eachPoint in wire1.split(","):
        dir = eachPoint[0]
        distance = int(eachPoint[1:])
        if dir == "R":
            for eachJump in range(distance):
                wire1Start[0] += 1
                tup = tuple(wire1Start)
                visitedPoints.add(tup)
        if dir == "L":
            for eachJump in range(distance):
                wire1Start[0] -= 1
                tup = tuple(wire1Start)
                visitedPoints.add(tup)
        if dir == "U":
            for eachJump in range(distance):
                wire1Start[1] += 1
                tup = tuple(wire1Start)
                visitedPoints.add(tup)
        if dir == "D":
            for eachJump in range(distance):
                wire1Start[1] -= 1
                tup = tuple(wire1Start)
                visitedPoints.add(tup)

    wire2Start = [0,0]
    for eachPoint in wire2.split(","):
        dir = eachPoint[0]
        distance = int(eachPoint[1:])
        if dir == "R":
            for eachJump in range(distance):
                wire2Start[0] += 1
                tup = tuple(wire2Start)
                if tup in visitedPoints:
                    sharedPoints.add(tup)
        if dir == "L":
            for eachJump in range(distance):
                wire2Start[0] -= 1
                tup = tuple(wire2Start)
                if tup in visitedPoints:
                    sharedPoints.add(tup)
        if dir == "U":
            for eachJump in range(distance):
                wire2Start[1] += 1
                tup = tuple(wire2Start)
                if tup in visitedPoints:
                    sharedPoints.add(tup)
        if dir == "D":
            for eachJump in range(distance):
                wire2Start[1] -= 1
                tup = tuple(wire2Start)
                if tup in visitedPoints:
                    sharedPoints.add(tup)
    min =   -1
    for eachPoint in sharedPoints:
        dist = manhattanDistance(eachPoint[0], eachPoint[1], 0, 0)
        if min == -1 or dist < min:
            min = dist
    print(min)



main()
