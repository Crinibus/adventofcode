import pathlib


def get_input():
    root_path = pathlib.Path(__file__).parent.absolute()

    with open(f"{root_path}/input.txt", "r") as input_file:
        input_raw = input_file.readlines()

    return [line.strip() for line in input_raw]


def get_answer_part_1(input_data):
    pass


def get_answer_part_2(input_data):
    pass


def main():
    input_data = get_input()

    answer1 = get_answer_part_1(input_data)
    answer2 = get_answer_part_2(input_data)

    print(f"Part 1 answer: {answer1}")
    print(f"Part 2 answer: {answer2}")


if __name__ == "__main__":
    main()
