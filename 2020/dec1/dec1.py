
def get_input():
    with open('input.txt', 'r') as input_file:
        input_raw = input_file.readlines()

    return [int(line.strip()) for line in input_raw]


def get_answer_part_1():
    input_numbers = get_input()

    for num_one in input_numbers:
        for num_two in input_numbers:
            number = num_one + num_two
            
            if number == 2020:
                # print(f'{num_one}, {num_two}')
                num_multi = num_one * num_two
                print(f'Answer part 1: {num_multi}')
                return


def get_answer_part_2():
    input_numbers = get_input()

    for num_one in input_numbers:
        for num_two in input_numbers:
            for num_three in input_numbers:
                number = num_one + num_two + num_three
                
                if number == 2020:
                    # print(f'{num_one}, {num_two}, {num_three}')
                    num_multi = num_one * num_two * num_three
                    print(f'Answer part 2: {num_multi}')
                    return


get_answer_part_1()
get_answer_part_2()
