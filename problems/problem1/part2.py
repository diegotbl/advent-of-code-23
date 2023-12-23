import os
import subprocess
import re


forward_pattern = "1|2|3|4|5|6|7|8|9|one|two|three|four|five|six|seven|eight|nine"
backward_pattern = "1|2|3|4|5|6|7|8|9|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin"
dictionary = {"one": "1", "eno": "1",
              "two": "2", "owt": "2",
              "three": "3", "eerht": "3",
              "four": "4", "ruof": "4",
              "five": "5", "evif": "5",
              "six": "6", "xis": "6",
              "seven": "7", "neves": "7",
              "eight": "8", "thgie": "8",
              "nine": "9", "enin": "9"}


def main():
    original_input = open_input()
    answer = part2(original_input)
    print(answer)
    close_input(original_input)


def open_input():
    try:
        f1 = open('input.txt', "r")
        return f1
    except FileNotFoundError:
        print("Please check the path. Current working directory: " + os.getcwd())
        raise SystemExit


def part2(original_input):
    modified_input = open('modified_input.txt', "w")

    lines = original_input.readlines()
    for line in lines:
        first_digit = str(find_first_digit(line))
        last_digit = str(find_last_digit(line))
        calibration_value = first_digit + last_digit + "\n"
        write_calibration_value_in_new_file(calibration_value, modified_input)

    modified_input.close()

    return subprocess.run(["python", "part1.py", 'modified_input.txt'])


def find_first_digit(line):
    match = get_match(forward_pattern, line)
    return dictionary.get(match, match)


def find_last_digit(line):
    reverse_line = reverse_string(line)
    match = get_match(backward_pattern, reverse_line)
    return dictionary.get(match, match)


def get_match(pattern, line):
    match = re.search(pattern, line)
    if match is None:
        return "0"
    return match.group()


def reverse_string(string):
    return string[::-1]


def write_calibration_value_in_new_file(line, file):
    file.write(line)


def close_input(f1):
    f1.close()


if __name__ == "__main__":
    main()
