import pathlib
from collections import Counter


def get_input():
    root_path = pathlib.Path(__file__).parent.absolute()

    with open(f"{root_path}/input.txt", "r") as input_file:
        input_raw = input_file.readlines()

    return [line.strip() for line in input_raw]


def get_most_common_bit(input_data, index):
    index_data = [bits[index] for bits in input_data]

    index_string = "".join(index_data)

    bits_counter = Counter(index_string)

    return bits_counter.most_common(1)[0][0]


def get_least_common_bit(input_data, index):
    index_data = [bits[index] for bits in input_data]

    index_string = "".join(index_data)

    bits_counter = Counter(index_string)

    return bits_counter.most_common()[-1][0]


def get_answer_part_1(input_data):
    num_bits = len(input_data[0])

    gamma_rate_binary = ""

    for i in range(num_bits):
        gamma_rate_binary += get_most_common_bit(input_data, i)

    gamma_rate = int(gamma_rate_binary, 2)

    epsilon_rate_binary = ""

    for i in range(num_bits):
        epsilon_rate_binary += get_least_common_bit(input_data, i)

    epsilon_rate = int(epsilon_rate_binary, 2)

    return gamma_rate * epsilon_rate


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
