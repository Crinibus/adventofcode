def get_input():
    with open('D:\\PC\\Documents\\GitHub\\Crinibus\\adventofcode\\2020\\dec4\\input.txt', 'r') as input_file:
        input_raw = input_file.readlines()

    return [line.strip() for line in input_raw]


def get_answer_part_1():
    data = get_input()

    valid_passports = 0
    invalid_passports = 0

    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    next_passport = False
    
    current_num_fields = 0
    current_fields_string = ''

    for line in data:

        fields_on_line = line.split(' ')
        
        print(fields_on_line)

        if len(fields_on_line) == 1 and fields_on_line[0] == '':
            if all(field in current_fields_string for field in required_fields):
                valid_passports += 1
                print('Valid passport')
            else:
                invalid_passports += 1
                print('Invalid passport')

            print(f'Num of fields: {current_num_fields}\n')
            next_passport = True
            current_num_fields = 0
            continue

        if next_passport:
            current_fields_string = line
            next_passport = False
        else:
            current_fields_string += line

        current_num_fields += len(fields_on_line)

    print(f'\nValid passports: {valid_passports}')


get_answer_part_1()