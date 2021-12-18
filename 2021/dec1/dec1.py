import pathlib


def get_input():
    root_path = pathlib.Path(__file__).parent.absolute()
    with open(f"{root_path}/input.txt", "r") as input_file:
        input_raw = input_file.readlines()

    return [int(line.strip()) for line in input_raw]


def get_answer_part_1(input_data):
    num = 0

    for index, depth in enumerate(input_data):
        if depth > input_data[index - 1]:
            num += 1

    return num


def get_answer_part_2(input_data):
    num = 0

    for index, _ in enumerate(input_data):
        if index >= len(input_data) - 3:
            continue

        first = get_three_measurement(index, input_data)
        second = get_three_measurement(index + 1, input_data)

        if second > first:
            num += 1

    return num


def get_three_measurement(index, list):
    return list[index] + list[index + 1] + list[index + 2]


def main():
    input_data = get_input()

    answer1 = get_answer_part_1(input_data)
    answer2 = get_answer_part_2(input_data)

    print(f"Part 1 answer: {answer1}")
    print(f"Part 2 answer: {answer2}")


if __name__ == "__main__":
    main()
