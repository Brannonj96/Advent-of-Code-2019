from input import x

def part2():
    print(sum(map((lambda a: lambda v: a(a,v))(lambda s,i: (i//3)-2 + s(s, (i//3)-2) if i>8 else 0), map(int, x.split()))))


if __name__=="__main__":
    part2()