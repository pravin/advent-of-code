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


def part2():
    game_map = {
        "A": {  # Rock chosen
            "X": 3,  # X: You lose. 3: You chose scissors
            "Y": 1,  # Y: Draw. 1: You chose rock
            "Z": 2,  # Z: You win. 2: You chose paper
        },
        "B": {  # Paper chosen
            "X": 1,
            "Y": 2,
            "Z": 3,
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1,
        },
    }

    score = 0
    with open("02.txt") as fp:
        for line in fp:
            they, outcome = line.strip().split()
            score = score + game_map[they][outcome] + (ord(outcome) - ord("X")) * 3
    return score


if __name__ == "__main__":
    print(sum(part1()))
    print(part2())
