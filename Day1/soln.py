#Advent of Code day 1
def main():
    """solution driver

    Returns:
        tuple[int]: the solutions for part 1 and part 2
    """
    inputs = readFile("input.txt")
    return (part1(inputs), part2(inputs))


def readFile(filePath):
    """reads the input file

    Args:
        filePath (string): the filename for the inputs

    Returns:
        list: a list of integer and "#" as delimiters
    """
    with open(filePath) as f:
        lines = f.readlines()
    lines = list(
        map(
            lambda x: "#" if x == "\n" else (int(x[:-2] if x[:-2] == "\n" else x)),
            lines,
        )
    )
    lines = clean(lines)
    return lines


def clean(inputs):
    """
    splits inputs into a list of list of integers

    Args:
        inputs (list): the inputs separated from the readFile function

    Returns:
        list[list[int]]: a list of list of integers representing the inputs
    """
    ret = []
    start = 0
    for i in range(len(inputs)):
        if inputs[i] == "#":
            ret.append(inputs[start:i])
            start = i + 1
    ret.append(inputs[start : len(inputs)])
    return ret


def part1(inputs):
    """
    returns the elf with the most calories

    Args:
        inputs (list[list[int]]): the input list where each list is the calories held by that elf

    Returns:
        int: the most calories held
    """
    return max(list(map(lambda x: sum(x), inputs)))


def part2(inputs):
    """returns the sum of the calories of the three elfs with the most calories

    Args:
        inputs (list[list[int]]): the input list where each list is the calories held by that elf

    Returns:
        int: sum of the calories of the top three elves
    """
    ls = list(map(lambda x: sum(x), inputs))
    ls.sort(reverse=True)
    return sum(ls[:3])


if __name__ == "__main__":
    print(main())
