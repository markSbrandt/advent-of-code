#https://adventofcode.com/2021/day/1

import math

depths = []
with open("01-input.txt") as f:
    depthReading = f.readline()
    while depthReading:
        # read each depth and convert it to an int
        depths.append(int(depthReading))
        depthReading = f.readline()

def countIncreased(depths):
    increased = 0

    for depth in range(len(depths) - 1):
        if depths[depth] < depths[depth + 1]:
            print(f'increased from {depths[depth]} to {depths[depth + 1]}')
            increased = increased + 1

    return increased

depthIncreases = countIncreased(depths)
print(f'{depthIncreases} increased depths in {len(depths)} readings')

def countSlidingWindowIncreased(depths, windowLength):
    increased = 0

    for depth in range(len(depths) - windowLength):
        if depths[depth] + depths[depth+1] + depths[depth+2] < depths[depth+1] + depths[depth+2] + depths[depth+3]:
               increased = increased + 1 
    
    return increased

depthIncreases = countSlidingWindowIncreased(depths, 3)
print(f'{depthIncreases} increased depths in {len(depths)} readings')
