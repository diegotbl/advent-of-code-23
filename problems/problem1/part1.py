import sys
import os


def main():
    input_file_name = get_input_file_name(sys.argv)
    f = read_input(input_file_name)
    part1(f)
    close_input(f)


def get_input_file_name(arguments):
    print(arguments)
    if len(arguments) <= 1:
        return "input.txt"
    return arguments[1]


def read_input(input_file_name):
    try:
        f = open(input_file_name, "r")
        return f
    except FileNotFoundError:
        print("Please check the path. Current working directory: " + os.getcwd() + "requested file " + input_file_name)
        raise SystemExit


def part1(f):
    lines = f.readlines()
    total = 0
    for line in lines:
        first_digit = ''
        last_digit = ''
        for char in line:
            if char.isdecimal():
                if len(first_digit) == 0:
                    first_digit = char
                last_digit = char
        calibration_value = first_digit + last_digit
        if len(calibration_value) == 0:
            calibration_value = 0
        total += int(calibration_value)
    print(total)


def close_input(f):
    f.close()


if __name__ == "__main__":
    main()
