import pathlib


def get_input() -> list[str]:
    root_path = pathlib.Path(__file__).parent.absolute()

    with open(f"{root_path}/input.txt", "r") as input_file:
        input_raw = input_file.readlines()

    return [line.strip() for line in input_raw]


def get_priority_of_item(item: str) -> int:
    if item.islower():
        return ord(item) - 96

    return ord(item) - 64 + 26


def get_answer_part_1(input_data: list[str]):
    items: list[str] = []

    for line in input_data:
        half_length = len(line) // 2
        first_compartment, second_compartment = line[:half_length], line[half_length:]
        unique_items_first_compartment, unique_items_second_compartment = set(first_compartment), set(second_compartment)

        compartment_with_most_unique_items = max(unique_items_first_compartment, unique_items_second_compartment)
        compartment_with_least_unique_items = unique_items_second_compartment if compartment_with_most_unique_items is unique_items_first_compartment else unique_items_first_compartment

        for item in compartment_with_least_unique_items:
            if item not in compartment_with_most_unique_items:
                continue
            items.append(item)

    return sum((get_priority_of_item(item) for item in items))


def get_answer_part_2(input_data: list[str]):
    pass


def main():
    input_data = get_input()

    answer1 = get_answer_part_1(input_data)
    answer2 = get_answer_part_2(input_data)

    print(f"Part 1 answer: {answer1}")
    print(f"Part 2 answer: {answer2}")


if __name__ == "__main__":
    main()
