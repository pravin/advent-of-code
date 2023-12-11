#!/usr/bin/env python3

def parse_input(input_string):
    games = {}
    for line in input_string.split('\n'):
        if line:
            game_id, rounds = line.split(': ')
            game_id = int(game_id.split(' ')[1])
            rounds = [dict((color, int(count)) for count, color in (pair.split(' ') for pair in round.split(', '))) for round in rounds.split('; ')]
            games[game_id] = rounds
    return games

def part1(input_data):
    possible_game_ids = []
    games = parse_input(input_data)
    possible_game_ids = []
    for game_id, rounds in games.items():
        possible = True
        for round in rounds:
            for color, count in round.items():
                if (color == 'red' and count > 12) or \
                   (color == 'green' and count > 13) or \
                   (color == 'blue' and count > 14):
                    possible = False
                    break
            if not possible:
                break
        if possible:
            possible_game_ids.append(game_id)
    return sum(possible_game_ids)

def calculate_min_cubes(games):
    min_cubes = {}
    for game_id, rounds in games.items():
        min_cubes[game_id] = {'red': 0, 'green': 0, 'blue': 0}
        for round in rounds:
            for color, count in round.items():
                min_cubes[game_id][color] = max(min_cubes[game_id][color], count)
    return min_cubes

def calculate_power(min_cubes):
    powers = {}
    for game_id, cubes in min_cubes.items():
        powers[game_id] = cubes['red'] * cubes['green'] * cubes['blue']
    return powers

def part2(input_string):
    games = parse_input(input_string)
    min_cubes = calculate_min_cubes(games)
    powers = calculate_power(min_cubes)
    return sum(powers.values())

input_data = open('02.txt', 'r').read()

print(part1(input_data))
print(part2(input_data))
