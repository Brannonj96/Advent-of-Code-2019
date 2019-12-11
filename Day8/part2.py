from input import x

def main():
    width = 25
    height = 6
    oneLineLayers = [x[i:i+(width*height)] for i in range(0,len(x), width*height)]
    finalOutput = [0] * width*height
    for eachPixel in range(len(oneLineLayers[0])):
        currentColor = "2"
        for eachLayer in oneLineLayers:
            if eachLayer[eachPixel] == "2":
                continue
            else:
                currentColor = eachLayer[eachPixel]
                break
        finalOutput[eachPixel] = currentColor

    print(finalOutput)
    rowsOfOutput = [finalOutput[i:i+width] for i in range(0, len(finalOutput), width)]
    for i in rowsOfOutput:
        for each in i:
            if each =="2":
                print(end=" ")
            if each == "1":
                print(end="#")
            else:
                print(end=" ")
        print()

if __name__ == "__main__":
    main()