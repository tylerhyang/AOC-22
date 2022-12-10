from os import getpriority


def main():
    inputs = readFile("input.txt")
    inputs1 = clean(inputs)
    inputs2 = clean2(inputs)
    out1 = soln1(inputs1)
    out2 = soln2(inputs2)
    return out1, out2


def readFile(filePath):
    """reads the input file

    Args:
        filePath (string): the filename for the inputs

    Returns:
        list: a list of strings
    """
    with open(filePath) as f:
        lines = f.readlines()
    lines = list(map(lambda x: x[:-1] if x[-1] == "\n" else x, lines))
    return lines


def clean(inputs):
    """cleans the input by spacing the sack properly

    Args:
        inputs (list[string]): a list of strings representing each rucksack

    Returns:
        list[list[string]]: a list of list of strings where the rucksacks are divided in half
    """
    res = []
    for sack in inputs:
        size = len(sack)
        res.append([sack[: size // 2], sack[size // 2 :]])
    return res

def clean2(inputs):
    """cleans the input if the sack to group into thirds

    Args:
        inputs (list[string]): a list of strings representing each rucksack

    Returns:
        list[list[string]]: a list of list of strings partitioning into groups of 3
    """
    res = []
    for i in range(0, len(inputs), 3):
        res.append(inputs[i:i+3])
    return res


def soln1(inputs):
    """finds the total priority across all the sacks

    Args:
        inputs (list[list[string]]): a list of list of strings representing the two compartments of each rucksack

    Returns:
        int: the sum of the priority of the items present in both compartments of each sack
    """
    total = 0
    for ls in inputs:
        sack1, sack2 = set(ls[0]), set(ls[1])
        overlap = sack1.intersection(sack2)
        total += getSPriority(overlap)
    return total


def soln2(inputs):
    """finds the total priority of all badges

    Args:
        inputs (list[list[string]]): a list of list of strings representing the triplets of rucksacks

    Returns:
        int: the sum of the priorities across each triplet
    """
    total = 0
    for sacks in inputs:
        set1,set2,set3 = set(sacks[0]), set(sacks[1]), set(sacks[2])
        badges = set1 & set2 & set3
        total += getSPriority(badges)
    return total


def getSPriority(charSet):
    """fetches the total priority of a given set of commonly found characters

    Args:
        charSet (set[str]): a set of characters that are present across all sacks

    Returns:
        int: the total priority of all the characters in the given set
    """
    totalPriority = 0
    for char in charSet:
        val = ord(char)
        if val < 91:
            totalPriority += val - ord("A") + 1 + 26
        else:
            totalPriority += val - ord("a") + 1
    return totalPriority


if __name__ == "__main__":
    print(main())
