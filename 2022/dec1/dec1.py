import pathlib


def get_input() -> list[str]:
    root_path = pathlib.Path(__file__).parent.absolute()

    with open(f"{root_path}/input.txt", "r") as input_file:
        input_raw = input_file.readlines()

    return [line.strip() for line in input_raw]


def get_elves(input_data: list[str]) -> list[tuple[int]]:
    elves = []

    temp_elf = []
    for calorie_line in input_data:
        if calorie_line == "":
            elves.append(tuple(temp_elf))
            temp_elf = []
            continue

        calorie = int(calorie_line)
        temp_elf.append(calorie)

    # remove empty elves
    elves = [elf for elf in elves if elf]
    return elves


def get_answer_part_1(input_data: list[str]):
    elves = get_elves(input_data)

    return max(sum(elf) for elf in elves)


def get_answer_part_2(input_data):
    elves = get_elves(input_data)

    sorted_elves = sorted((sum(elf) for elf in elves), reverse=True)
    return sum(sorted_elves[:3])


def main():
    input_data = get_input()

    answer1 = get_answer_part_1(input_data)
    answer2 = get_answer_part_2(input_data)

    print(f"Part 1 answer: {answer1}")
    print(f"Part 2 answer: {answer2}")


if __name__ == "__main__":
    main()
