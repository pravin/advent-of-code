def part1():
    # Create a large enough array to capture visited state
    SIZE = 1000
    vstate = [[0] * SIZE for _ in range(SIZE)]

    half = (SIZE - 1) // 2
    hpos = [half, half]  # Head position
    tpos = [half, half]
    vstate[tpos[0]][tpos[1]] = 1

    with open("09.txt") as fp:
        for line in fp:
            direction, increment = line.strip().split()
            increment = int(increment)

            for i in range(increment):
                x, y = 0, 0
                # Set the direction
                if direction == "R":
                    x += 1
                elif direction == "L":
                    x -= 1
                elif direction == "U":
                    y -= 1
                elif direction == "D":
                    y += 1
                # Temporary save prev hpos
                prev_hpos = hpos.copy()
                # Move hpos in the direction
                hpos[0] += x
                hpos[1] += y

                if (
                    tpos[0] >= hpos[0] - 1
                    and tpos[0] <= hpos[0] + 1
                    and tpos[1] >= hpos[1] - 1
                    and tpos[1] <= hpos[1] + 1
                ):
                    # If tpos is touching hpos, do nothing
                    pass
                else:
                    # Else move tpos to prev hpos
                    tpos = prev_hpos
                    vstate[tpos[0]][tpos[1]] = 1
    return [sum(x) for x in vstate]


if __name__ == "__main__":
    print(sum(part1()))
