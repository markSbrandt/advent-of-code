#https://adventofcode.com/2021/day/2

commands = []
with open('02-input.txt') as f:
    command = f.readline()
    while(command):
        commands.append(command)
        command = f.readline()

def generateFinalPosition(commands):
    location = [0,0,0] # horiz position, depth, aim

    for command in commands:
        parts = command.split()
        # "forward 5" {direction value}
        direction = parts[0]
        value = int(parts[1])

        if direction == "forward":
            location[0] = location[0] + value
            # location[1] aka depth = aim aka location[2] * value
            location[1] = location[1] + (location[2] * value)
        elif direction == "down":
            location[2] = location[2] + value
        elif direction == "up":
            location[2] = location[2] - value
        
    return location[0] * location[1]

finalLocationValue = generateFinalPosition(commands)
print(f'Final Location Value: {finalLocationValue}')