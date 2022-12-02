def order_calories():
    # Implicitly numbered array containing total weights carried by elf_i
    elf_calories = []
    calories_sum = 0  # Adds the calories for a single elf
    with open("01.txt") as fp:
        for line in fp:
            if line.strip() == "":
                elf_calories.append(calories_sum)
                calories_sum = 0
            else:
                num = int(line.strip())
                calories_sum += num
    elf_calories.append(calories_sum)
    return elf_calories


def part1():
    return max(order_calories())


def part2():
    calories = order_calories()
    return sum(sorted(calories)[-3:])


if __name__ == "__main__":
    print(part1())
    print(part2())
