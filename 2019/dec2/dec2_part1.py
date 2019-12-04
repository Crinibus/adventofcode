# adventofcode.com/2019
# december 2 2019
# part 1

input_list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]

index = 0

def intcode(index):
    if index == 0:
        index += 4
    opcode = input_list[index]
    x = input_list[index + 1]
    y = input_list[index + 2]
    position = input_list[index + 3]
    if opcode == 1:
        print(f'opcode: {opcode}')
        z = x + y
        input_list[position] = z
    elif opcode == 2:
        print(f'opcode: {opcode}')
        z = x * y
        input_list[position] = z
    elif opcode == 99:
        print('Opcode 99')
    return index

# num = 0
# while num < len(input_list):
#     intcode(index)
#     num += 1

# print(input_list)
# print(f'Number at position 0: {input_list[0]}')

# print('\n\n\n\n')

def test(index):
    test_list = [1,0,0,3]
    print(f'test_list: {test_list}')
    #index = 0
    opcode = test_list[index]
    print(f'opcode: {opcode}')
    x = input_list[index + 1]
    y = input_list[index + 2]
    position = input_list[index + 3]
    print(f'x: {x}, y: {y}, position: {position}')
    if opcode == 1:
        z = x*y
        print(f'x*y = {z}')
        test_list[position] = z
        print(f'position in list: {test_list[position]}')
        print(f'new test_liste: {test_list}')


def test_two2():
    test_list_two = [1,0,0,3,1,1,2,3]
    print(test_list_two)

def test_two(index):
    input_list = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,6,1,19,1,5,19,23,2,9,23,27,1,6,27,31,1,31,9,35,2,35,10,39,1,5,39,43,2,43,9,47,1,5,47,51,1,51,5,55,1,55,9,59,2,59,13,63,1,63,9,67,1,9,67,71,2,71,10,75,1,75,6,79,2,10,79,83,1,5,83,87,2,87,10,91,1,91,5,95,1,6,95,99,2,99,13,103,1,103,6,107,1,107,5,111,2,6,111,115,1,115,13,119,1,119,2,123,1,5,123,0,99,2,0,14,0]
    print(f'input_list: {input_list}')
    #index = 0
    opcode = input_list[index]
    print(f'opcode: {opcode}')
    x = input_list[index + 1]
    y = input_list[index + 2]
    position = input_list[index + 3]
    print(f'x: {x}, y: {y}, position: {position}')
    if opcode == 1:
        z = input_list[x] + input_list[y]
        print(f'x + y = {z}')
        input_list[position] = z
        print(f'position in list: {input_list[position]}')
        print(f'new input_liste: {input_list}')
    if opcode == 2:
        z = input_list[x] * input_list[y]
        print(f'x * y = {z}')
        input_list[position] = z
        print(f'position in list: {input_list[position]}')
        print(f'new input_liste: {input_list}')
    if opcode == 99:
        print(f'opcode is 99')
        print(f'position 0: {input_list[0]}')
    print()


index = 0
try:
    while True:
        test_two(index)
        index += 4
except:
    print(f'Position 0 is: {input_list[0]}')



