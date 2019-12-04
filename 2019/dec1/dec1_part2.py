# adventofcode.com/2019
# december 1 2019
# part 2

import math
# open file in readmode
input_file = open('input.txt', 'r')

# read first line in file
line = input_file.readline()


def calc_fuel(mass_module):
    total_fuel = 0
    fuel = math.floor(mass_module / 3) - 2
    total_fuel += fuel
    while fuel > 0:
        fuel = math.floor(fuel / 3) - 2
        if fuel > 0:
            #print(fuel)
            total_fuel += fuel
    print(total_fuel)
    return total_fuel


# sets start total fuel amount
total_fuel = 0

# while there is a line in file
while line:
    #print(f'{line.strip()}')

    # read number on line in file
    mass = int(line.strip())

    # add fuel of one module and the fuel of the fuel to total amount of fuel
    total_fuel += calc_fuel(mass)
    
    # read next line
    line = input_file.readline()

# print total amount of fuel
print(f'Total amount of fuel: {total_fuel}')

# close file
input_file.close()
