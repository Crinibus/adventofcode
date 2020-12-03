
def get_input():
    with open('input.txt', 'r') as input_file:
        input_raw = input_file.readlines()

    return [line.strip() for line in input_raw]


def get_answer_part_1():
    input_lines = get_input()
    
    num_correct_pass = 0

    for line in input_lines:
        rule = line.split(': ')[0]
        password = line.split(': ')[1]
        min_value = int(rule.split('-')[0])
        max_value = int(rule.split('-')[1].split(' ')[0])
        letter = rule.split(' ')[1]

        letter_num = password.count(letter)

        if (letter_num >= min_value and letter_num <= max_value):
            num_correct_pass += 1

    print(f'Answer part 1: {num_correct_pass}')


def get_answer_part_2():
    input_lines = get_input()
    
    num_correct_pass = 0

    for line in input_lines:
        rule = line.split(': ')[0]
        password = line.split(': ')[1]
        position_one = int(rule.split('-')[0])-1
        position_two = int(rule.split('-')[1].split(' ')[0])-1
        letter = rule.split(' ')[1]

        if password[position_one] == letter and password[position_two] != letter:
            num_correct_pass += 1
        elif password[position_one] != letter and password[position_two] == letter:
            num_correct_pass += 1

    print(f'Answer part 2: {num_correct_pass}')


get_answer_part_1()
get_answer_part_2()
        