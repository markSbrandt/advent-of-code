#store most common bit in each position
nums_by_position = []

with open('03-input.txt') as f:
    binary_num = f.readline()
    line_number = 0
    while(binary_num):
        for num in range(len(binary_num)):
            if(binary_num[num].isnumeric()):
                if(len(nums_by_position) <= num):
                    nums_by_position.append([])
                nums_by_position[num].append(binary_num[num])
        binary_num = f.readline()

#nums_by_position should look like [[0,1,1,0,0],[1,0,1,1,0], ...]

gamma = ''
epsilon = []

for num in range(len(nums_by_position)):
    if(nums_by_position[num].count("0") > nums_by_position[num].count("1")):
        nums_by_position[num] = "0"
        epsilon.append("1")
    elif nums_by_position[num].count("0") < nums_by_position[num].count("1"):
        nums_by_position[num] = "1"
        epsilon.append("0")

#join binary parts to single "number"
gamma = ''.join(nums_by_position)
epsilon = ''.join(epsilon)

#convert base2 (binary) to base10 (decimal)
gammaValue = int(gamma,2)
epsilonValue = int(epsilon, 2)

#part1 answer
print(gammaValue * epsilonValue)