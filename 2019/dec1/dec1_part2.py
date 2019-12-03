# adventofcode.com/2019
# december 1 2019
# part 2

import math
def forrige():
    # open file in readmode
    input_file = open('input.txt', 'r')

    # read first line in file
    line = input_file.readline()

    def calc_fuel(mass, index): # calculate fuel

        fuel = mass
        extra_fuel = fuel

        

        while fuel >= 0:
            fuel = math.floor(fuel / 3) - 2
            extra_fuel += fuel
            print(f'Index {index}, extra_fuel = {extra_fuel}')
        return extra_fuel

    # sets start total fuel amount
    total_fuel = 0
    index = 0

    # while there is a line in file
    while line:
        #print(f'{line.strip()}')

        # read number on line in file
        mass = int(line.strip())

        index += 1

        # add fuel of one module to total amount of fuel
        total_fuel += calc_fuel(mass, index)
        
        # read next line
        line = input_file.readline()

    # print total amount of fuel
    print(f'Total amount of fuel: {total_fuel}')

    # close file
    input_file.close()


data = [61302,
105953,
129165,
121039,
64799,
120172,
147328,
65147,
123112,
103573,
85213,
130378,
115416,
129131,
88809,
147043,
86119,
138383,
136803,
66719,
59465,
122491,
126551,
110028,
96959,
115214,
83823,
109324,
148671,
70505,
96375,
83861,
62724,
77493,
122275,
112894,
143872,
93525,
50526,
140725,
147110,
115859,
137582,
143800,
68830,
130259,
122393,
64373,
51810,
62449,
143889,
108038,
55083,
59927,
77613,
67488,
91711,
67498,
147320,
65348,
101088,
51983,
97705,
61890,
74561,
128456,
76450,
95132,
78835,
142148,
128037,
71497,
138382,
143474,
54236,
104095,
121533,
136757,
123213,
66306,
83269,
90894,
82215,
143024,
117140,
128722,
139823,
87177,
58107,
94303,
70008,
130633,
114210,
67931,
59062,
125819,
127278,
118718,
70968,
66126]

total_fuel = 0
fuel = 0

for mass in data:
    fuel = math.floor(mass / 3) - 2
    total_fuel += fuel
    while fuel > 0:
        fuel = math.floor(fuel / 3) - 2
        total_fuel += fuel

print(total_fuel)
    
