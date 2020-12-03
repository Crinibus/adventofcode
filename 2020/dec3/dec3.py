
def get_input():
    with open('input.txt', 'r') as input_file:
        input_raw = input_file.readlines()

    return [line.strip() for line in input_raw]



def get_answer_part_1():
    input_lines = get_input()

    trees_encountered = 0

    position = 0

    for index, origin_line in enumerate(input_lines):
        if index == 0:
            continue
        
        position += 3
        
        line = origin_line

        while position >= len(line):
            line += origin_line

        if line[position] == '#':
            trees_encountered += 1
        
    print(f'Answer part 1: {trees_encountered}')


def get_answer_part_2():
    input_lines = get_input()

    trees_encountered = 0

    list_slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

    list_encountered_trees = []

    for slope in list_slopes:
        trees_encountered = 0
        position = 0

        move_right = slope[0]
        move_down = slope[1]

        for index, origin_line in enumerate(input_lines):
            if index == 0:
                continue
            
            if move_down == 2 and index % 2 != 0:
                continue
            
            position += move_right

            line = origin_line

            while position >= len(line):
                line += origin_line

            if line[position] == '#':
                trees_encountered += 1


        list_encountered_trees.append(trees_encountered)

    answer = 1

    for num in list_encountered_trees:
        answer *= num


    print(f'Answer part 2: {answer}')


get_answer_part_1()
get_answer_part_2()