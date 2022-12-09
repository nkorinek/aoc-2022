from aocd.models import Puzzle
import pandas as pd
import numpy as np

puzzle = Puzzle(year=2022, day=5)

data = puzzle.input_data

test = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2"""

# boxes, instructions = test.split('\n\n')
boxes, instructions = data.split('\n\n')

instructions = instructions.split('\n')

boxes = boxes.split('\n')[:-1]

boxes = [box.replace('    ', ' ').split(' ') for box in boxes]

box_np = pd.DataFrame(boxes).values

box_rot = np.rot90(box_np, k=3).tolist()

box_vals = [[val for val in col if val != ''] for col in box_rot]

box_vals_2 = [[val for val in col if val != ''] for col in box_rot]

def box_mover(amount, from_col, to_col, boxes):
    for i in range(amount):
        box = boxes[from_col-1].pop()
        boxes[to_col-1].append(box)

instructs = []

for i in instructions:
    vals = i.split(' ')
    instructs.append([int(vals[1]), int(vals[3]), int(vals[5])])

for i in instructs:
    box_mover(i[0], i[1], i[2], box_vals)

answer = [top[-1].strip("[]") for top in box_vals]

solution_part_1 = "".join(answer)

print(solution_part_1)

def box_mover9001(amount, from_col, to_col, boxes):
    boxes_to_move = []
    for i in range(amount):
        boxes_to_move.append(boxes[from_col-1].pop())
    boxes_to_move.reverse()
    for box in boxes_to_move:
        boxes[to_col-1].append(box)

for i in instructs:
    box_mover9001(i[0], i[1], i[2], box_vals_2)

answer2 = [top[-1].strip("[]") for top in box_vals_2]

solution_part_2 = "".join(answer2)

print(solution_part_2)