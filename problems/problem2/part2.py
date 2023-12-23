import os
import re


def main():
    f = read_input()
    answer = part2(f)
    print(answer)
    close_input(f)


def read_input():
    try:
        f = open('input.txt', "r")
        return f
    except FileNotFoundError:
        print("Please check the path. Current working directory: " + os.getcwd())
        raise SystemExit


def part2(f):
    lines = f.readlines()
    answer = 0

    for idx, line in enumerate(lines):
        max_number_of_cubes_in_game = find_max_number_of_cubes_in_game(line)
        min_amount_of_cubes_for_game_to_be_possible = max_number_of_cubes_in_game
        set_of_cubes_power = evaluate_set_of_cubes_power(min_amount_of_cubes_for_game_to_be_possible)
        answer += set_of_cubes_power

    return answer


def find_max_number_of_cubes_in_game(line):
    red_max = find_max_number_cubes_in_game_by_color("red", line)
    green_max = find_max_number_cubes_in_game_by_color("green", line)
    blue_max = find_max_number_cubes_in_game_by_color("blue", line)
    return [red_max, green_max, blue_max]


def find_max_number_cubes_in_game_by_color(color, line):
    pattern = "\\d+(?= " + color + ")"
    all_reveled_cube_amounts_by_color = re.findall(pattern, line)
    if len(all_reveled_cube_amounts_by_color) == 0:
        return 0
    return max(list(map(int, all_reveled_cube_amounts_by_color)))


def evaluate_set_of_cubes_power(set_of_cubes):
    power = 1
    for value in set_of_cubes:
        power *= value
    return power


def close_input(f):
    f.close()


if __name__ == "__main__":
    main()
