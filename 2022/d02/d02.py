def part1():
    score_map = {
        "A X": 3,
        "A Y": 6,
        "A Z": 0,
        "B X": 0,
        "B Y": 3,
        "B Z": 6,
        "C X": 6,
        "C Y": 0,
        "C Z": 3,
    }
    scores_list = []
    with open("02.txt") as fp:
        for line in fp:
            _, you = line.strip().split()
            score = score_map[line.strip()] + (ord(you) - ord("W"))

            scores_list.append(score)
    return scores_list


if __name__ == "__main__":
    print(sum(part1()))
