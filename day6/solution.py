from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=6)

data = puzzle.input_data

input = data
# input = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"

indices = [0, 4]

idx = 0

for i in range(len(input)-3):
    string = input[indices[0]+i:indices[1]+i]
    if len(set(string)) == 4:
        idx = i+4
        break

print(idx)

idx2 = 0

indices2 = [0, 14]

for i in range(len(input)-3):
    string = input[indices2[0]+i:indices2[1]+i]
    if len(set(string)) == 14:
        idx2 = i+14
        break

print(idx2)

