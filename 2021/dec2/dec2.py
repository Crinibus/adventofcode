from typing import List
import pathlib


class Command:
    def __init__(self, input_string) -> None:
        string_command, value_string = input_string.split(" ")

        self.is_forward = True if string_command == "forward" else False
        self.value = -int(value_string) if string_command == "up" else int(value_string)


def get_input() -> List[Command]:
    root_path = pathlib.Path(__file__).parent.absolute()
    with open(f"{root_path}/input.txt", "r") as input_file:
        input_raw = input_file.readlines()

    return [Command(line.strip()) for line in input_raw]


def get_answer_part_1(input_data: List[Command]):
    horizontal = 0
    depth = 0

    for command in input_data:
        if command.is_forward:
            horizontal += command.value
        else:
            depth += command.value

    return horizontal * depth


def get_answer_part_2(input_data):
    horizontal = 0
    depth = 0
    aim = 0

    for command in input_data:
        if command.is_forward:
            horizontal += command.value
            depth += aim * command.value
        else:
            aim += command.value

    return horizontal * depth


def main():
    input_data = get_input()

    answer1 = get_answer_part_1(input_data)
    answer2 = get_answer_part_2(input_data)

    print(f"Part 1 answer: {answer1}")
    print(f"Part 2 answer: {answer2}")


if __name__ == "__main__":
    main()
