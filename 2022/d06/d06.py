def part1():
    return compute(4)


def part2():
    return compute(14)


def compute(pos):
    with open("06.txt") as fp:
        string = fp.read().strip()
        for i in range(len(string)):
            if len(set(string[i : i + pos])) == pos:
                break
    return i + pos


if __name__ == "__main__":
    print(part1())
    print(part2())
