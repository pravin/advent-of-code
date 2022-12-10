def part1():
    state = [1]
    with open("10.txt") as fp:
        for line in fp:
            line = line.strip()
            if " " in line:  # add
                _, inc = line.split(" ")
                inc = int(inc)
                state.append(state[-1])
                state.append(state[-1] + inc)
            else:  # noop
                state.append(state[-1])

    return (
        state[19] * 20
        + state[59] * 60
        + state[99] * 100
        + state[139] * 140
        + state[179] * 180
        + state[219] * 220
    )


def part2():
    state = [1]
    with open("10.txt") as fp:
        for line in fp:
            line = line.strip()
            if " " in line:  # add
                _, inc = line.split(" ")
                inc = int(inc)
                state.append(state[-1])
                state.append(state[-1] + inc)
            else:  # noop
                state.append(state[-1])

    counter = 0
    for i in range(240):
        if i in (40, 80, 120, 160, 200):
            counter = 0
            print()
        if counter >= state[i] - 1 and counter <= state[i] + 1:
            print("#", end="")
        else:
            print(".", end="")
        counter += 1


if __name__ == "__main__":
    print(part1())
    part2()
    print()
