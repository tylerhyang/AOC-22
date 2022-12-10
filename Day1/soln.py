from distutils.command.clean import clean


def main():
    inputs = readFile("input.txt")
    return (part1(inputs), part2(inputs))


def readFile(filePath):
    with open(filePath) as f:
        lines = f.readlines()
    lines = list(map(lambda x: "#" if x == '\n' else (int(x[:-2] if x[:-2] == '\n' else x)), lines))
    lines = clean(lines)
    return lines
def clean(inputs):
    ret = []
    start = 0
    for i in range(len(inputs)):
        if inputs[i] == "#":
            ret.append(inputs[start:i])
            start = i+1
    ret.append(inputs[start:len(inputs)])
    return ret

def part1(inputs):
    return max(list(map(lambda x: sum(x), inputs)))

def part2(inputs):
    ls = list(map(lambda x: sum(x), inputs))
    ls.sort(reverse=True)
    return sum(ls[:3])
    
if __name__ == "__main__":
    print(main())
