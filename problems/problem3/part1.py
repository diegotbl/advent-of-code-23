import os

total_rows = 140
total_columns = 140


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
    answer = 0
    data = fill_data(f)
    for row_number, row in enumerate(data):
        is_number_already_accounted_for = False
        for column_number, element in enumerate(row):
            if element.isdecimal():
                if is_number_already_accounted_for is False:
                    is_number_already_accounted_for = True
                    number, digit_amount = find_number(column_number, row)
                    if is_part_number(data, row_number, column_number, digit_amount):
                        answer += number
            else:
                is_number_already_accounted_for = False
    return answer


def fill_data(f):
    matrix = [['' for _ in range(total_columns)] for _ in range(total_rows)]
    lines = f.read().splitlines()
    for row_idx, line in enumerate(lines):
        matrix[row_idx] = list(line)
    return matrix


def find_number(position, row):
    number_string = ''

    for i in range(position, total_columns):
        if row[i].isdecimal():
            number_string += row[i]
        else:
            break

    number = int(number_string)
    digit_amount = len(number_string)

    return number, digit_amount


def is_part_number(data, row_number, column_number, digit_amount):
    answer = False

    y = row_number-1
    for x in range(column_number-1, column_number+digit_amount+1):
        answer = is_this_element_a_symbol(data, y, x) or answer

    y = row_number
    answer = is_this_element_a_symbol(data, y, column_number-1) or answer
    answer = is_this_element_a_symbol(data, y, column_number+digit_amount) or answer

    y = row_number+1
    for x in range(column_number-1, column_number+digit_amount+1):
        answer = is_this_element_a_symbol(data, y, x) or answer

    return answer


def is_this_element_a_symbol(data, row_number, column_number):
    if is_position_valid(row_number, column_number) is False:
        return False

    elem = data[row_number][column_number]
    return elem.isdecimal() is False and elem != '.'


def is_position_valid(row_number, column_number):
    return (0 <= row_number <= total_rows-1 and
            0 <= column_number <= total_columns-1)


def close_input(f):
    f.close()


if __name__ == "__main__":
    main()
