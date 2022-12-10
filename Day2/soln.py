from functools import reduce


def main():
    """solution driver

    Returns:
        tuple[int]: the solutions for part 1 and part 2
    """
    inputs = readFile("input.txt")
    inputsp1 = clean(inputs)
    pt1 = soln1(inputsp1)
    pt2 = soln2(inputs)
    return (pt1, pt2)


def readFile(filePath):
    """reads the input file

    Args:
        filePath (string): the filename for the inputs

    Returns:
        list: a list of integer and "#" as delimiters
    """
    with open(filePath) as f:
        lines = f.readlines()
    lines = list(map(lambda x: x[:-1] if x[-1] == "\n" else x, lines))
    return lines


def clean(inputs):
    """Cleans the input for the part 1 driver function to handle

    Args:
        inputs (list[str]): a list representing the adversarial actions and your own actions

    Returns:
        list[str]: a list representing the adversarial actions in their respective user actions
    """
    replacements = {"A": "X", "B": "Y", "C": "Z"}
    res = list(map(lambda x: replacements[x[0]] + x[1:], inputs))
    return res


def soln1(inputs):
    """
    finds the sum of all interactions

    Args:
        inputs (list[str]): a list of strings representing actions between the adversary and the user

    Returns:
        int: the sum of the scores following the strategy
    """
    val = {"X": 1, "Y": 2, "Z": 3}
    total = 0
    for pairs in inputs:
        adv, prot = pairs[0], pairs[2]
        diff = ord(prot) - ord(adv)
        if diff == 2 or diff == -1:
            total += val[prot]
        elif diff == 1 or diff == -2:
            total += 6 + val[prot]
        else:
            total += 3 + val[prot]
    return total


def soln2(inputs):
    """finds the total score of the user when the encrypted column is revealed to be the required state

    Args:
        inputs (list[str]): a list of strings representing the adversarial and user actions

    Returns:
        int: the sum of the scores
    """
    val = {"A": 1, "B": 2, "C": 3}
    total = 0
    for pair in inputs:
        adv, state = pair[0], pair[2]
        if state == "Y":
            total += val[adv] + 3
        elif state == "X":
            char = determineLoss(adv)
            total += val[char]
        else:
            char = determineWin(adv)
            total += val[char] + 6
    return total


def determineLoss(action):
    """returns the user action that results in a loss

    Args:
        action (str): the action that the adversary takes

    Returns:
        str: the action the user must take to result in a Loss state
    """
    if action == "A":
        return "C"
    elif action == "B":
        return "A"
    else:
        return "B"


def determineWin(action):
    """returns the user action that results in a win

    Args:
        action (str): the action that the adversary takes

    Returns:
        str: the action the user must take to result in a Win state
    """
    if action == "A":
        return "B"
    elif action == "B":
        return "C"
    else:
        return "A"


if __name__ == "__main__":
    print(main())
