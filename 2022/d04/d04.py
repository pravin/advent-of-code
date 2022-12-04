def part1():
    count = 0
    with open("04.txt") as fp:
        for line in fp:
            arr = line.strip().split(",")
            s1, e1 = [int(x) for x in arr[0].split("-")]
            s2, e2 = [int(x) for x in arr[1].split("-")]
            if s2 >= s1 and s2 <= e1 and e2 >= s1 and e2 <= e1:
                count += 1
            elif s1 >= s2 and s1 <= e2 and e1 >= s2 and e1 <= e2:
                count += 1
    return count


def part2():
    count = 0
    with open("04.txt") as fp:
        for line in fp:
            arr = line.strip().split(",")
            s1, e1 = [int(x) for x in arr[0].split("-")]
            s2, e2 = [int(x) for x in arr[1].split("-")]
            if (s2 >= s1 and s2 <= e1) or (e2 >= s1 and e2 <= e1):
                count += 1
            elif (s1 >= s2 and s1 <= e2) or (e1 >= s2 and e1 <= e2):
                count += 1
    return count


if __name__ == "__main__":
    print(part1())
    print(part2())
