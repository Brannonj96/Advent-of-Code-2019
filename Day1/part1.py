from input import x

def main():
    print(sum([(i//3)-2 for i in map(int,x.split())]))

if __name__=="__main__":
    main()