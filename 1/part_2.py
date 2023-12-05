from typing import List, Tuple


ALPHABETIC_DIGITS = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


NUMERIC_DIGITS = [
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


ALL_DIGITS = ALPHABETIC_DIGITS + NUMERIC_DIGITS


DIGITS_MAP = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def get_first_digit(line: str) -> int:
    all_digit_first_indexes_in_line = [(line.find(digit), digit) for digit in ALL_DIGITS]
    digit_first_indexes_in_line = [
        (index, digit)
        for index, digit in all_digit_first_indexes_in_line
        if index != -1
    ]

    first_digit = min(digit_first_indexes_in_line)[1]

    return convert(digit=first_digit)


def get_last_digit(line: str) -> int:
    all_digit_last_indexes_in_line = [(line.rfind(digit), digit) for digit in ALL_DIGITS]
    digit_last_indexes_in_line = [
        (index, digit)
        for index, digit in all_digit_last_indexes_in_line
        if index != -1
    ]

    last_digit = max(digit_last_indexes_in_line)[1]

    return convert(digit=last_digit)


def convert(digit: str) -> int:
    if digit in NUMERIC_DIGITS:
        return int(digit)
    if digit in ALPHABETIC_DIGITS:
        return DIGITS_MAP[digit]
    raise Exception("Unknown digit")

def combine(first: int, last: int) -> int:
    return int(str(first) + str(last))


def solve(file_name: str) -> int:
    numbers = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for line in lines:
            first_digit = get_first_digit(line)
            last_digit = get_last_digit(line)
            number = combine(first_digit, last_digit)
            numbers.append(number)

    return sum(numbers)

if __name__ == "__main__":
    result = solve("input.txt")
    print(result)
