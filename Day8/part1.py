from input import x

def main():
    width = 25
    height = 6
    oneLineLayers = [x[i:i+(width*height)] for i in range(0,len(x), width*height)]
    min = 151
    myLayer = []
    for eachLayer in oneLineLayers:
        c = eachLayer.count("0")
        if c < min:
            min = c
            myLayer = eachLayer

    print(myLayer.count("2") * myLayer.count("1"))

if __name__ == "__main__":
    main()