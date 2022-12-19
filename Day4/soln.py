import xxlimited


def main():
    inputs = readFile("input.txt")
    inputs1 = clean1(inputs)
    part1 = soln1(inputs1)
    part2 = soln2(inputs1)
    return part1, part2


def readFile(filePath):
    """reads the input file

    Args:
        filePath (string): the filename for the inputs

    Returns:
        list: a list of strings
    """
    with open(filePath) as f:
        lines = f.readlines()
    lines = list(map(lambda x: [[x[:-1]]] if x[-1] == "\n" else [[x]], lines))
    return lines

def clean1(inputs):
    parsed = [x[0][0].split(",") for x in inputs]
    for i in range(len(parsed)):
        parsed[i] = toIntRange(parsed[i])
    return parsed

def soln1(pairs):
    valid = 0
    for pairSet in pairs:
        interval1, interval2 = pairSet
        if containsInterval(interval1, interval2):
            print(pairSet)
            valid += 1
    return valid

def soln2(pairs):
    valid = 0
    for pairSet in pairs:
        interval1, interval2 = pairSet
        if overlapInterval(interval1, interval2):
            print(pairSet)
            valid += 1
    return valid

def containsInterval(i1, i2):
    start1, end1 = i1
    start2, end2 = i2
    if (start1 >= start2 and end1 <= end2) or (start2 >= start1 and end2 <= end1):
        return True
    return False

def overlapInterval(i1, i2):
    start1, end1 = i1
    start2, end2 = i2
    if (end1 >= start2 and start1 <= end2):
        return True
    return False

def toIntRange(pair):
    x = []
    interval1 = pair[0].split("-")
    newPair = [int(x) for x in interval1]
    x.append(newPair)
    interval2 = pair[1].split("-")
    x.append([int(x) for x in interval2])
    return x

if __name__ == "__main__":
    print(main())