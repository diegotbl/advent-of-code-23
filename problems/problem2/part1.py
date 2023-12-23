import os
import re


total_cubes_rgb = [12, 13, 14]


def main():
    f = read_input()
    answer = part1(f)
    print(answer)
    close_input(f)


def read_input():
    try:
        f = open('input.txt', "r")
        return f
    except FileNotFoundError:
        print("Please check the path. Current working directory: " + os.getcwd())
        raise SystemExit


def part1(f):
    lines = f.readlines()
    answer = 0

    for idx, line in enumerate(lines):
        max_number_of_cubes_in_game = find_max_number_of_cubes_in_game(line)
        if is_game_possible(max_number_of_cubes_in_game):
            answer += (idx + 1)

    return answer


def find_max_number_of_cubes_in_game(line):
    red_max = find_max_number_of_revealed_cubes_in_game_by_color("red", line)
    green_max = find_max_number_of_revealed_cubes_in_game_by_color("green", line)
    blue_max = find_max_number_of_revealed_cubes_in_game_by_color("blue", line)
    return [red_max, green_max, blue_max]


def find_max_number_of_revealed_cubes_in_game_by_color(color, line):
    pattern = "\\d+(?= " + color + ")"
    all_reveled_cube_amounts_by_color = re.findall(pattern, line)
    if len(all_reveled_cube_amounts_by_color) == 0:
        return 0
    return max(list(map(int, all_reveled_cube_amounts_by_color)))


def is_game_possible(max_number_of_cubes_in_game):
    if max_number_of_cubes_in_game[0] > total_cubes_rgb[0] or \
            max_number_of_cubes_in_game[1] > total_cubes_rgb[1] or \
            max_number_of_cubes_in_game[2] > total_cubes_rgb[2]:
        return False
    return True


def close_input(f):
    f.close()


if __name__ == "__main__":
    main()
